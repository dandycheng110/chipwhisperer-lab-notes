# 附錄 A　實驗環境與工具速查

> 本書的內容都可以在一台筆電上驗證。本附錄提供從零開始的環境與最常用的指令速查。

---

## A.1 本地實驗環境：Docker Desktop / kind / minikube

### 選哪一個

| 工具 | 適合 | 資源需求 | 特點 |
|---|---|---|---|
| **Docker Desktop** | 第七、八章（容器與 Compose） | 4 GB | 內建單節點 K8s，最省事 |
| **kind**（Kubernetes in Docker） | 第九～十三章 | 4–8 GB | **可建多節點集群**（測試調度、親和性），啟動最快 |
| **minikube** | 同上 | 4–8 GB | 附加元件豐富（ingress、metrics-server 一鍵開） |
| **k3d / k3s** | 資源吃緊、邊緣場景 | 2 GB | 極輕量 |

**本書建議：Docker Desktop（第 4 篇）+ kind（第 5 篇起）。**

### 安裝

```bash
# macOS
brew install --cask docker
brew install kind kubectl helm k9s stern kubectx

# Linux
curl -fsSL https://get.docker.com | sh
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind && sudo mv ./kind /usr/local/bin/kind
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl && sudo mv kubectl /usr/local/bin/
```

### 建立一個「像樣的」多節點集群

```yaml
# kind-cluster.yaml —— 1 控制面 + 3 工作節點，可測試拓撲分散
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - { containerPort: 80,  hostPort: 80,  protocol: TCP }
  - { containerPort: 443, hostPort: 443, protocol: TCP }
- role: worker
  labels: { topology.kubernetes.io/zone: zone-a }
- role: worker
  labels: { topology.kubernetes.io/zone: zone-b }
- role: worker
  labels: { topology.kubernetes.io/zone: zone-c }
```

```bash
kind create cluster --name shop --config kind-cluster.yaml
kubectl get nodes --show-labels

# 裝 Ingress Controller（第 10.2 節）
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

# 裝 metrics-server（HPA 必需，第 11.2 節）
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl patch deploy metrics-server -n kube-system --type=json \
  -p='[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'

# 清理
kind delete cluster --name shop
```

### 必裝的效率工具

| 工具 | 用途 |
|---|---|
| **k9s** | 終端機的 K8s 儀表板。**學 K8s 最好的工具，強烈推薦** |
| **stern** | 同時追蹤多個 Pod 的日誌：`stern item-service` |
| **kubectx / kubens** | 快速切換集群與命名空間 |
| **kubectl krew** | kubectl 插件管理器 |
| **dive** | 分析鏡像每一層的大小（第 7.2 節瘦身用） |
| **trivy** | 鏡像漏洞掃描 |

---

## A.2 Dockerfile 與 Compose 速查

### Dockerfile 指令

| 指令 | 說明 | 注意 |
|---|---|---|
| `FROM` | 基礎鏡像 | 固定版本，別用 `latest` |
| `RUN` | 建置時執行 | 多個指令用 `&&` 串起來減少層數 |
| `COPY` / `ADD` | 複製檔案 | **優先用 COPY**；ADD 會自動解壓縮與下載 URL，行為難預測 |
| `ENV` | 環境變數 | 建置期與執行期都有效 |
| `ARG` | 建置參數 | **只在建置期有效**，不會留在鏡像裡（適合傳版本號） |
| `WORKDIR` | 工作目錄 | 別用 `RUN cd`（不會持續） |
| `EXPOSE` | 宣告 port | **只是文件，不會真的開 port** |
| `USER` | 切換使用者 | 一定要設非 root |
| `VOLUME` | 宣告掛載點 | 會產生匿名 volume，小心磁碟被吃掉 |
| `HEALTHCHECK` | 健康檢查 | K8s 會用自己的探針，此項對 Compose 有用 |
| `ENTRYPOINT` / `CMD` | 啟動命令 | **用 exec form**（JSON 陣列），否則收不到 SIGTERM |

### 常用指令

```bash
# 建置
docker build -t myapp:1.0.0 .
docker build --build-arg VERSION=1.0.0 --platform linux/amd64,linux/arm64 -t myapp:1.0.0 .
docker buildx build --push --platform linux/amd64,linux/arm64 -t reg/myapp:1.0.0 .  # 多架構

# 執行
docker run -d --name app \
  -p 127.0.0.1:8080:8080 \
  -e SPRING_PROFILES_ACTIVE=dev \
  -v app-data:/data \
  --memory=2g --cpus=1.5 \
  --restart=unless-stopped \
  myapp:1.0.0

# 除錯
docker logs -f --tail 200 app
docker exec -it app sh
docker stats                      # 即時資源使用
docker inspect app | jq '.[0].State'
docker diff app                   # 容器相對鏡像改了什麼（查組態漂移）

# 清理（磁碟滿了必備）
docker system df                  # 看誰佔空間
docker system prune -a --volumes  # ⚠️ 會刪掉所有未使用的東西，含 volume
```

