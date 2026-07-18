# MaligPx Project Log



## Purpose



This document provides a high-level chronological record of the development of the MaligPx project. Unlike the research log, which documents detailed scientific activities and methodological implementation, or the engineering log, which records software development and technical infrastructure, the project log summarizes major project milestones, their objectives, completion status, and their contribution to the overall progression of the project.



Each milestone represents a major phase of development. Detailed implementation records are maintained separately in the corresponding documentation files.



---



## Project Information



*\*Project Name:\*\* MaligPx



*\*Project Type:\*\* Computational Biology / Bioinformatics



*\*Research Domain:\*\* Single-cell Transcriptomics, Cancer Systems Biology, Machine Learning



*\*Primary Disease Focus:\*\* Pancreatic Ductal Adenocarcinoma (PDAC)



*\*Current Development Stage:\*\* MD-2 – Data Acquisition and Dataset Preparation



*\*Repository Status:\*\* Public GitHub repository established.



---



## Development Timeline



### MD-1 — Software and Computational Environment Initialization



*\*Status:\*\* Completed



The first project milestone established the computational foundation required for all subsequent biological analyses. The software environment was designed to maximize reproducibility while maintaining compatibility with the modern Python single-cell analysis ecosystem.



Major accomplishments included:



* Installation and configuration of Git.

* Installation of Miniforge as the canonical Python distribution.

* Creation of the `maligpx` Conda environment using Python 3.10.

* Installation and verification of the project's scientific software stack, including Scanpy, AnnData, scVelo, CellRank, Scrublet, NumPy, SciPy, Pandas, Matplotlib, NetworkX, igraph, Leidenalg, scikit-learn, and Statsmodels.

* Resolution of Windows Smart App Control restrictions that prevented execution of Conda environment interpreters.

* Installation of Microsoft Visual Studio Build Tools to support compilation of Python packages requiring native C/C++ extensions.

* Verification of successful package imports through an environment validation script.

* Generation of reproducibility artifacts, including `environment.yml`, `environment.lock.yml`, and `requirements.txt`.

* Construction of the standardized project directory structure rooted at `C:\\MaligPx`.

* Initialization of Git version control.

* Publication of the project's GitHub repository under the MIT License.



Completion of MD-1 established a fully operational computational environment suitable for reproducible scientific development.



---



### MD-2 — Data Acquisition and Dataset Preparation



*\*Status:\*\* In Progress



The second milestone focuses on establishing the data infrastructure required for the biological component of the project. Rather than immediately downloading sequencing data, emphasis has been placed on documenting data provenance, auditing repository contents, organizing local storage, and planning a reproducible acquisition workflow.



Completed activities include:



* Installation and verification of IBM Aspera Connect for high-speed data transfer.

* Construction of the standardized data directory hierarchy within `C:\\MaligPx\\data\\`.

* Creation of dedicated storage locations for raw sequencing data, intermediate processing outputs, processed datasets, and RNA velocity resources.

* Creation of project documentation supporting data provenance, including the dataset manifest, data dictionary, and acquisition log.

* Comprehensive audit of the Peng et al. (2019) Genome Sequence Archive repository (CRA001160), including verification of repository metadata, sequencing platform, experimental design, accession history, replacement runs, download methods, repository size, and public accessibility.

* Verification that the repository contains raw paired-end FASTQ files rather than processed expression matrices.

* Decision to reconstruct expression count matrices directly from raw sequencing reads as part of the official analytical workflow, thereby incorporating computational preprocessing into the reproducible methodology.

* Publication of the GitHub repository and synchronization of the local Git history with the remote repository.



Activities currently in progress include completion of the project documentation, acquisition planning, and preparation for downloading the biological datasets required for subsequent preprocessing.



---



## Milestone Status



| Milestone | Description                                                       | Status      |

| --------- | ----------------------------------------------------------------- | ----------- |

| MD-1      | Software and computational environment initialization             | Completed   |

| MD-2      | Data acquisition and dataset preparation                          | In Progress |

| MD-3      | Expression matrix generation from raw sequencing reads            | Pending     |

| MD-4      | Quality control and preprocessing                                 | Pending     |

| MD-5      | Malignant cell identification                                     | Pending     |

| MD-6      | Cell fate inference and trajectory modeling                       | Pending     |

| MD-7      | Fate State Ambiguity Index (FSAI) computation                     | Pending     |

| MD-8      | Biological validation and downstream analyses                     | Pending     |

| MD-9      | Final validation, software refinement, and manuscript preparation | Pending     |



---



## Current Project State



At the present stage of development, the computational infrastructure has been fully established and version-controlled, the software environment has been frozen to support reproducibility, the public repository has been created and synchronized with GitHub, and the primary discovery dataset has been identified and thoroughly audited. Data provenance documentation has been established before biological data acquisition, ensuring that every future dataset can be traced from its original repository through every stage of preprocessing and analysis.



No biological sequencing data have yet been downloaded, and no preprocessing or statistical analyses have been performed. This deliberate sequencing reflects the project's emphasis on reproducibility and software engineering discipline, ensuring that infrastructure and documentation are complete before computational analyses begin.



---



## Next Objectives



The immediate objectives are to complete the remaining MD-2 documentation, obtain the metadata associated with the Peng et al. (2019) dataset, finalize the acquisition strategy for raw sequencing data and reference resources, and prepare the computational preprocessing pipeline that will generate expression count matrices directly from the published FASTQ files. Completion of these tasks will conclude the data acquisition milestone and allow progression to MD-3, where biological data processing formally begins.



---



*\*Last Updated:\*\* 18 July 2026



*\*Current Milestone:\*\* MD-2 — Data Acquisition and Dataset Preparation



*\*Overall Project Status:\*\* Active Development



