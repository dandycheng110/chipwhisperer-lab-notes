# 第七章　打破部署地獄：Docker 容器技術登場

> **本章場景**：承接 6.4 節列出的六個痛點。本章解決前三個：
> 環境不一致、依賴衝突、擴容靠人肉（單機部分）。
> **讀本章時請隨時對照 6.4 節的地獄清單**——每一個 Docker 特性，都在殺一條具體的痛。

---

## 7.1 虛擬機 vs 容器：本質差異與隔離模型

### 先問：虛擬機不是已經解決隔離了嗎？

是的，虛擬機（VM）確實解決了隔離與環境打包。問題在於**成本**：

```
虛擬機：                          容器：
┌─────────┐┌─────────┐          ┌─────────┐┌─────────┐
│  App A  ││  App B  │          │  App A  ││  App B  │
│  Libs   ││  Libs   │          │  Libs   ││  Libs   │
│┌───────┐││┌───────┐│          └─────────┘└─────────┘
││Guest  ││││Guest  ││          ┌───────────────────┐
││OS 2GB ││││OS 2GB ││          │  Docker Engine    │
│└───────┘││└───────┘│          └───────────────────┘
└─────────┘└─────────┘          ┌───────────────────┐
┌───────────────────┐           │   Host OS Kernel  │  ← 共用同一個核心
│    Hypervisor     │           └───────────────────┘
└───────────────────┘           ┌───────────────────┐
┌───────────────────┐           │     實體機         │
│  Host OS / 實體機  │           └───────────────────┘
└───────────────────┘
```

| | 虛擬機 | 容器 |
|---|---|---|
| 隔離的東西 | 硬體（虛擬 CPU/記憶體/磁碟） | 進程（namespace + cgroup） |
| 每個實例含 | **完整 Guest OS（1–4 GB）** | 只有應用與依賴（**10–300 MB**） |
| 啟動時間 | **30 秒 – 2 分鐘**（要開機） | **50 毫秒 – 2 秒**（就是啟動一個進程） |
| 單機密度 | 10–20 個 | **100–1000 個** |
| 隔離強度 | **強（硬體級）** | 中（共用核心） |
| 效能損耗 | 5–15% | **接近 0** |

**關鍵洞察**：容器**根本不是輕量級虛擬機**。

> **容器只是一個「被限制了視野與資源的普通 Linux 進程」。**
> 你在宿主機上 `ps aux` 看得到它；`kill` 得掉它；它跟其他進程共用同一個核心。
> 它只是「以為」自己獨佔一台機器。

這解釋了所有事情：為什麼啟動這麼快（就是 fork+exec）、為什麼這麼省（沒有第二個 OS）、
為什麼隔離較弱（核心逃逸就全完了）、以及**為什麼 Linux 容器不能跑在 Windows 核心上**。

### 三根支柱

#### ① Namespace：限制「你看得到什麼」

| Namespace | 隔離什麼 | 效果 |
|---|---|---|
| PID | 進程編號 | 容器內 `ps` 只看到自己的進程，自己的主進程是 PID 1 |
| NET | 網路 | 容器有自己的網卡、IP、路由表、iptables、port 空間 |
| MNT | 掛載點 | 容器有自己的檔案系統視圖 |
| UTS | 主機名 | 容器有自己的 hostname |
| IPC | 進程間通訊 | 共享記憶體、訊號量隔離 |
| USER | 使用者 | 容器內的 root 可以映射成宿主的普通使用者 |
| CGROUP | cgroup 視圖 | 隱藏宿主的 cgroup 層級 |

```bash
# 親眼看見 namespace：容器內
$ docker run --rm -it alpine sh
/ # ps aux
PID   USER     COMMAND
    1 root     sh            ← 我是 PID 1，世界上只有我
    7 root     ps aux

# 同一時間，宿主機上
$ ps aux | grep sh
root  31847  ... /bin/sh     ← 同一個進程，宿主機看到的是 31847
```