### Compose 速查

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f --tail 100 <service>
docker compose exec <service> sh
docker compose restart <service>
docker compose up -d --scale item-service=3
docker compose down            # 保留 volume
docker compose down -v         # 連 volume 一起刪
docker compose config          # 展開變數後的最終設定（除錯必用）
```

### Compose 檔常用片段

```yaml
services:
  app:
    build: { context: ., dockerfile: Dockerfile, args: { VERSION: "1.0" } }
    image: myapp:1.0.0
    env_file: [.env]
    environment: { KEY: value }
    ports: ["127.0.0.1:8080:8080"]
    volumes:
      - ./conf:/app/conf:ro          # bind mount，唯讀
      - app-data:/data               # 具名 volume
    depends_on:
      db: { condition: service_healthy }
    healthcheck:
      test: ["CMD", "curl", "-fsS", "http://localhost:8080/health"]
      interval: 10s
      timeout: 3s
      retries: 5
      start_period: 40s
    deploy:
      resources:
        limits: { cpus: "2", memory: 2g }
    restart: unless-stopped
    logging:
      driver: json-file
      options: { max-size: "10m", max-file: "3" }   # ⭐ 防止日誌撐爆磁碟
volumes: { app-data: {} }
networks: { backend: { driver: bridge } }
```

---

## A.3 kubectl 與 YAML 速查

### 高頻指令

```bash
# ── 查看 ───────────────────────────────────────
kubectl get pods -o wide -n shop
kubectl get all -n shop
kubectl get pods --sort-by=.status.containerStatuses[0].restartCount   # 找重啟最多的
kubectl get events --sort-by=.metadata.creationTimestamp -A | tail -30
kubectl describe pod <pod> -n shop            # ⭐ 90% 的問題看底部 Events

# ── 日誌 ───────────────────────────────────────
kubectl logs -f <pod> -c <container> -n shop
kubectl logs <pod> --previous                 # ⭐ 上次崩潰的日誌
kubectl logs -l app=item-service --tail=100 --max-log-requests=20   # 按 label 看多個

# ── 進入與轉發 ─────────────────────────────────
kubectl exec -it <pod> -- sh
kubectl port-forward svc/item-service 8080:80 -n shop
kubectl debug <pod> -it --image=nicolaka/netshoot   # ⭐ distroless 鏡像沒有 shell 時用這個

# ── 變更 ───────────────────────────────────────
kubectl apply -f manifests/
kubectl apply -k overlays/prod/               # Kustomize
kubectl set image deploy/item-service app=myapp:1.4.3
kubectl scale deploy/item-service --replicas=10
kubectl rollout status deploy/item-service
kubectl rollout undo deploy/item-service      # ⭐ 一鍵回滾
kubectl rollout restart deploy/item-service   # 重啟所有 Pod（滾動）

# ── 資源與除錯 ─────────────────────────────────
kubectl top nodes
kubectl top pods -n shop --sort-by=memory
kubectl get pod <pod> -o yaml                 # 看實際生效的完整設定
kubectl explain deployment.spec.strategy      # ⭐ 內建文件，不用查網頁
kubectl auth can-i create deployments -n shop
kubectl api-resources                         # 所有資源類型與縮寫

# ── 節點維運 ───────────────────────────────────
kubectl cordon node-1                          # 不再調度新 Pod
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data  # 驅逐（受 PDB 保護）
kubectl uncordon node-1

