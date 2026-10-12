# How the major world university rankings measure research citations (status as of 11 Oct 2026)

*Retrieval note for the report writer: the environment blocked direct page fetching (WebFetch DNS failure; the egress proxy refused CONNECT to timeshighereducation.com, support.qs.com, shanghairanking.com, usnews.com and elsevier.com). Every finding below comes from search-engine extracts of the cited pages, most of them official methodology pages. Short quotations are reproduced as the extracts returned them. A detail is marked "single extract" or "third-party" when only one source, or only a non-official source, supported it. I did not open any PDF directly.*

---

## Cross-cutting question: what must be true for a citation to count, and can a master's-thesis-to-master's-thesis citation ever register?

### Takeaway
Every ranking computes its citation indicators inside one closed bibliographic database: Elsevier Scopus (QS, THE, SCImago, and Webometrics "Excellence"), Clarivate Web of Science (US News, NTU Ranking, Leiden Traditional, and ARWU through its Highly Cited Researchers input), or OpenAlex (Leiden Open Edition, Webometrics "Openness"). A citation counts only if the **citing** document is indexed in that database. The **cited** item must be an indexed publication of an eligible document type, carry the university's affiliation, and fall inside the publication and citation windows. No ranking's documented eligible document types include master's theses. A thesis citing another thesis therefore has no documented route into QS, THE, ARWU, US News, Leiden, SCImago, Nature Index or NTU Ranking. Webometrics' OpenAlex-based "Openness" indicator (10%) is the only theoretical exception, and it is unverified.

### Cited Findings
**Summary table (latest editions released by Oct 2026)**