**同一個進程，兩個編號。** 這就是 namespace 的全部魔法。

#### ② Cgroup：限制「你能用多少」

```bash
docker run -d --cpus=2 --memory=4g --memory-swap=4g myapp
```

- `--cpus=2`：最多用 2 核（CFS 配額，超過就被節流 throttle）。
- `--memory=4g`：超過就被 **OOM Killer 殺掉**（容器內的 OOM，不影響其他容器）。

**這一行直接解決了 6.4 節的地獄之二**：推薦服務再也不能吃掉 40 GB 記憶體把交易服務餓死。

> ⚠️ **JVM 與 cgroup 的經典坑**：JDK 8u191 以前的 JVM **看不到 cgroup 限制**，
> 它讀的是宿主機的總記憶體（例如 256 GB），於是把堆設成 64 GB，
> 然後在容器 4 GB 的限制下被 OOM Killer 秒殺，且**不會留下 Java 的 OOM 堆疊**。
> 排查起來極度痛苦（容器莫名重啟，日誌什麼都沒有）。
>
> 解法：用 JDK 11+（預設支援 `UseContainerSupport`），並用比例設定：
> ```
> JAVA_OPTS="-XX:MaxRAMPercentage=70 -XX:InitialRAMPercentage=70"
> ```
> 留 30% 給 metaspace、執行緒堆疊、直接記憶體與 JVM 本身。

#### ③ UnionFS / 聯合檔案系統：分層與共享

這是**鏡像**能夠存在的原因，也是 Docker 最精巧的設計，下一節細講。

### 什麼時候仍然該用虛擬機

容器不是萬能的：

| 場景 | 原因 |
|---|---|
| 多租戶執行不受信任的程式碼 | 共用核心，**核心漏洞 = 逃逸風險** |
| 需要不同核心或 Windows | 容器共用宿主核心 |
| 強合規隔離（金融、醫療） | 需硬體級隔離 |

中間路線：**安全容器**（Kata Containers、gVisor、Firecracker），
用輕量 VM 或使用者態核心包住容器，取得接近容器的啟動速度與接近 VM 的隔離。
這是 Serverless 平台的底層技術（第 12.3 節）。

---

## 7.2 Docker 三要素：Image / Container / Repository

### 三者關係

```
Dockerfile ──build──→ Image ──run──→ Container
   (食譜)              (冷凍食品)      (加熱後的餐點)
                         │
                       push/pull
                         ↓
                   Registry（倉庫：Docker Hub / Harbor / ACR / ECR）
```

| 名詞 | 是什麼 | 類比 |
|---|---|---|
| **Image 鏡像** | **唯讀**的分層檔案系統快照 + 啟動設定 | 類別（Class）、安裝光碟 |
| **Container 容器** | 鏡像 + 一層**可寫層** + 執行中的進程 | 物件（Instance） |
| **Registry 倉庫** | 存放與分發鏡像的服務 | Maven Central / npm registry |

### 分層儲存：為什麼鏡像不會佔爆磁碟

```dockerfile
FROM eclipse-temurin:17-jre-alpine    # Layer 1: 180 MB（基礎鏡像）
RUN apk add --no-cache curl           # Layer 2: 3 MB
COPY libs/ /app/libs/                 # Layer 3: 120 MB（第三方套件，很少變）
COPY app.jar /app/                    # Layer 4: 8 MB（你的程式，天天變）
```

```
       容器 A          容器 B          容器 C
    ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ 可寫層   │   │ 可寫層   │   │ 可寫層   │  ← 每個容器獨有，很小
    └────┬─────┘   └────┬─────┘   └────┬─────┘
         └──────────────┼──────────────┘
                 ┌──────▼───────┐
                 │ Layer 1~4    │  ← 唯讀，三個容器「共用同一份」
                 │ 磁碟只存一次 │
                 └──────────────┘
```