# ── 危險操作（知道就好）─────────────────────────
kubectl delete pod <pod> --grace-period=0 --force   # ⚠️ 強制刪除，可能造成資料不一致
```

### 一份「什麼都不缺」的 Deployment 骨架

複製這份，改名字就能用。**每一行都對應書中的一個教訓。**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: APP_NAME
  namespace: shop
  labels: { app: APP_NAME, team: TEAM, cost-center: CC, env: prod }   # 13.3 成本歸屬
spec:
  replicas: 3
  revisionHistoryLimit: 10
  selector: { matchLabels: { app: APP_NAME } }
  strategy:
    type: RollingUpdate
    rollingUpdate: { maxSurge: 1, maxUnavailable: 0 }                 # 9.4 零中斷
  template:
    metadata:
      labels: { app: APP_NAME, team: TEAM }
      annotations:
        checksum/config: "PLACEHOLDER"                                # 10.4 設定變更觸發滾動
    spec:
      terminationGracePeriodSeconds: 45                               # 7.3 優雅關閉
      securityContext:                                                # 7.3 非 root
        runAsNonRoot: true
        runAsUser: 10001
        fsGroup: 10001
      containers:
      - name: app
        image: registry.example.com/shop/APP_NAME:1.0.0               # 7.2 絕不用 latest
        imagePullPolicy: IfNotPresent
        ports: [{ name: http, containerPort: 8080 }]
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities: { drop: ["ALL"] }
        resources:                                                    # 11.3 必填
          requests: { cpu: "500m", memory: "1Gi" }
          limits:   { memory: "2Gi" }                                 # 11.3 CPU 可不設 limit
        envFrom:
        - configMapRef: { name: APP_NAME-config }
        - secretRef:    { name: APP_NAME-secret }
        env:
        - name: POD_NAME
          valueFrom: { fieldRef: { fieldPath: metadata.name } }
        - name: JAVA_OPTS
          value: "-XX:MaxRAMPercentage=70 -XX:+ExitOnOutOfMemoryError" # 7.1 容器感知
        startupProbe:                                                  # 11.1 慢啟動保護
          httpGet: { path: /actuator/health/liveness, port: http }
          failureThreshold: 30
          periodSeconds: 5
        livenessProbe:                                                 # 11.1 不檢查外部依賴
          httpGet: { path: /actuator/health/liveness, port: http }
          periodSeconds: 10
          failureThreshold: 3
        readinessProbe:
          httpGet: { path: /actuator/health/readiness, port: http }
          periodSeconds: 5
          failureThreshold: 2
        lifecycle:
          preStop: { exec: { command: ["sh","-c","sleep 5"] } }        # 9.3 端點傳播
        volumeMounts:
        - { name: tmp, mountPath: /tmp }                               # readOnlyRootFS 時需要
      volumes:
      - name: tmp
        emptyDir: {}
      topologySpreadConstraints:                                       # 11.4 高可用
      - maxSkew: 1
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: ScheduleAnyway
        labelSelector: { matchLabels: { app: APP_NAME } }
---
apiVersion: v1
kind: Service
metadata: { name: APP_NAME, namespace: shop }
spec:
  selector: { app: APP_NAME }
  ports: [{ name: http, port: 80, targetPort: http }]
---
apiVersion: policy/v1
kind: PodDisruptionBudget                                              # 11.1 保護驅逐
metadata: { name: APP_NAME-pdb, namespace: shop }
spec:
  minAvailable: 60%
  selector: { matchLabels: { app: APP_NAME } }
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler                                          # 11.2 彈性
metadata: { name: APP_NAME-hpa, namespace: shop }
spec:
  scaleTargetRef: { apiVersion: apps/v1, kind: Deployment, name: APP_NAME }
  minReplicas: 3
  maxReplicas: 50
  metrics:
  - type: Resource
    resource: { name: cpu, target: { type: Utilization, averageUtilization: 60 } }
  behavior:
    scaleUp:   { stabilizationWindowSeconds: 0 }
    scaleDown: { stabilizationWindowSeconds: 600 }
```

### 常見問題排查對照

| 現象 | 先看什麼 |
|---|---|
| Pod `Pending` | `kubectl describe pod` 的 Events：資源不足？PVC 綁不到？親和性衝突？ |
| `ImagePullBackOff` | tag 拼錯？私有倉庫 `imagePullSecrets`？節點能連到倉庫嗎？ |
| `CrashLoopBackOff` | `kubectl logs --previous`（**必用**） |
| `OOMKilled` | `describe` 看 Last State；檢查 JVM 參數與 limits |
| Running 但沒流量 | `kubectl get endpoints <svc>` 是空的嗎？→ readiness 沒過或 selector 標籤不匹配 |
| Service 連不通 | 1. endpoints 有沒有 2. Service 的 targetPort 對不對 3. NetworkPolicy 擋住了嗎 |
| Ingress 502 | 後端 Service 通嗎？`kubectl port-forward` 直連 Pod 測試 |
| 節點 `NotReady` | `kubectl describe node`：磁碟壓力？記憶體壓力？kubelet 掛了？ |
| 發布時有錯誤請求 | preStop + graceful shutdown + maxUnavailable:0 三件套有沒有齊 |

### PromQL 速查（第 13.2 節）

```promql
# 錯誤率
sum(rate(http_requests_total{code=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))

# P99 延遲
histogram_quantile(0.99, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))

# Pod 重啟次數（過去一小時）
increase(kube_pod_container_status_restarts_total[1h]) > 0

# CPU 節流比例（11.3 節）
rate(container_cpu_cfs_throttled_periods_total[5m]) / rate(container_cpu_cfs_periods_total[5m])

# 記憶體用量 vs limit
container_memory_working_set_bytes / container_spec_memory_limit_bytes > 0.9

# requests 浪費（13.3 節 FinOps）
sum by (namespace) (kube_pod_container_resource_requests{resource="cpu"})
  - sum by (namespace) (rate(container_cpu_usage_seconds_total[7d]))
```

---

**← 回到 [目錄](README.md)**
