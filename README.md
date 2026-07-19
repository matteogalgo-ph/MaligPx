# **MaligPx**

MaligPx is a computational systems biology framework under **active development** for quantifying malignant cell fate plasticity in pancreatic ductal adenocarcinoma (PDAC) using single-cell RNA sequencing (scRNA-seq). The project integrates transcriptomic preprocessing, RNA velocity, probabilistic fate inference, regulatory network analysis, and statistical modeling into a fully reproducible analytical pipeline designed to investigate cellular plasticity during malignant progression.
Unlike conventional analyses that primarily classify malignant cells into discrete transcriptional subtypes, MaligPx is being developed to estimate each malignant cell's propensity to transition between alternative developmental states. The framework introduces the **Fate State Ambiguity Index (FSAI)**, a quantitative metric derived from CellRank fate probabilities that measures the degree of developmental uncertainty exhibited by individual malignant cells.
The project is being developed as an independent scientific research project and emphasizes computational reproducibility, transparent documentation, modular software engineering, and complete provenance tracking from raw sequencing data through downstream biological interpretation.

# **Research Objective**

The primary objective of MaligPx is to develop, validate, and evaluate a computational framework capable of identifying highly plastic malignant cells within pancreatic ductal adenocarcinoma using single-cell transcriptomic data.
The framework seeks to determine whether probabilistic cell-fate inference can provide biologically meaningful information beyond conventional subtype classification by integrating transcriptomic similarity, developmental trajectories, RNA velocity, and regulatory network activity.

# **Scientific Background**

Pancreatic ductal adenocarcinoma is characterized by extensive intratumoral heterogeneity, dynamic transcriptional programs, and substantial phenotypic plasticity. Existing subtype classifications, including the Classical and Basal-like continuum, describe malignant populations but do not directly quantify the uncertainty associated with future cellular state transitions.
Recent advances in trajectory inference, RNA velocity, and Markov-state modeling provide the opportunity to estimate probabilistic developmental outcomes for individual cells rather than assigning deterministic labels.
MaligPx combines these computational advances into a unified workflow that estimates fate probabilities for every malignant cell and derives a continuous plasticity metric suitable for downstream statistical analysis.

# Current development status
Current milestone (7/18/2026):
**MD-2 — Data Acquisition and Dataset Preparation**
Completed milestones include:
* Computational environment initialization
* Scientific software installation
* Version control initialization
* Reproducible environment specification
* Repository architecture
* Documentation framework
* GitHub repository publication
* Dataset identification and repository audit
Current work focuses on acquisition of the Peng et al. (2019) discovery cohort and preparation of the computational preprocessing pipeline.

---

# Methodological overview
The planned computational workflow consists of the following major stages.
1. Raw sequencing data acquisition.
2. Generation of gene-expression count matrices from raw FASTQ files.
3. Quality control and preprocessing using Scanpy.
4. Batch integration and dimensionality reduction.
5. Identification of malignant epithelial cells.
6. Construction of CellRank transition kernels.
7. GPCCA macrostate identification.
8. Computation of the Fate State Ambiguity Index (FSAI).
9. Differential expression analysis.
10. Functional enrichment analysis.
11. Gene regulatory network analysis.
12. Statistical hypothesis testing.
13. Biological interpretation and visualization.
Each stage is documented independently to ensure that every analytical result can be traced back to its originating dataset and computational environment.

# Project architecture
The repository follows a modular directory structure designed to separate raw data, processed data, software components, documentation, configuration, analyses, and generated outputs.
```text
MaligPx/
│
├── configs/
├── data/
│   ├── raw/
│   ├── intermediate/
│   ├── processed/
│   └── velocity/
│
├── docs/
├── figures/
├── logs/
├── notebooks/
├── references/
├── results/
├── scripts/
├── src/
├── tests/
│
├── environment.yml
├── environment.lock.yml
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── .gitattributes
```
The repository structure intentionally separates permanent source data from intermediate computational products to simplify provenance tracking and minimize accidental modification of irreplaceable datasets.

# Documentation
Project documentation is maintained throughout development rather than generated retrospectively.
Major documentation files include:
| Document                   | Purpose                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| `docs/dataset_manifest.md` | Records provenance and acquisition status of every dataset.                                |
| `docs/data_dictionary.md`  | Maintains metadata describing every biological sample and sequencing run.                  |
| `docs/acquisition_log.md`  | Chronological record of every dataset acquisition event.                                   |
| `research_log.md`          | Scientific progress log documenting methodological development and experimental decisions. |
| `engineering_log.md`       | Software engineering and implementation history.                                           |
| `project_log.md`           | High-level project milestone summary.                                                      |
| `decisions.md`             | Architectural and methodological decision record.                                          |

**Computational environment**
The project is developed using:
* Miniforge
* Conda
* Mamba
* Python 3.10
Primary scientific libraries include:
* Scanpy
* AnnData
* scVelo
* CellRank
* NumPy
* SciPy
* Pandas
* Matplotlib
* NetworkX
* igraph
* Leidenalg
* scikit-learn
* Statsmodels
* Scrublet
Additional environments are maintained where necessary for software packages whose dependency constraints conflict with the primary analytical environment.