**效益**：
- 40 個 Java 服務共用同一個 `temurin:17-jre` 基礎層 → 磁碟只存一份 180 MB，不是 40 × 180 MB。
- 部署新版本時，只有 Layer 4（8 MB）改變 → **`docker pull` 只下載 8 MB**。
  這讓「發布 300 個實例」從搬運 300 × 300 MB 變成 300 × 8 MB。

**寫時複製（Copy-on-Write）**：容器修改唯讀層的檔案時，
先把它複製到可寫層再改，原始層不受影響。所以容器啟動不用複製任何東西——**這是毫秒級啟動的關鍵**。

### 分層的實務含義：Dockerfile 的指令順序決定建置速度

```dockerfile
# ❌ 錯誤：程式碼放前面
COPY . /app                  # 改一行程式 → 這層變了
RUN mvn dependency:go-offline # → 這層快取失效 → 重新下載 300 個 jar（5 分鐘）

# ✅ 正確：變動頻率低的放前面
COPY pom.xml /app/           # 只有依賴變更時才失效
RUN mvn dependency:go-offline # 有快取，跳過
COPY src /app/src            # 改程式只讓這層以後失效
RUN mvn package -o
```

> **黃金法則：Dockerfile 由上到下，依「變動頻率由低到高」排列。**
> 一層失效，其後所有層都會重建。

### 不可變基礎設施（Immutable Infrastructure）

這是容器帶來的**思想革命**，比技術本身更重要：

| 傳統（可變） | 容器（不可變） |
|---|---|
| SSH 上機器改設定、打補丁 | **禁止進容器改東西** |
| 機器越跑越「獨特」（雪花伺服器） | 每次部署都是全新的、一模一樣的實例 |
| 回滾 = 反向操作（可能失敗） | **回滾 = 換回舊鏡像 tag**（必定成功） |
| 「這台機器上到底裝了什麼？」沒人知道 | 看 Dockerfile 就知道全部 |

> **紀律：容器是「牲畜（cattle）」，不是「寵物（pet）」。**
> 寵物生病你帶它去看醫生（SSH 上去修）；牲畜生病你直接換一頭（殺掉重建）。
> 一旦你開始 `docker exec` 進去改設定，**你就把 6.4 節的組態漂移搬進容器裡了**，
> 而且下次重啟就會全部消失，製造出更難查的問題。

**推論：永遠不要用 `latest` 標籤。**

```bash
myapp:latest        # ❌ 今天的 latest 跟明天的 latest 不是同一個東西
myapp:1.4.2         # ✅ 語意化版本
myapp:git-a3f9c21   # ✅ 對應到確切的 commit（最推薦，可追溯）
myapp:2026-09-16-3  # ✅ 帶建置序號
```

`latest` 會讓「回滾到上一版」變成不可能的任務，也讓「這批機器跑的到底是哪個版本」無法回答。
（想起第 3.4 節 CDN 的「改內容就改 URL」嗎？**同一個不可變思想。**）

---

## 7.3 編寫 Dockerfile：把微服務打包為標準單元

### 一份生產級的 Java 服務 Dockerfile

```dockerfile
# ---------- Stage 1: 建置 ----------
FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /build

# 先只複製 pom，讓依賴層可以被快取
COPY pom.xml .
RUN mvn -B dependency:go-offline

COPY src ./src
RUN mvn -B package -DskipTests -o

# ---------- Stage 2: 執行 ----------
FROM eclipse-temurin:17-jre-alpine

# 1) 不要用 root 跑應用
RUN addgroup -S app && adduser -S -G app app

# 2) 時區與憑證（華人系統的經典坑：容器內是 UTC，日誌時間差 8 小時）
RUN apk add --no-cache tzdata ca-certificates curl \
    && cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime \
    && echo "Asia/Taipei" > /etc/timezone

WORKDIR /app
COPY --from=builder /build/target/*.jar app.jar
RUN chown -R app:app /app
USER app

# 3) 容器感知的 JVM 參數
ENV JAVA_OPTS="-XX:MaxRAMPercentage=70 \
               -XX:+UseG1GC \
               -XX:+ExitOnOutOfMemoryError \
               -Duser.timezone=Asia/Taipei \
               -Djava.security.egd=file:/dev/./urandom"

EXPOSE 8080

# 4) 健康檢查（K8s 會用自己的探針，但本地/Compose 很有用）
HEALTHCHECK --interval=15s --timeout=3s --start-period=40s --retries=3 \
    CMD curl -fsS http://localhost:8080/actuator/health || exit 1

# 5) exec form：讓 java 成為 PID 1，能收到 SIGTERM 優雅關閉
ENTRYPOINT ["sh", "-c", "exec java $JAVA_OPTS -jar app.jar"]
```