| Ranking (latest edition) | Citation database | Cited document types counted | Windows | Self-citation rule | Weight of citation-based indicators | Sources |
|---|---|---|---|---|---|---|
| QS WUR 2027 (released June 2026) | Scopus (annual Q1 extract) | Articles, reviews, conference papers, books, book chapters. Letters, editorials, notes, errata and press releases are excluded. | 5-year paper window, 6-year citation window | **Author-level** self-citations excluded. Institution-level self-citations are not excluded. | 20% (Citations per Faculty) | [QS CpF](https://support.qs.com/hc/en-gb/articles/360019107580-Citations-per-Faculty-Indicator); [QS processing](https://support.qs.com/hc/en-gb/articles/4411823040018-Processing-of-citations-and-papers) |
| THE WUR 2027 (released ~Oct 2026) | Scopus (Elsevier) | Journal articles, reviews, conference proceedings, books, book chapters (per the 2026 methodology) | Publications 2021–2025, citations 2021–2026 | No exclusion documented. An institutional self-citation **cap** is planned for the 2028 edition. | 30% (Research Quality pillar) | [THE 2027 method](https://www.timeshighereducation.com/world-university-rankings/methodology); [THE 2026 PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_world_university_rankings_2026_methodology.pdf); [THE metric changes](https://www.timeshighereducation.com/world-university-rankings/metric-modifications-will-help-maintain-rankings-quality) |
| ARWU 2026 | WoS SCIE/SSCI and Clarivate Highly Cited Researchers (HCR) list | "Article" type only (PUB, N&S) | PUB = papers from the previous year; N&S = 5 years | Not applicable (no citation counts used) | 0% direct. HiCi (20%) is citation-derived through the HCR list. | [ARWU 2025](https://www.shanghairanking.com/methodology/arwu/2025); [ARWU 2026](https://www.shanghairanking.com/methodology/arwu/2026) |
| US News BGU 2026–2027 | WoS Core Collection via InCites | Articles, notes, reviews. Letters, editorials and meeting abstracts are excluded. Books and conferences are separate indicators. | 2020–2024 | Not documented | ≥40% confirmed (≈50% if the top-1% indicators are unchanged) | [US News method](https://www.usnews.com/education/best-global-universities/articles/methodology) |
| CWTS Leiden Ranking 2025 (2026 edition due 4 Nov 2026) | WoS (Traditional) / OpenAlex (Open) | "Core publications": English-language articles and reviews in core international journals, not retracted | Publications 2020–2023, citations counted to end of 2024 | **Author** self-citations excluded | No composite score | [Leiden Open indicators](https://open.leidenranking.com/information/indicators); [Leiden Trad. indicators](https://traditional.leidenranking.com/information/indicators) |
| Webometrics (Jan 2026 / July 2026 editions) | Majestic (web links), OpenAlex (Openness), Scimago-Scopus (Excellence) | Excellence = top-10%-cited Scopus papers | Excellence 2020–2024; Openness 2021–2025 | Not documented | Excellence 40% and Openness 10% | [Webometrics Jan 2026 (figshare)](https://figshare.com/articles/preprint/Ranking_Web_of_Universities_webometrics_info_January_2026_edition/31132501); [Mahidol summary](https://stang.sc.mahidol.ac.th/research/ranking_Webometric.php) |
| SCImago SIR 2026 | Scopus | "Citable documents" = Article, Chapter, Conference Paper, Review, Short Survey | Not verified | Not verified | Part of the Research factor (50%) | [SIR methodology](https://www.scimagoir.com/methodology.php) |
| Nature Index 2026 | Own database of 177 journals plus 1 conference | Primary research articles | Calendar year / 12-month window | Not applicable | 0% (authorship counts only) | [Nature Index FAQ](https://www.nature.com/nature-index/faq); [Springer Nature PR](https://group.springernature.com/gp/group/media/press-releases/nature-index-expands-to-applied-and-social-sciences-with-release/52529418) |
| NTU Ranking 2026 (Taiwan) | Clarivate ESI and WoS (SCI/SSCI) | Not verified | 11 years (2015–2025), 2 years (2024–2025), current year (2025) | Not documented | 60% (impact 35%, h-index 10%, highly cited papers 15%) | [NTU Ranking indicators](https://nturanking.csti.tw/methodoloyg/indicators) |

**The database gate (citing side):**
- Scopus's "Cited by" count includes only citations from Scopus-indexed sources. Each database counts only citations from the sources it indexes, so totals differ between databases. — [CASRAI: Scopus vs Web of Science](https://casrai.org/compare/scopus-vs-web-of-science/); [Boston College Libraries "Times Cited" guide](https://libguides.bc.edu/articleinfluence/times_cited)
- The Web of Science "Times Cited" count is limited to sources WoS covers. A University of Michigan guide says it does "not count citations from ... books, conference proceedings, dissertations/theses, patents, technical reports or other types of publications." Note that the books and proceedings part is dated or simplified: WoS also has Conference Proceedings Citation Indices, which US News itself refers to. The dissertations/theses part is the point relevant here. — [U-Michigan Library WoS citation guide](https://guides.lib.umich.edu/citation/WebofScience); [US News methodology](https://www.usnews.com/education/best-global-universities/articles/methodology)
- SciVal (the Elsevier tool behind FWCI) computes standard FWCI **with self-citations included**, unless a user selects the "FWCI excluding self-citations" option. — [CASRAI guide: reading FWCI](https://casrai.org/guides/reading-and-reporting-fwci)
- Gaming of QS through Scopus volume has been documented. A Scientometrics study of Ukrainian universities found institutions "published extensively in Ukrainian Scopus-indexed, discontinued from Scopus and MDPI journals to increase output in Scopus rapidly." It also notes that QS does not normalise citations by document type, which affects how conference papers count. — [Scientometrics 2024, Ukrainian universities in QS](https://link.springer.com/article/10.1007/s11192-024-05165-2)
- Research-integrity critics argue that rankings "often lack safeguards against manipulation and rarely impose meaningful sanctions." They propose a Research Integrity Risk Index (RI²) based on retraction rates and reliance on delisted journals. — [Meho, Scientometrics 2025, "Gaming the metrics"](https://link.springer.com/article/10.1007/s11192-025-05480-2)

### Inferences
- **Direct answer to the student's question.** For a thesis citation to register in QS or THE, both the citing thesis and the cited professor's thesis would have to be Scopus-indexed items of an eligible type (article, review, conference paper, book or book chapter). For US News, ARWU or NTU Ranking they would have to be WoS Core Collection or ESI items of type article, note or review (or "Article" only for ARWU). For Leiden they would have to be core journal articles or reviews. Master's theses are none of these, so on the documented rules **the act has zero effect** on these rankings.
- **Webometrics is the only theoretical exception, and only if three unverified conditions hold:**
  1. OpenAlex indexes both theses.
  2. OpenAlex attributes them to the university through ROR.
  3. OpenAlex parses the citing thesis's reference list.

  Even then, the citation would enter only a 10%-weight indicator, and its effect would be negligible. Whether OpenAlex covers Taiwanese theses is outside my scope (another researcher covers thesis indexing).
- **Counterfactual: the student publishes a Scopus/WoS journal paper that cites professors' indexed papers.** How it counts depends on the ranking:
  - **THE and US News:** it counts. Neither documents a self-citation exclusion today. THE plans a cap on *institutional* self-citations from the 2028 edition.
  - **QS:** it counts only if no author is shared between the citing and cited papers. Excluded if the professor co-authored the student's paper (author-level exclusion).
  - **Leiden:** author self-citations are excluded.
  - **ARWU:** a single extra citation changes nothing, because ARWU counts papers, Nature/Science articles and HCR status, not citations.
- **Scale.** THE's 2027 dataset holds 188.7 million citations to 19.9 million publications, an average of about 9.5 citations per publication. One added citation is about 5×10⁻⁹ of that pool (arithmetic on THE's published totals; see the Scale section).

### Gaps
- No ranking's methodology page (in the extracts) says explicitly "theses are excluded". The exclusion follows from the positive lists of included document types and from database coverage. Whether Scopus, WoS or OpenAlex index any master's theses was out of scope for these notes.
- Whether citations *from* non-core or non-eligible document types (for example, a Scopus-indexed letter citing a ranked article) count on the citing side is not documented for QS, THE or US News in the extracts. QS's and THE's eligible-type lists apply to the *cited* (counted) publications.

---

## QS World University Rankings (2026 and 2027 editions): Citations per Faculty

### Takeaway
QS's only citation indicator is **Citations per Faculty (20%)**, which sits with Academic Reputation (30%, a survey) in the 50% "Research & Discovery" lens. It is computed from an annual Elsevier **Scopus** extract over a **5-year paper window and 6-year citation window**. It excludes **author-level self-citations** (since 2011) and caps hyper-affiliated papers. It is normalised so that each of five faculty areas contributes 20%. Only articles, reviews, conference papers, books and book chapters count. No new anti-manipulation rule for the 2026 or 2027 editions was found.

### Cited Findings
- **Weight (2026 and 2027).** Citations per Faculty is 20% of the overall score, in the "Research and Discovery" lens (50%) together with Academic Reputation (30%). — [QS methodology page](https://www.topuniversities.com/world-university-rankings/methodology); [QS methodology guide](https://www.qs.com/insights/world-university-rankings-methodology). Aggregators list the same 20% for the 2027 edition. — [mastergradschools QS 2027](https://mastergradschools.com/master-rankings/qs-world-university-rankings-2027); [xuanxiao QS 2027](https://xuanxiao.org/en/rankings/qs/world-university-rankings)
- **Release.** The QS WUR 2027 fact file was uploaded in June 2026, which shows the 2027 edition was out by then. — [QS WUR 2027 Fact file (via U.Porto)](https://noticias.up.pt/wp-content/uploads/2026/06/QS-World-University-Rankings-2027-Fact-file.pdf)
- **Data source.** Elsevier Scopus supplies the citation data. Citations per Faculty divides a normalised total citation count by reported faculty numbers. — [Elsevier: Understanding the QS WUR](https://www.elsevier.com/academic-and-government/qs-university-rankings-data); [QS: Citations per Faculty](https://support.qs.com/hc/en-gb/articles/360019107580-Citations-per-Faculty-Indicator)
- **Extract timing.** QS uses an annual Scopus extract, not the live database: "An extract is provided to us in Q1 of each year which is used for the new cycle of each ranking." — [QS: Citations per Faculty](https://support.qs.com/hc/en-gb/articles/360019107580-Citations-per-Faculty-Indicator); [QS Scopus User Guide](https://support.qs.com/hc/en-gb/articles/4411497775506-QS-Scopus-User-Guide)
- **Windows.** QS gathers "paper count over a five-year period and citations count for six years for papers published over a five-year period." The worked example given is the 2022 cycle: papers 2016–2020, citations 2016–2021. — [QS: Citations per Faculty](https://support.qs.com/hc/en-gb/articles/360019107580-Citations-per-Faculty-Indicator); also [Elsevier explainer](https://www.elsevier.com/academic-and-government/qs-university-rankings-data). QS's guide says citations up to the end of the calendar year before publication are counted (single extract). — [QS methodology guide](https://www.qs.com/insights/world-university-rankings-methodology)
- **Self-citations.** "We exclude citation of an author's own work by said author. We use an author-level definition of self-citations, as opposed to a journal-level or institution-level definition." Self-citations are excluded from all citation counts. — [QS: Processing of citations and papers](https://support.qs.com/hc/en-gb/articles/4411823040018-Processing-of-citations-and-papers); [QS: Citations per Faculty](https://support.qs.com/hc/en-gb/articles/360019107580-Citations-per-Faculty-Indicator)
- **Since 2011.** "A key development in 2011 was the exclusion of self-citations." This comes from a third-party copy (Scribd) of older QS text, not a dated primary QS page. QS's refinement-chronology page appeared in results but its text was not retrieved. — [Scribd copy of QS methodology text](https://www.scribd.com/document/418187286/Docs-Rems); [QS IU refinement chronology](http://www.iu.qs.com/university-rankings/refinement-chronology/)
- **Document types (Scopus definitions).** Included: articles, reviews, conference papers, books, book chapters. Excluded: letters, editorials, notes, errata, press releases. — [QS: Processing of citations and papers](https://support.qs.com/hc/en-gb/articles/4411823040018-Processing-of-citations-and-papers)
- **Affiliation cap (anti-distortion).** "An affiliation cap is applied discarding papers with an unusually high number of affiliations." The cap is "variable and calculated individually for each QS subject, ensuring no more than 0.1% (0.001) of research is excluded in a given field." — [QS: Processing of citations and papers](https://support.qs.com/hc/en-gb/articles/4411823040018-Processing-of-citations-and-papers)
- **Affiliation cap history.** In 2015 QS dropped papers with more than 10 affiliated institutions (about 0.34% of the database). In 2016 it replaced this with a discipline-sensitive cap. — [Scribd copy of QS text](https://www.scribd.com/document/418187286/Docs-Rems); [QS IU Citations per Faculty](http://www.iu.qs.com/university-rankings/indicator-citations-per-faculty/)
- **Faculty-area normalisation.** In the World and Regional rankings, "each of the five key faculty areas contributes 20% to the final indicator." Normalisation is not applied in Subject rankings. — [QS: Faculty Area Normalization](https://support.qs.com/hc/en-gb/articles/360021456540-Faculty-Area-Normalization); [QS: Processing](https://support.qs.com/hc/en-gb/articles/4411823040018-Processing-of-citations-and-papers)
- **Why normalisation was adopted (2015).** It offsets the fact that "a straight ratio of citations per faculty places a strong emphasis on life sciences and medicine." — [Scribd copy of QS text](https://www.scribd.com/document/418187286/Docs-Rems)
- **Eligibility threshold.** An institution needs at least **100 Scopus-indexed papers over a five-year period**, along with teaching-scope criteria. For 2026, QS added a requirement that institutions in the Arab Region, Asia, Europe and LAC be ranked in their regional ranking. — [QS: How to take part](https://support.qs.com/hc/en-gb/articles/360019131519-How-to-take-part-in-the-QS-rankings); [QS support: QS World University Rankings](https://support.qs.com/hc/en-gb/articles/4405955370898-QS-World-University-Rankings)
- **Regional rankings threshold.** "A minimum of 100 papers are required to be evaluated in this indicator." — [QS: Processing](https://support.qs.com/hc/en-gb/articles/4411823040018-Processing-of-citations-and-papers)
- **Subject rankings.** Thresholds vary by field (e.g., Life Sciences & Medicine 800 papers, Arts & Humanities 50). Institutions with low paper counts have their citation count reduced on a sliding scale, up to 10× the subject threshold. — [QS: Paper thresholds by subject](https://support.qs.com/hc/en-gb/articles/4406040194578-Paper-thresholds-by-subject); [QS: Processing](https://support.qs.com/hc/en-gb/articles/4411823040018-Processing-of-citations-and-papers)
- **No anomaly rule found.** A targeted search found no QS announcement of an anomalous-citation, citation-cartel, retraction or delisted-journal filter for the 2026 or 2027 editions. QS's public safeguards are the affiliation cap, author self-citation exclusion and normalisation. — [QS: Citations per Faculty](https://support.qs.com/hc/en-gb/articles/360019107580-Citations-per-Faculty-Indicator); [QS: Processing](https://support.qs.com/hc/en-gb/articles/4411823040018-Processing-of-citations-and-papers)

### Inferences
- **Inferred 2027 windows.** The "2022 cycle" example uses citations through 2021, which a Q1 extract can only contain if it was taken in early 2022. That cycle therefore corresponds to the edition published in June 2022 (WUR 2023). Applying the same rule:
  - QS WUR 2026 (published June 2025): papers ≈2019–2023, citations ≈2019–2024.
  - QS WUR 2027 (published June 2026): papers ≈2020–2024, citations ≈2020–2025.

  These dates are **inferred, not verified**.
- **Self-citation scope.** Because the exclusion is author-level, a citation from one professor's Scopus paper to a *different* professor's paper at the same university still counts. Institutional self-citation is not removed by QS.
- **Effect of one citation.** It is diluted three ways: divided by faculty numbers, normalised by faculty area, and scaled against the top institution. The effect of a single citation on a university's score is negligible (see the Scale section).

### Gaps
- The exact 2026 and 2027 paper and citation years could not be confirmed from a QS page.
- The International Research Network indicator (bibliometric co-authorship, not citations): its 2027 weight and Scopus basis were not verified in this session.
- Whether QS restricts the *citing* documents (e.g., excludes citations from errata or from discontinued titles) is not documented in the extracts.
- No primary QS page dated 2011 was retrieved for the start of self-citation exclusion.

---

## THE World University Rankings (2026 and 2027 editions, WUR 3.0) and the planned 2028 changes

### Takeaway
In THE WUR 2027 (released early Oct 2026), the **Research Quality pillar = 30%**, and all of it is citation-based: citation impact (mean FWCI) 15%, research strength 5%, research excellence 5%, research influence 5%. It is computed by Elsevier on **Scopus** from 19.9M publications (2021–2025) and 188.7M citations (2021–2026). Counted output types are journal articles, reviews, conference proceedings, books and book chapters. The eligibility threshold is ≥1,000 publications over 5 years and ≥100 per year. No self-citation exclusion is documented today. In late Sept 2026 THE announced that the **2028 edition** will **cap institutional self-citations** and reduce the weight of citation impact, citing outliers, manipulation, citation cartels and coercive citation.

### Cited Findings
- **Release.** THE published the WUR 2027 results with the press release "Asia overtakes continental Europe in THE World University Rankings 2027." — [THE press release](https://www.timeshighereducation.com/press-releases/asia-overtakes-continental-europe-world-university-rankings-2027)
- **2027 weights.** "Research quality: 30%". Citation impact 15%; research strength, research excellence and research influence 5% each. — [THE WUR 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology)
- **Indicator count.** The 2027 page describes "17 carefully calibrated performance indicators." — [THE WUR 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology)
- **2027 data and windows.** Data cover "more than 29,100 active peer-reviewed journals indexed by Elsevier's Scopus database and all indexed publications between 2021 and 2025." Citations to those papers made from 2021 to 2026 are counted. Elsevier supplied **188.7 million citations to 19.9 million publications**. — [THE WUR 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology)
- **2026 edition (for comparison).** Elsevier provided "174.9 million citations to 18.7 million journal articles, article reviews, conference proceedings, books and book chapters published over five years" (2020–2024). — [THE WUR 2026 methodology PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_world_university_rankings_2026_methodology.pdf)
- **Citation impact (15%).** Mean field-weighted citation impact per institution. FWCI compares a publication's citations with the average for "similar publications", defined as "publications in the Scopus database that have the same publication year, type, and discipline, as defined by the Scopus journal classification system (ASJC)." Citation data are calculated by Elsevier. — [THE WUR 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology); [THE 2026 methodology PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_world_university_rankings_2026_methodology.pdf)
- **Research strength (5%).** The 75th-percentile FWCI of an institution's papers, which is "less susceptible to the effect of extremely highly cited publications." — [THE 2026 methodology PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_world_university_rankings_2026_methodology.pdf); [THE 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology)
- **Research excellence (5%).** The number of publications in the global top 10% by FWCI, normalised by year, subject and staff numbers. — [THE 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology)
- **Research influence (5%).** An iterative, network-based measure: a citation from an "important" paper counts more than one from an "unimportant" paper. It considers both citation counts and the importance of the citing papers. — [THE 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology)
- **Other Scopus-derived indicators (not citation-based).** "Research productivity" counts publications in Scopus-indexed journals per scholar, scaled for size and normalised for subject. — [THE 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology)
- **Eligibility (2027).** The institution must have "published at least 1,000 research publications between 2021 and 2025, with at least 100 in each year." Institutions below this are "reporters" with no rank. An institution is also excluded if ≥80% of its output is in a single one of the 11 subject areas. — [THE 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology)
- **Eligibility wording (2026).** For 2020–2024 the 2026 PDF says "more than" 1,000 and "more than" 100, so the exact boundary wording varies. — [THE 2026 PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_world_university_rankings_2026_methodology.pdf)
- **Kilo-author papers.** Papers with more than 1,000 authors were excluded in 2015–16. From 2017 they were "reincorporated using a fractional counting approach" that gives every contributing university at least 5% of the paper's value. — [THE 2021 methodology PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_2021_world_university_rankings_methodology_24082020final.pdf); [THE 2025 methodology PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_2025_world_university_rankings_methodology.pdf)
- **Counting basis for the threshold: the sources conflict.**
  - The 2025 PDF says kilo-authored fractional counting was used "until the rankings published in 2023, when we changed to the full publication count." — [THE 2025 PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_2025_world_university_rankings_methodology.pdf)
  - The 2024 PDF dates the change to the 2024 rankings. — [THE 2024 PDF](https://www.timeshighereducation.com/sites/default/files/the_2024_world_university_rankings_methodology.pdf)
  - A 2026-era extract says "for the purposes of these metrics, as well as the publication threshold determination, we use the kilo-authored fractionally counted publication count." — [THE 2026 PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_world_university_rankings_2026_methodology.pdf)
- **Planned 2028 changes (announced ~late Sept 2026).** THE will "cap institutional self-citations" in its bibliometric analysis from the **2028 edition** (to be published autumn 2027). It will also adjust the research-quality metrics to reduce the weight of citation impact. THE says that metric "can be skewed by statistical outliers in universities with lower volumes of publication output, and can be vulnerable to active manipulation." THE rejected an outright ban because self-citation can be legitimate, and pointed to citation cartels and coercive citation. Thresholds and calculation details are "to come". The changes are "subject to public scrutiny and debate before being officially confirmed next year." — [THE: Metric modifications will help maintain rankings quality](https://www.timeshighereducation.com/world-university-rankings/metric-modifications-will-help-maintain-rankings-quality)
- **Third-party reading of the 2028 change.** A commentary says THE will not ban self-citation but will limit how many institutional self-citations count. — [xuanxiao THE 2027 commentary](https://xuanxiao.org/en/articles/the-world-university-rankings-2027-commentary)
- **Existing integrity stance (c. 2025).** THE runs ongoing "rankings integrity" reviews. It describes addressing attempted manipulation as "built into the DNA" of its rankings. It cites as defences the mix of data sources and 17 indicators, bibliometric normalisation, and its refusal to use journal metrics such as the JIF. — [THE: Protecting the integrity of university rankings](https://www.timeshighereducation.com/world-university-rankings/protecting-integrity-university-rankings)
- **Documented sanction (reputation survey, not citations).** In a documented manipulation case, a mutual-voting scheme among 21 universities in seven Arab countries, THE "neutralized" the votes rather than excluding institutions. — [Meho, Scientometrics 2025](https://link.springer.com/article/10.1007/s11192-025-05480-2)

### Inferences
- **Current self-citation status.** THE is only now proposing a cap on *institutional* self-citations, and SciVal's standard FWCI includes self-citations by default. So, as of the 2026 and 2027 editions, institutional self-citations most likely count in full. They are diluted only by FWCI normalisation and the percentile/top-10% design.
- **What THE counts.** THE counts Scopus-indexed outputs of five types. A master's thesis is neither a counted output nor (normally) a Scopus citing document.
- **Size of one extra citation.** One citation to a typical paper raises that paper's FWCI by about 1/(expected citations). With a global average of about 9.5 citations per publication in the 2027 window, that is about +0.1 for one paper. For an institution with about 20,000 papers in the window, the mean FWCI moves by roughly 5×10⁻⁶ (see Scale; illustrative).

### Gaps
- The 2027 document-type list was not confirmed verbatim. The five-type list comes from the 2026 PDF; the 2027 page extract describes "all indexed publications."
- Whether the minimum-5% kilo-author rule still applies in 2027 is not stated in the 2027 extract.
- The weights of the non-citation pillars for 2027, and which of WUR 3.0's original 18 indicators was dropped to reach "17", are not confirmed.
- The 2028 cap thresholds, and whether "institutional self-citation" will be defined via Scopus affiliation IDs, are not yet published.

---

## ARWU / ShanghaiRanking Academic Ranking of World Universities (2025 and 2026 editions)

### Takeaway
ARWU uses **no ordinary citation counts**. Its six indicators are Alumni 10%, Award 20%, HiCi 20%, N&S 20%, PUB 20% and PCP 10%. They count prizes, Clarivate **Highly Cited Researchers** (primary affiliation), Nature/Science articles, and SCIE/SSCI **"Article"-type** papers (SSCI counted double). Citations enter only indirectly, through Clarivate's HCR selection, which is based on top-1% WoS papers and includes integrity screening for excessive self-citation.

### Cited Findings
- **2025 weights.** Alumni 10%, Award 20%, HiCi 20%, N&S 20%, PUB 20%, PCP 10%. — [ARWU 2025 methodology](https://www.shanghairanking.com/methodology/arwu/2025)
- **N&S (2025).** The number of research articles published in Nature and Science 2020–2024. Credit by affiliation: "100% ... for corresponding author affiliation, 50% for first author affiliation" (where different), 25% for the next author's, 10% for others. "Only publications of 'Article' type are considered." — [ARWU 2025 methodology](https://www.shanghairanking.com/methodology/arwu/2025)
- **PUB (2025).** Papers indexed in SCIE and SSCI in 2024, 'Article' type only. "A special weight of two was introduced for papers indexed in Social Science Citation Index." — [ARWU 2025 methodology](https://www.shanghairanking.com/methodology/arwu/2025)
- **HiCi (2025).** Uses the Highly Cited Researchers list issued in November 2024. "Only the primary affiliations of Highly Cited Researchers are considered." — [ARWU 2025 methodology](https://www.shanghairanking.com/methodology/arwu/2025)
- **2026 edition.** ARWU 2026 uses the HCR list Clarivate issued in December 2025, primary affiliations only. A Taiwanese example of this is the Chang Gung University profile page. Each indicator is scaled so the top institution scores 100. Universities with "a significant amount of papers indexed in" SCIE/SSCI are also considered for inclusion. — [ARWU 2026 methodology](https://www.shanghairanking.com/methodology/arwu/2026); [ShanghaiRanking: Chang Gung University](https://www.shanghairanking.com/universities/chang-gung-university)
- **2026 windows (third-party only).** PUB = SCIE/SSCI papers of 2025, SSCI counted double; N&S = 2021–2025, author-position weighted. — [xuanxiao ARWU 2026 commentary](https://xuanxiao.org/en/articles/arwu-academic-ranking-of-world-universities-2026-commentary)
- **How HCR selection works (2025 list).** Selection is based on papers in the top 1% by citations for their field and year in the WoS Core Collection over the past 11 years, across 20 fields plus Cross-Field. The 2025 list recognised 6,868 individuals with 7,131 awards. Clarivate says it screens for "hyper-prolific authorship, excessive self-citation, anomalous publication and citation patterns." — [Clarivate HCR 2025 announcement](https://clarivate.com/news/clarivate-announces-highly-cited-researchers-2025-list/); [Clarivate: How HCRs are selected](https://clarivate.com/highly-cited-researchers/evaluation-and-selection/)

### Inferences
- **No route for thesis citations.** No ordinary citation count enters ARWU; PUB and N&S are publication counts. A thesis-to-thesis citation therefore cannot affect ARWU.
- **The only citation-sensitive lever.** That lever is producing a Highly Cited Researcher, which requires top-1% WoS papers, and Clarivate screens out anomalous self-citation patterns.
- **Effective citation-derived weight.** HiCi carries 20%, plus a tiny share of PCP (10%), which is computed from the other indicators per academic staff.

### Gaps
- I could not open the ARWU 2026 page beyond the extract, so the 2026 PUB and N&S definitions rely on a third-party summary plus the year-on-year pattern. They are probably unchanged, but unverified.
- Clarivate's numeric self-citation thresholds for HCR exclusion were not retrieved.

---

## U.S. News & World Report Best Global Universities (2025–2026 and 2026–2027 editions)

### Takeaway
US News BGU 2026–2027 uses **Clarivate InCites / Web of Science Core Collection** data for 2020–2024 across 13 indicators, with weights "unchanged from the prior edition". Confirmed citation-based weights total **40%**: normalised citation impact 10%, total citations 7.5%, number of top-10% papers 12.5%, share of top-10% papers 10%. The remaining 10% belongs to the top-1% highly cited paper indicators in prior editions. Only **articles, notes and reviews** count as publications. No self-citation exclusion is documented.

### Cited Findings
- **2026–2027 structure.** "Global rankings are calculated using 13 indicators and weights"; the weights are unchanged from the prior edition. The edition covers 2,250 universities in 105 countries. — [US News 2026–2027 methodology](https://www.usnews.com/education/best-global-universities/articles/methodology)
- **Weights.**
  - Number of top-10%-cited papers 12.5%.
  - Share of top-10% papers 10%.
  - Total citations 7.5%, computed as "the publications ranking factor" × "the normalized citation impact factor".
  - Normalised citation impact 10%.
  - International collaboration 5%, plus international collaboration relative to country 5%.
  - Global and regional research reputation 12.5% each (Clarivate Academic Reputation Survey 2021–2025).
  - Publications 10%; books 2.5%; conferences 2.5%.
  
  — [US News 2026–2027 methodology](https://www.usnews.com/education/best-global-universities/articles/methodology); [US News 2024–2025 methodology](https://www.usnews.com/education/best-global-universities/articles/methodology?page=3); a third-party summary of 2026–2027 also gives publications, books and conferences as 15% in total. — [xuanxiao US News 2027 commentary](https://xuanxiao.org/en/articles/usnews-best-global-universities-2027-commentary)
- **Data source.** "For all nonreputation indicators, Best Global Universities rankings data comes from the Clarivate product InCites. InCites contains all of the Web of Science Core Collection." The 2026–2027 bibliometric window is 2020–2024. The 2025–2026 edition (released 17 June 2025) used 2019–2023. — [US News 2026–2027 methodology](https://www.usnews.com/education/best-global-universities/articles/methodology); [US News 2025–2026 subject methodology](https://www.usnews.com/education/best-global-universities/articles/subject-rankings-methodology?page=2); [US News release-date post](https://www.usnews.com/education/blogs/college-rankings-blog/articles/2025-06-03/2025-2026-best-global-universities-rankings-coming-june-17)
- **Document types.** "Only papers with the document types of 'articles,' 'notes' and 'reviews' were considered." Letters, editorials and meeting abstracts are excluded. Proceedings published in WoS Core Collection journals are classed as articles and included. Proceedings from the Conference Proceedings Citation Indices are "usually excluded" from the publication-based indicators; the separate "conferences" indicator covers them. — [US News methodology](https://www.usnews.com/education/best-global-universities/articles/methodology)
- **How weights were set.** "Based on our judgment of the relative importance of the ranking factors and in consultation with Clarivate's bibliometric experts." — [US News 2024–2025 methodology](https://www.usnews.com/education/best-global-universities/articles/methodology?page=3)
- **InCites normalisation.** InCites' Category Normalized Citation Impact divides actual citations by the expected citation rate for documents of the same document type, publication year and subject area. — [QUT Library guide: CNCI](https://libguides.library.qut.edu.au/c.php?g=427625&p=7059823)
- **InCites self-citation metric.** InCites has a separate "Times Cited without Self-Citations" metric. There, a self-citation is "a citation received from the same entity that provided the citation", i.e., the organisation level. — [InCites help: Times Cited without Self-Citations](https://incites.zendesk.com/hc/en-gb/articles/25087162457233-Times-Cited-without-Self-Citations-and-H-Index-without-Self-Citations)

### Inferences
- **Citation-based share.** Confirmed citation-based weight is 40%. If the two top-1% indicators (5% + 5%) persist, as the arithmetic of a 100% total implies, citation-based indicators carry about 50% of the score.
- **Self-citations.** Nothing indicates US News uses the without-self-citation variant, so institutional and author self-citations are presumably included.
- **Theses.** Theses are not WoS Core Collection articles, notes or reviews, and WoS "Times Cited" does not count citations from theses. A thesis-to-thesis citation therefore has no effect here.

### Gaps
- **Top-1% weights.** The 2026–2027 weights of the two "highly cited papers (top 1%)" indicators were not shown in the extracts; 5% + 5% is inferred from the arithmetic and prior editions.
- **Citation cut-off.** The citation end date (InCites extraction date) was not found.
- **Self-citations.** No US News statement on self-citations was found.
- **Taiwan university data.** The US News profile page for National Taiwan University (#233, global score 59.6) returned jumbled indicator-rank pairings, so per-indicator values are not reported here. — [US News: National Taiwan University](https://www.usnews.com/education/best-global-universities/national-taiwan-university-504077)

---

## CWTS Leiden Ranking: Traditional Edition (Web of Science) and Open Edition (OpenAlex)

### Takeaway
Leiden counts only **core publications**: English-language, non-retracted **articles and reviews** with named authors in "core" international journals. It **excludes author self-citations**, recommends **fractional counting**, and uses 4-year publication windows (2025 edition: 2020–2023, citations to end of 2024). It produces **no composite score**. The 2025 editions appeared ~29 Oct 2025, and the 2026 edition(s) are due **4 Nov 2026**. In July 2026 CWTS announced it will stop using WoS, so **from 2027 only the OpenAlex-based Open Edition will remain**.

### Cited Findings
- **Core publications only.** Indicators are calculated only on core publications in international scientific journals. Criteria: written in English, one or more authors, not retracted, published in a core journal. — [Leiden Traditional: indicators](https://traditional.leidenranking.com/information/indicators); [Leiden Open: indicators](https://open.leidenranking.com/information/indicators)
- **Article and review only.** "Only research articles and review articles are taken into account." — [Leiden Ranking 2024 methodology PDF](https://traditional.leidenranking.com/Content/CWTS%20Leiden%20Ranking%202024.pdf)
- **Core journals.** The Open Edition requires that a core journal "has a sufficiently large number of references to other core journals." — [Leiden Open: indicators](https://open.leidenranking.com/information/indicators)
- **Self-citations and citation window.** Author self-citations are excluded in both editions. "Citations are counted until the end of 2024" for the current (2025) indicators. — [Leiden Open: indicators](https://open.leidenranking.com/information/indicators); [Leiden Traditional: indicators](https://traditional.leidenranking.com/information/indicators)
- **Counting method.** Full and fractional counting are both available, and fractional counting is preferred for impact indicators. Worked example: 2 of 5 authors from a university gives a weight of 0.4. Indicators such as MNCS, TNCS and top-x% are field-normalised. — [Leiden Ranking 2024 methodology PDF](https://traditional.leidenranking.com/Content/CWTS%20Leiden%20Ranking%202024.pdf); [Leiden Open: indicators](https://open.leidenranking.com/information/indicators)
- **2025 editions.** The CWTS post on the 2025 release is dated 29 Oct 2025. The Open Edition 2025 covers 2,831 universities (publications 2020–2023) and added "non-core publications". The Traditional Edition covers over 1,500 universities. — [Leiden Madtrics: Leiden Ranking 2025](https://www.leidenmadtrics.nl/articles/the-cwts-leiden-ranking-2025-more-open-more-inclusive-more-informative); [Univ. Freiburg on Open Edition 2025](https://uni-freiburg.de/en/cwts-leiden-ranking-open-edition-2025-the-university-of-freiburg-placed-ninth-nationally-among-the-top-1-publications/); [Leiden Open: updates](https://open.leidenranking.com/information/updates)
- **Open Edition data.** The 2025 Open Edition is reportedly built on an August 2025 OpenAlex snapshot (single extract), with data and code openly released. — [Zenodo: Open Edition 2025 data](https://zenodo.org/records/17471989); [GitHub releases](https://github.com/CWTSLeiden/CWTS-Leiden-Ranking-Open-Edition/releases)
- **WoS exit (July 2026).** A joint CWTS–Clarivate statement says CWTS "will discontinue the use of Web of Science data, both in the Leiden Ranking and in the services we offer to external organisations." — [Leiden University news, July 2026](https://www.universiteitleiden.nl/en/news/2026/07/cwts-takes-next-step-in-open-research-information-transition)
- **2026 releases and after.** Search extracts say both the Traditional Edition 2026 and the Open Edition 2026 "will be released on November 4, 2026", and that "from 2027 onward, the Traditional Edition ... will be discontinued." — [Leiden Traditional site](https://traditional.leidenranking.com/); [Leiden Open site](https://open.leidenranking.com/); [Leiden University news](https://www.universiteitleiden.nl/en/news/2026/07/cwts-takes-next-step-in-open-research-information-transition)
- **No composite score.** Leiden "refrains from arbitrarily combining multiple dimensions of university performance in a single aggregate indicator." Users sort by one indicator at a time. — [Leiden Ranking 2011/2012 paper](https://arxiv.org/pdf/1202.3941); [Leiden: responsible use](https://traditional.leidenranking.com/information/responsibleuse); [CWTS ten principles](https://www.cwts.nl/blog?article=n-r2q274)

### Inferences
- **Latest edition as of 11 Oct 2026.** The latest released Leiden data (2025 edition) cover publications 2020–2023. The 2026 edition, presumably 2021–2024 with citations to end of 2025, is not out until 4 Nov 2026.
- **Theses.** Theses are not core journal articles or reviews, so they cannot enter Leiden's impact indicators. Author self-citations are removed in any case.

### Gaps
- What "non-core publications" includes in the Open Edition 2025, and whether it ever covers dissertation-type OpenAlex works, was not determined. Its use appears limited to output views; unverified.
- Whether citations *from* non-core publications are counted on the citing side was not confirmed in the extracts.
- The 2026 time window was not confirmed.

---

## Webometrics (Ranking Web of Universities, CSIC Cybermetrics Lab): does any indicator still rely on Google Scholar?

### Takeaway
**No longer.** Webometrics' "Openness" indicator (10%) used Google Scholar citation data from 2016 until 2025. Webometrics could no longer obtain Google Scholar data, so **since the July 2025 edition Openness is computed from OpenAlex via ROR identifiers**. "Excellence" (40%) is the count of an institution's **top-10%-cited Scopus papers** (Scimago data, 27 disciplines, 2020–2024). "Visibility/Impact" (50%) is web inlinks from Majestic. The Google Scholar pathway through which theses could have registered is therefore gone. Only the OpenAlex-based 10% remains as a theoretical, unverified path.

### Cited Findings
- **January 2026 edition.** Posted 23 Jan 2026 by Isidro F. Aguillo, DOI 10.6084/m9.figshare.31132501. It covers more than 32,000 HEIs. Indicators are "collected from reliable sources such as Majestic, OpenAlex, and Scimago-Scopus." Web data are gathered in early January. Bibliometric periods are "2020 to 2024 (Excellence) and 2021-2025 (Openness)." — [Webometrics January 2026 edition, figshare](https://figshare.com/articles/preprint/Ranking_Web_of_Universities_webometrics_info_January_2026_edition/31132501)
- **Weights and definitions.** Visibility 50% (Majestic inlinks). Excellence 40%: "top 10% cited papers for each one of the 27 disciplines in the period 2020-2024 (Scimago)." "Presence" has been discontinued. — [Mahidol Univ. library summary of Webometrics](https://stang.sc.mahidol.ac.th/research/ranking_Webometric.php)
- **July 2026 edition.** A site styled as Webometrics lists the "July 2026 ... 2nd Edition – Final" with Impact 50%, Openness 10%, Excellence 40%, and Majestic as the web-impact source. Caution: webometrics.org may not be the official CSIC domain, which is webometrics.info. — [webometrics.org](https://www.webometrics.org/)
- **Google Scholar dropped (2025).** The Webometrics website "ceased to function in 2025 due to an inability to obtain citation data from Google Scholar. From July 2025 onwards, the Openness indicator values for citations have been calculated using OpenAlex via the ROR identifier." Data are now distributed via figshare and, on a paid basis, as twice-yearly Excel files. — [Moskovkin 2025 preprint, "From Google Scholar to OpenAlex" (ResearchGate)](https://www.researchgate.net/publication/394543432_New_Methodology_for_Calculating_Webometrics_University_Ranking_From_Google_Scholar_to_OpenAlex)
- **Openness history.**
  - It originally counted PDF files found through Google Scholar.
  - From the second half of 2016 it shifted to Google Scholar citations, at 10% weight. — [Moskovkin preprint](https://www.researchgate.net/publication/394543432_New_Methodology_for_Calculating_Webometrics_University_Ranking_From_Google_Scholar_to_OpenAlex)
  - An older description says the indicator used "the citation counts of the 110 most cited authors of that institution, according to Google Scholar" (same preprint).
  - CSIC's related Google-Scholar-based analysis took data "directly from Google Scholar Citations" rather than WoS or Scopus. — [Aguillo et al., arXiv 2005.03324](https://arxiv.org/pdf/2005.03324)
- **Excellence weight: sources conflict.** The Moskovkin preprint gives 30%, older descriptions give 35%, and the Mahidol page and webometrics.org give 40%. — [Moskovkin preprint](https://www.researchgate.net/publication/394543432_New_Methodology_for_Calculating_Webometrics_University_Ranking_From_Google_Scholar_to_OpenAlex); [Mahidol](https://stang.sc.mahidol.ac.th/research/ranking_Webometric.php)

### Inferences
- **Google Scholar route closed.** The user's hypothesis that Webometrics registers thesis citations via Google Scholar applied only to editions up to January 2025. It no longer applies.
- **What remains.** The only remaining citation input open to non-journal items is the OpenAlex-based Openness indicator (10%). OpenAlex does index some repository content, but whether it holds Taiwanese master's theses with parsed references and ROR-linked affiliations is for the thesis-indexing researcher to establish.
- **Size of any effect.** Even if such citations registered, they would add to a 10%-weight indicator measured over a whole institution's OpenAlex record. One citation would have no measurable effect.

### Gaps
- The exact current Openness formula (total citations, top-cited authors, or top-cited works; any exclusions) under OpenAlex was not retrieved from an official CSIC page.
- Self-citation handling is undocumented.
- The official status of webometrics.org versus webometrics.info is unclear.

---

## Briefly: SCImago Institutions Rankings, Nature Index, NTU Ranking (國立臺灣大學世界大學科研論文質量評比)

### Takeaway
**SCImago SIR** is Scopus-based (Research 50%, Innovation 30%, Societal 20%) and uses citable documents only. **Nature Index** uses no citations at all: it counts authorship of primary research articles in a curated list, which expanded in June 2026 to 177 journals plus 1 conference. **NTU Ranking 2026** is built on Clarivate ESI/WoS SCI-SSCI, and about 60% of its weight is citation-based (11-year and 2-year citations, h-index, highly cited papers).

### Cited Findings
- **SCImago structure.** A composite on a 0–100 scale: Research 50% (includes Normalized Impact, Excellence with Leadership, High Quality Publications), Innovation 30%, Societal 20%. — [SCImago SIR methodology](https://www.scimagoir.com/methodology.php)
- **SCImago impact indicators.**
  - Normalized impact = the ratio of an institution's average scientific impact to the world average for papers in the same period and subject area.
  - Excellence = the share of papers in the top 10% most cited, normalised by field and year.
  
  — [SCImago SIR methodology](https://www.scimagoir.com/methodology.php)
- **SCImago inclusion.** At least 100 works in Scopus in the last year of the period. "Citable documents (Article, Chapter, Conference Paper, Review and Short Survey) must represent at least 75%" of output. For SIR 2026, Altmetrics was replaced by a "Media Mentions" metric. — [SCImago SIR methodology](https://www.scimagoir.com/methodology.php)
- **Nature Index metrics.** Count gives 1 for each article with at least one author from the institution. Share is fractional: 1 per article divided equally among authors, so 10 authors get 0.1 each. Adjusted Share corrects for annual variation in article totals. — [Nature Index FAQ](https://www.nature.com/nature-index/faq); [Nature Index brief guide](https://www.nature.com/nature-index/brief-guide)
- **Nature Index June 2026 expansion.** It added 17 applied-science journals plus one conference and 15 social-science journals. It now tracks 177 journals plus 1 conference (178 publications), about 125,000 articles in 2025. Subjects are now assigned per article. A beta applied-sciences ranking ran in December 2025. — [Springer Nature press release](https://group.springernature.com/gp/group/media/press-releases/nature-index-expands-to-applied-and-social-sciences-with-release/52529418); [Nature Index: Major changes for 2026](https://www.nature.com/nature-index/news/major-changes-nature-index)
- **NTU Ranking 2026 indicators.**
  - Research Productivity 25%: 11-year articles (2015–2025) 10%; current-year articles (2025) 15%.
  - Research Impact 35%: 11-year citations 15%; 2-year citations (2024–2025) 10%; 11-year average citations 10%.
  - Research Excellence 40%: h-index (2024–2025) 10%; Highly Cited Papers (2015–2025) 15%; current-year articles in high-impact journals 15%.
  
  — [NTU Ranking: Indicators](https://nturanking.csti.tw/methodoloyg/indicators)
- **NTU Ranking data source.** "Prior data is drawn from ESI, which covers the data for the articles indexed by SCI and SSCI from 2015 to 2025." Current-year searches were run in April 2026. — [NTU Ranking: Indicators](https://nturanking.csti.tw/methodoloyg/indicators)
- **NTU Ranking design.** Eight indicators in three criteria, using up to 11 years of publication and citation data. — [Univ. of Toronto news on NTU Ranking](https://www.utoronto.ca/news/u-t-fourth-globally-second-among-public-universities-ntu-research-rankings); [IREG profile](https://ireg-observatory.org/en/initiatives/international-ranking?rankingid=7)
- **NTU Ranking history.** It succeeds the HEEACT ranking. The weights have stayed broadly stable while the windows roll forward; the 2016-era version used 2006–2016 for the 11-year indicators at the same 10% and 15% weights. — [USP University Performance Metrics: NTU Ranking](https://metricas.usp.br/rankings/04-ntu/en/); [Wikipedia: Performance Ranking of Scientific Papers for World Universities](https://en.wikipedia.org/wiki/Performance_Ranking_of_Scientific_Papers_for_World_Universities)

### Inferences
- **NTU Ranking and theses.** NTU Ranking is Taiwan's own ranking and is about 60% citation-based, but only on WoS SCI/SSCI and ESI data. Master's theses, whether citing or cited, are invisible to it.
- **Nature Index and theses.** Nature Index uses no citations, so a citation of any kind is irrelevant to it.
- **SCImago and theses.** SCImago's citable-document list (Article, Chapter, Conference Paper, Review, Short Survey) excludes theses.

### Gaps
- SCImago's publication and citation window and its self-citation handling were not retrieved.
- NTU Ranking's document-type filter (ESI normally restricts to articles and reviews) was not confirmed on the NTU Ranking page, nor were its self-citation handling and the 2026 release date.
- Nature Index's FAQ extract did not explicitly state "no citations". The conclusion follows from its metric definitions.

---

## Scale: how small is one citation relative to institutional and global totals?

### Takeaway
THE's 2027 Scopus dataset contains **188.7 million citations to 19.9 million publications**, about 9.5 citations per paper. A Taiwanese research university contributes thousands of indexed papers a year; NCKU's research portal lists about 3,900–4,600 outputs per year for 2022–2024. One extra citation is a vanishingly small fraction of an institution's citation base: on the order of 10⁻⁶ of its mean FWCI. Verified institution-level Scopus/WoS citation totals for NTU, NTHU, NYCU or NCKU could not be retrieved.

### Cited Findings
- **Global totals.** THE WUR 2027: 188.7M citations to 19.9M publications (2021–2025 publications, citations through 2026; 29,100+ journals). THE WUR 2026: 174.9M citations to 18.7M publications. — [THE WUR 2027 methodology](https://www.timeshighereducation.com/world-university-rankings/methodology); [THE WUR 2026 methodology PDF](https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_world_university_rankings_2026_methodology.pdf)
- **NCKU research portal.** It lists 2024: 3,942 outputs; 2023: 4,283; 2022: 4,642. The portal does not state whether the counts come from Scopus, so treat them as a university-repository count. — [NCKU research output portal](https://researchoutput.ncku.edu.tw/en/publications/)
- **NTU (Taiwan): third-party totals.** EduRank (own database, third-party, low reliability) gives about 153,985 publications and about 4.13 million citations (cumulative, all fields). — [EduRank: National Taiwan University](https://edurank.org/uni/national-taiwan-university/rankings/)
- **NTU (Taiwan): Top 2% scientists.** 229 NTU scholars are on the 2024 "Top 2% of Global Scientists" list, which uses Scopus data as of 1 Aug 2024 with citations counted to end of 2023. — [NTU Lab Spotlight](https://labspotlight.ntu.edu.tw/en/vision/cmta2dby3013za9htd3ww6kpn)
- **Nature Index counts.** NTU was first in Taiwan for natural sciences, with Count 236 in 2023. NCKU's profile shows Count 184 and Share 57.70 for its 12-month window. — [Nature Index 2024 Research Leaders, Taiwan natural sciences](https://www.nature.com/nature-index/annual-tables/2024/institution/all/natural-sciences/countries-Taiwan); [Nature Index: NCKU](https://www.nature.com/nature-index/institution-outputs/taiwan/national-cheng-kung-university-ncku/513906bb34d6b65e6a000207)
- **Database totals differ.** Scopus and WoS give different publication and citation totals. SciVal's publication count can differ from the count a ranking uses, because rankings include only specific document types. — [NCCU Library guide](https://www.lib.nccu.edu.tw/p/406-1000-4547,r105.php?Lang=zh-tw)

### Inferences
These are illustrative arithmetic on the sourced numbers, not measured values.
- **Global average.** 188.7M / 19.9M ≈ **9.5 citations per publication** in THE's 2027 window.
- **Share of the global pool.** One citation is about 1/188,700,000 ≈ **5×10⁻⁹** of THE's citation pool.
- **Share of one university's citations.** A university with about 4,000 outputs/year has about 20,000 in a 5-year window. At the global average that implies roughly 190,000 window citations. One added citation is about **0.0005%** of that.
- **Effect on THE's mean FWCI.** One added citation to an average paper raises that paper's FWCI by about 1/9.5 ≈ 0.1. The institution's mean FWCI then rises by about 0.1/20,000 ≈ **5×10⁻⁶**, far below the one-decimal precision at which overall scores are published.
- **Under QS.** QS's per-faculty, faculty-area-normalised and top-scaled transformation dilutes the effect similarly.
- **This holds only if the citation counts at all.** For theses, it does not (see the cross-cutting section).

### Gaps
- No verified SciVal/Scopus or InCites/WoS annual publication and citation totals were found for NTU, NTHU, NYCU or NCKU. Official university reports (研發處 annual reports) or SciVal/InCites exports would be needed.
- The NTU research homepage shows "論文總數 57,400+", but the label-to-number mapping in the extract was unclear, so it is not used here. — [臺大研究](https://www.ntu.edu.tw/research/research.html)