# Reproducibility strategy
Reproducibility is treated as a core design principle rather than a post hoc objective. The project maintains three complementary environment specifications.
* `environment.yml` defines the intended Conda environment.
* `environment.lock.yml` records the exact Conda environment exported after installation.
* `requirements.txt` preserves the exact versions of packages installed through pip.
Software versions are frozen before biological analyses begin to ensure that computational results remain reproducible throughout the lifetime of the project.

# Data sources
## Primary discovery cohort: Peng J. *et al.* (2019)
Dataset ID: DS-001
Dataset: Peng et al. (2019)
Title: Single-cell RNA-seq highlights intra-tumoral heterogeneity and malignant progression in pancreatic ductal adenocarcinoma
Authors: Junya Peng, Bao-Fa Sun, Chuan-Yuan Chen, Jia-Yi Zhou, Yu-Sheng Chen, Hao Chen, Lulu Liu, Dan Huang, Jialin Jiang, Guan-Shen Cui, Ying Yang, Wenze Wang, Dan Guo, Menghua Dai, Junchao Guo, Taiping Zhang, Quan Liao, Yi Liu, Yong-Liang Zhao, Da-Li Han, Yupei Zhao, Yun-Gui Yang, Wenming Wu
Publication: Cell Research, 2019, 29(9), 725–738. https://doi.org/10.1038/s41422-019-0195-y
DOI: 10.1038/s41422-019-0195-y
Organization: Beijing Institute of Genomics, Chinese Academy of Sciences
Repository: Genome Sequence Archive (GSA), National Genomics Data Center (NGDC)
Repository URL: https://ngdc.cncb.ac.cn/gsa/
Dataset URL: https://ngdc.cncb.ac.cn/gsa/browse/CRA001160
BioProject: PRJCA001063
Accession: CRA001160 (GSA)
Release date: 2019-07-09
Date accessed: 2026-07-18
Organisms: Homo sapiens
Disease: Pancreatic ductal adenocarcinoma (PDAC)
Data Type: Transcriptome or Gene expression
Sample Scope: Single-cell 
Relevance: Medical
Tissue: Primary pancreatic tumor and matched normal pancreatic tissue
Experimental Design: Single-cell RNA sequencing of PDAC tumor and normal pancreatic samples to characterize tumor heterogeneity, the tumor microenvironment, and determine the transcriptomes of over 50,000 individual pancreatic cells. 
Number of Patients: 24 patients with PDAC tumors (primary); 11 normal pancreas(control)
Number of Experiments: 35
Number of Runs: 35
Biosample: 35
Number of FASTQ Files: 70 
Data Format: Raw paired-end FASTQ files (.fastq.gz)
Platforms: Illumina HiSeq X Ten
Single-cell technology: inDrop
Download Methods:  HTTPS, FTP, Aspera, QTrans
Metadata File: CRA001160.xlsx
Total Download Size, Repository Size: 2694.29 GB
License / Accessibility: Publicly available at https://ngdc.cncb.ac.cn/gsa/browse/CRA001160

## Secondary validation cohort

Elyada E. *et al.* (2019)
Tumor microenvironment single-cell RNA sequencing dataset, used for validation analyses.
Accession: GSE129455

# Development workflow
Development follows milestone-based project management.
Major milestones include:
* MD-1 — Software and environment initialization
* MD-2 — Data acquisition
* MD-3 — Expression matrix generation
* MD-4 — Quality control and preprocessing
* MD-5 — Malignant cell identification
* MD-6 — Fate inference
* MD-7 — FSAI computation
* MD-8 — Downstream biological analysis
* MD-9 — Validation and manuscript preparation
Each milestone is independently documented before subsequent work begins.

# Repository status
Current branch:
`main`
Repository status: Active development.

**NOTE**: Scientific analyses have not yet begun.
Current emphasis is on establishing a fully reproducible computational foundation before dataset processing.

# Current milestone
MD-2 — Dataset acquisition and preprocessing.
Completed
✓ Computational environment
✓ Reproducible repository
✓ Documentation framework
✓ Dataset provenance audit
In progress
• Acquisition of Peng et al. (2019)
• Generation of expression matrices

# License

This repository is distributed under the MIT License.

See the `LICENSE` file for complete licensing information.

# Citation

Formal citation information will be provided following the first public software release.

A `CITATION.cff` file will be added once the project reaches a stable release suitable for citation.

# Acknowledgements

MaligPx builds upon numerous open-source scientific software projects that make modern single-cell computational biology possible, including Scanpy, AnnData, scVelo, CellRank, NumPy, SciPy, Pandas, Matplotlib, NetworkX, Leidenalg, and the broader Python scientific computing ecosystem. The project also relies on publicly available datasets generated by Peng et al. (2019) and Elyada et al. (2019), whose contributions provide the biological foundation for the development and evaluation of the framework.