### 為什麼要多階段建置（Multi-stage Build）

| | 單階段 | 多階段 |
|---|---|---|
| 鏡像大小 | **750 MB**（含 Maven、JDK、原始碼、`~/.m2` 快取） | **190 MB**（只有 JRE + jar） |
| 安全 | **原始碼與建置憑證留在鏡像裡**（任何人 `docker run` 都能拿到） | 只有執行必需品 |
| 拉取速度 | 慢 | 快 4 倍 |

**鏡像大小直接影響擴容速度**：大促時要在 60 秒內啟動 200 個新實例，
190 MB 與 750 MB 的差別就是「來得及」與「來不及」。

### 五個高頻坑

#### 坑一：PID 1 與優雅關閉（最重要）

```dockerfile
# ❌ shell form：實際執行 /bin/sh -c "java -jar app.jar"
#    PID 1 是 sh，它不會把 SIGTERM 轉給 java
ENTRYPOINT java -jar app.jar

# ✅ exec form
ENTRYPOINT ["java", "-jar", "app.jar"]
# ✅ 或需要變數展開時，用 exec 取代 shell
ENTRYPOINT ["sh", "-c", "exec java $JAVA_OPTS -jar app.jar"]
```

**為什麼重要**：K8s 要停止 Pod 時發 `SIGTERM`，等待 `terminationGracePeriodSeconds`（預設 30 秒），
還沒死就 `SIGKILL`。如果 PID 1 是 sh，你的應用**永遠收不到 SIGTERM**，
每次滾動更新都會有請求被硬砍 → **每次發布都有一批使用者看到錯誤**。

對應的應用側設定：

```properties
server.shutdown=graceful                          # Spring Boot 優雅停機
spring.lifecycle.timeout-per-shutdown-phase=20s   # 給進行中的請求 20 秒處理完
```

#### 坑二：用 root 執行

容器內的 root 在某些設定下（特權模式、掛載宿主目錄、核心漏洞）可以影響宿主機。
**一律建立非 root 使用者。** K8s 可以強制執行：

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 10001
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities: { drop: ["ALL"] }
```

#### 坑三：把設定寫進鏡像

```dockerfile
COPY application-prod.properties /app/   # ❌ 一個鏡像只能跑一個環境
```

**十二要素應用（12-Factor App）第三條：設定來自環境變數。**

```bash
docker run -e SPRING_PROFILES_ACTIVE=prod \
           -e DB_URL=jdbc:mysql://prod-db:3306/shop \
           myapp:1.4.2
```

**同一個鏡像，走遍開發/測試/預發/生產**——這才是「環境一致」的真正含義。
如果各環境用不同鏡像，你測的就不是你上線的東西。

#### 坑四：日誌寫進檔案

```
❌ logback 寫到 /app/logs/app.log  → 容器一沒，日誌就沒了
✅ 寫到 stdout/stderr             → 由 Docker/K8s 收集，統一送到 ELK
```

12-Factor 第十一條：**把日誌當成事件流，而不是檔案。**

#### 坑五：`.dockerignore` 沒寫

```gitignore
# .dockerignore
.git
target/
node_modules/
*.log
.env
.idea/
```
沒寫的話，`COPY . .` 會把 `.git`（可能幾 GB）與 `.env`（含密碼！）打進鏡像。

### 鏡像安全檢查

```bash
trivy image myapp:1.4.2           # 掃 CVE 漏洞
docker scout cves myapp:1.4.2
syft myapp:1.4.2 -o spdx-json     # 產生 SBOM（軟體物料清單），合規必備
cosign sign myapp:1.4.2           # 簽章，確保部署的鏡像沒被掉包
```

> 供應鏈安全是 2020 年代的重點：你的鏡像裡有數百個你沒寫的套件。
> **基礎鏡像選擇建議**：`alpine`（小但 musl libc 可能有相容性問題）、
> `-slim`（Debian 精簡版，相容性好）、`distroless`（只有執行期，連 shell 都沒有，最安全）。

---

## 7.4 Docker Compose 實戰：一鍵啟動 微服務 + Redis + MySQL + Nginx

### 痛點：新人 onboarding 要三天

要在本機跑起系統，新同事得裝：MySQL、Redis、Nacos、RocketMQ、ES、還有 5 個服務……
裝到第三天還在查「為什麼我的 MySQL 是 5.7 但大家是 8.0」。

### 解法：把整套環境寫成一個檔案

```yaml
# docker-compose.yml
services:
  mysql:
    image: mysql:8.0.36                       # 精確版本，不用 latest
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD:-root123}
      MYSQL_DATABASE: shop
      TZ: Asia/Taipei
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    volumes:
      - mysql-data:/var/lib/mysql             # 具名 volume：資料不隨容器消失
      - ./sql/init.sql:/docker-entrypoint-initdb.d/init.sql:ro   # 首次啟動自動建表
    ports: ["3306:3306"]
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-p${MYSQL_ROOT_PASSWORD:-root123}"]
      interval: 10s
      timeout: 5s
      retries: 10
      start_period: 30s
    networks: [backend]

  redis:
    image: redis:7.2-alpine
    command: redis-server --appendonly yes --maxmemory 256mb --maxmemory-policy allkeys-lru
    volumes: [redis-data:/data]
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      retries: 5
    networks: [backend]

  item-service:
    build:
      context: ./item-service
      dockerfile: Dockerfile
    environment:
      SPRING_PROFILES_ACTIVE: docker
      # 注意：用「服務名」當主機名，Docker 內建 DNS 會解析
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/shop?useSSL=false&serverTimezone=Asia/Taipei
      SPRING_DATA_REDIS_HOST: redis
      JAVA_OPTS: "-XX:MaxRAMPercentage=70"
    depends_on:
      mysql:   { condition: service_healthy }   # 等 MySQL 真的可用，不只是「啟動了」
      redis:   { condition: service_healthy }
    deploy:
      replicas: 2                               # 起兩個副本，模擬集群
      resources:
        limits: { cpus: "1.0", memory: 1g }
    networks: [backend]

  trade-service:
    build: ./trade-service
    environment:
      SPRING_PROFILES_ACTIVE: docker
      ITEM_SERVICE_URL: http://item-service:8080   # 服務間用服務名互連
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/shop?useSSL=false
    depends_on:
      mysql: { condition: service_healthy }
    networks: [backend]

  nginx:
    image: nginx:1.25-alpine
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    ports: ["80:80"]
    depends_on: [item-service, trade-service]
    networks: [backend]

volumes:
  mysql-data:
  redis-data:

networks:
  backend:
    driver: bridge
```

```bash
docker compose up -d --build     # 一行，整套環境起來
docker compose ps                # 看狀態與健康檢查
docker compose logs -f trade-service
docker compose down              # 停掉（保留 volume）
docker compose down -v           # 連資料一起清掉，回到出廠設定
```

**新人 onboarding 從三天變成 10 分鐘。**

### Compose 的三個關鍵知識點

#### ① 服務名即 DNS

同一個自訂 network 內，Docker 提供內建 DNS：`mysql`、`redis`、`item-service`
自動解析到對應容器的 IP。

> **這是 K8s Service 的原型。** 第十章你會看到 `item-service.default.svc.cluster.local`
> ——同一個概念，只是跨主機了。

#### ② `depends_on` 的陷阱

```yaml
depends_on: [mysql]                            # ❌ 只等「容器啟動」，MySQL 可能還在初始化
depends_on:
  mysql: { condition: service_healthy }        # ✅ 等健康檢查通過
```

但**更根本的解法是讓應用自己重試**：

> **應用必須容忍依賴暫時不可用。**
> 在 K8s 環境下，DB 可能在你之後才就緒、可能中途重啟、可能故障轉移。
> 「啟動時連不上 DB 就直接退出」的應用，會在 K8s 裡陷入 `CrashLoopBackOff` 無限重啟。
> 正確做法：啟動時重試 + 就緒探針回報「還沒好」。

#### ③ Compose 能做什麼、不能做什麼

| Compose 能 | Compose 不能 |
|---|---|
| 單機多容器編排 | **跨多台主機** |
| 定義依賴與網路 | 自動故障轉移（容器掛了不會搬到別台） |
| `--scale` 起多副本 | 依負載自動擴縮容 |
| 本地開發、CI、小型部署 | 滾動更新與自動回滾 |

**定位**：Compose 是**開發與測試環境的神器**，不是生產編排工具。
（Docker Swarm 曾試圖補上這塊，但編排之戰已由 K8s 勝出。）

---

## 本章代價與下一章的痛

**我們做了什麼**：把每個服務打包成不可變鏡像，解決了環境不一致與依賴衝突；
用 Compose 讓整套環境一鍵啟動。

**對照 6.4 節的地獄**：

| 地獄 | 狀態 |
|---|---|
| ① 環境不一致 | ✅ **已解決**（鏡像包含完整執行環境） |
| ② 依賴衝突與資源打架 | ✅ **已解決**（namespace + cgroup） |
| ③ 擴容靠人肉 | 🟡 **單機解決了**（`docker run` 一秒），跨機器還沒 |
| ④ 發布無原子性 | 🟡 部分（鏡像可回滾，但多機協調還是靠腳本） |
| ⑤ 服務 IP 變動 | ❌ 未解決 |
| ⑥ 資源利用率 | 🟡 密度提高了，但仍是「人決定誰跑在哪台」 |

**我們買進的新問題**：
- 多了鏡像倉庫要維護（儲存、清理、權限、簽章）。
- 多了一層網路與儲存的抽象要理解（**下一章主題**）。
- 容器化本身不會讓爛架構變好：**有狀態的應用裝進容器，只會壞得更快。**

**新的痛點**：容器跑起來了，但立刻撞上兩個問題：

1. **容器之間怎麼通訊？** 跨主機的容器 IP 互不相通。
2. **資料存哪裡？** 容器一刪，MySQL 的資料就沒了。

下一章：[第八章　Docker 網路與儲存管理](08-Docker網路與儲存管理.md)。

---

## 名詞速查

| 名詞 | 一句話 |
|---|---|
| Namespace | 限制進程「看得到什麼」（PID/NET/MNT/UTS/IPC/USER） |
| Cgroup | 限制進程「能用多少」（CPU/記憶體/IO） |
| UnionFS / 分層 | 鏡像由唯讀層疊成，多容器共用，寫時複製 |
| 多階段建置 | 建置與執行分開，最終鏡像只留執行必需品 |
| 不可變基礎設施 | 不改機器只換鏡像；回滾＝換 tag |
| 牲畜 vs 寵物 | 壞了就換 vs 壞了就修 |
| PID 1 / SIGTERM | 容器主進程要能收到停止訊號才有優雅關閉 |
| 12-Factor App | 設定走環境變數、日誌走 stdout 等雲原生實務 |
| distroless | 連 shell 都沒有的極簡基礎鏡像 |
