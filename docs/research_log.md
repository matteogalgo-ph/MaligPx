# MaligPx Research Log
## Purpose

This document serves as the official scientific laboratory record for the MaligPx project. It documents the chronological progression of scientific work, including the rationale for each milestone, the procedures performed, the observations obtained, the conclusions drawn, and the resulting direction of subsequent research. Unlike C:\MaligPx\docs\engineering_log.md, which records software implementation details, and C:\MaligPx\docs\project_log.md, which provides a high-level overview of project progress, this document focuses exclusively on the scientific development of the project and the reproducible computational workflow used to investigate pancreatic ductal adenocarcinoma (PDAC) through single-cell transcriptomics.

All milestones are assigned permanent identifiers to maintain traceability throughout the lifetime of the project. Architectural decisions are cross-referenced with C:\MaligPx\docs\decisions.md, while datasets and external resources are documented in C:\MaligPx\docs\dataset_manifest.md. Engineering implementation details that are not directly relevant to scientific methodology are recorded separately in C:\MaligPx\docs\engineering_log.md.

# MD-1 — Computational Infrastructure Initialization
## Objective

Establish a stable, reproducible, and version-controlled computational infrastructure capable of supporting large-scale single-cell transcriptomic analysis, RNA velocity analysis, lineage inference, and future development of the MaligPx Fate-State Artificial Intelligence (FSAI) framework.

## Scientific Rationale

Reproducibility is a fundamental requirement of computational biology. Biological conclusions cannot be considered scientifically valid unless every computational step—from software installation through downstream analysis—can be reproduced under an identical software environment. Consequently, no biological datasets would be downloaded or analyzed until the computational infrastructure had been completely established, documented, and version-controlled. This principle was later formalized through Decision DEC-007.

# MD-1-001: Established Version Control and Project Identity

A dedicated GitHub account was created using the institutional project email address to serve as the permanent public repository for MaligPx. Git was installed and configured to provide distributed version control for all source code, documentation, computational workflows, and project metadata. Repository version control was adopted before scientific work commenced to ensure that every subsequent modification could be traced to a permanent revision history.

## Outcome

A version-controlled foundation was established for all future scientific and software development.

# MD-1-002: Established the Computational Distribution

Miniforge was selected as the canonical Python distribution for the project and installed in C:\Miniforge. Immediately following installation, the base Conda installation was updated from the public conda-forge repositories to ensure that package resolution began from the most recent stable state. Mamba was subsequently installed as the project's primary dependency solver because of its substantially improved performance and reliability when resolving complex scientific software environments.

This milestone established the software distribution that would remain the computational foundation of MaligPx throughout development and directly resulted in Decision DEC-001.

## Deliverables

Miniforge installation (C:\Miniforge)
Updated Conda installation
Mamba package manager
Decision DEC-001

## Outcome

The computational package management infrastructure was successfully established.

# MD-1-003: Established the Primary Scientific Environment

A dedicated Conda environment named maligpx was created using Python 3.10. The environment was intentionally isolated from the base Conda installation to eliminate dependency contamination and ensure that all project software could be reproduced independently of the operating system.

Python 3.10 was selected because it provided the broadest compatibility across the modern single-cell computational biology ecosystem while minimizing dependency conflicts among Scanpy, AnnData, scVelo, CellRank, and associated scientific libraries.

This milestone established the official project environment and resulted in Decision DEC-002.

## Deliverables

Conda environment maligpx
Python 3.10 environment specification
Decision DEC-002

## Outcome

A reproducible scientific computing environment was successfully established.

# MD-1-004: Resolved Environment Execution Failure

Following creation of the project environment, Windows prevented execution of C:\Miniforge\envs\maligpx\python.exe, reporting that execution had been blocked by a Device Guard policy despite the project being developed on a personal Windows 11 Home workstation.

Systematic diagnostics demonstrated that the Conda installation itself remained functional because the base interpreter executed correctly while only the environment interpreter was blocked. Investigation isolated Windows Smart App Control as the probable cause of the restriction. After Smart App Control was disabled and the operating system restarted, the project environment executed normally without modification of either Conda or the project environment.

The incident confirmed that the failure originated from operating system security enforcement rather than corruption of the computational environment.

## Outcome

The computational environment became fully operational without requiring reconstruction of the Conda installation or project environment.

# MD-1-005: Established the Scientific Software Stack

The core computational biology ecosystem required for MaligPx was installed using a Conda-first strategy. Primary scientific packages included Scanpy, AnnData, NumPy, SciPy, Pandas, Matplotlib, scVelo, NetworkX, igraph, Leidenalg, Scikit-learn, Statsmodels, JupyterLab, Black, Ruff, and isort.

Installation of CellRank through conda-forge was investigated but proved unsatisfiable on Windows because the dependency graph required pygpcca, which in turn depends on PETSc. Compatible PETSc packages were unavailable through conda-forge for the Windows platform, preventing successful dependency resolution.

Following investigation, CellRank was installed through pip, and successful installation was verified by importing the package and confirming the installed version. This implementation strategy was formalized through Decision DEC-004 and preserved the Conda-first philosophy established by Decision DEC-003 while permitting carefully documented exceptions when required by upstream package availability.

## Deliverables

Core scientific software ecosystem
CellRank 2.0.7
Decision DEC-003
Decision DEC-004

## Outcome

The computational biology software stack required for downstream single-cell transcriptomic analysis was successfully established.

# MD-1-006: Verified the Computational Environment

Following installation of the scientific software ecosystem, a comprehensive verification procedure was performed to confirm that the computational environment was capable of executing the software stack required by MaligPx. An environment verification script, C:\MaligPx\tests\environment_test.py, was developed to import each critical scientific package and detect installation failures before biological data acquisition commenced.

Successful execution of the verification script confirmed that Scanpy, AnnData, scVelo, CellRank, NumPy, SciPy, Pandas, Matplotlib, Leidenalg, igraph, and the remaining core dependencies could all be imported successfully within the maligpx Conda environment. Verification at this stage eliminated uncertainty regarding dependency conflicts prior to beginning computational biology workflows.

To preserve the computational state, the active Conda environment was exported to C:\MaligPx\environment.yml, and an inventory of Python packages installed through pip was exported to C:\MaligPx\requirements.txt. During export, Conda reported the expected CondaExportWarning, indicating that several packages had been installed through pip. Investigation confirmed that the warning resulted from the intentional installation strategy adopted for CellRank and did not represent an error or compromise reproducibility.

## Deliverables

C:\MaligPx\tests\environment_test.py
C:\MaligPx\environment.yml
C:\MaligPx\requirements.txt

## Related Decisions

DEC-003
DEC-004

## Outcome

The computational environment was verified to be operational and reproducible.

# MD-1-007: Established the Standardized Project Architecture

Following verification of the software environment, the permanent project repository was established at C:\MaligPx. A standardized directory hierarchy was created before any biological datasets were downloaded to ensure that all future analyses, intermediate files, documentation, figures, software components, and research outputs would be organized according to a consistent and reproducible structure.

The following primary directories were established:

C:\MaligPx\configs\
C:\MaligPx\data\
C:\MaligPx\docs\
C:\MaligPx\figures\
C:\MaligPx\logs\
C:\MaligPx\notebooks\
C:\MaligPx\references\
C:\MaligPx\results\
C:\MaligPx\scripts\
C:\MaligPx\src\
C:\MaligPx\tests\

In addition, the foundational repository files required for reproducibility and collaborative development were created, including:

C:\MaligPx\.gitignore
C:\MaligPx\.gitattributes
C:\MaligPx\environment.yml
C:\MaligPx\requirements.txt

A dedicated documentation framework was also established within C:\MaligPx\docs\ through creation of:

project_log.md
engineering_log.md
research_log.md
decisions.md

This repository architecture standardized the separation of computational code, datasets, scientific documentation, engineering records, analytical outputs, and supporting reference material. The organizational strategy adopted during this milestone was subsequently formalized through Decision DEC-005 and Decision DEC-006.

## Deliverables

Standardized project directory hierarchy
Documentation framework
Reproducibility specification files

## Related Decisions

DEC-005
DEC-006

## Outcome

The permanent repository architecture for MaligPx was successfully established.

# MD-1-008: Established Version-Controlled Development

Following construction of the repository architecture, Git version control was initialized within C:\MaligPx. The initial repository commit established the baseline from which all future scientific analyses, software development, documentation revisions, and methodological decisions would be tracked.

Subsequent commits refined the repository structure and incorporated the documentation framework, ensuring that the computational environment, repository architecture, and supporting documentation were permanently preserved within the project's revision history.

The repository was then published to GitHub, creating the canonical remote repository for MaligPx and enabling synchronized development between the local workstation and the public repository.

The repository adopted the MIT License to provide an explicit open-source licensing framework for future software releases while maintaining transparency and reproducibility.

## Deliverables

Git repository initialization
Initial commit history
Remote GitHub repository
MIT License

## Outcome

Version-controlled scientific development was successfully established.

# MD-1-009: Installed the Native Compilation Toolchain

Installation of Scrublet required compilation of native C++ extensions because compatible precompiled Windows wheels were unavailable for one or more dependencies. To satisfy these requirements, Microsoft Visual Studio 2022 Build Tools were installed with the Desktop Development with C++ workload.

The installation included the Microsoft Visual C++ compiler, the Windows Software Development Kit, and CMake support. Successful installation was verified by confirming availability of the Microsoft C/C++ compiler through the Developer Command Prompt.

Establishing the native compilation toolchain ensured compatibility with future scientific Python packages requiring compilation from source.

## Deliverables

Microsoft Visual Studio 2022 Build Tools
MSVC v143 compiler
Windows SDK
CMake toolchain

## Outcome

Native compilation capability was successfully established.

# MD-1-010: Installed Scrublet for Doublet Detection

Scrublet was evaluated for incorporation into the MaligPx preprocessing workflow because doublet detection constitutes an important quality-control procedure in single-cell RNA sequencing analysis.

Initial attempts to install Scrublet through conda-forge were unsuccessful because no compatible Windows package was available. Installation through pip likewise failed initially because the Annoy dependency required native compilation.

Following installation of the Microsoft Visual Studio Build Tools during the preceding milestone, Scrublet installation was repeated successfully. Pip compiled the required native components, installed Scrublet together with its dependencies, and integration into the project environment was verified through successful package import.

The completed software stack now contained all principal packages required for quality control, transcriptomic analysis, RNA velocity analysis, lineage inference, and future development of the MaligPx Fate-State Artificial Intelligence framework.

## Deliverables

Scrublet 0.2.3
Annoy
Supporting image-processing dependencies

## Outcome

Doublet detection capability was successfully incorporated into the computational workflow.

# MD-1-011: Finalized the Reproducibility Specification

After completion of the scientific software installation, the computational environment was frozen to preserve an exact record of the software state supporting future analyses.

A complete Conda environment export was generated as C:\MaligPx\environment.lock.yml. The expected CondaExportWarning regarding pip-installed packages was recorded and investigated. The warning was determined to be consistent with the installation strategy documented under Decisions DEC-003 and DEC-004 and therefore required no corrective action.

Together with environment.yml and requirements.txt, the lock file completed the reproducibility specification for the MaligPx computational infrastructure.

## Deliverables

C:\MaligPx\environment.lock.yml

## Outcome

The computational environment was frozen and documented prior to biological data acquisition.

# MD-1 Summary

The objective of MD-1 was to establish a fully reproducible computational infrastructure before initiating scientific analysis. This objective was achieved through installation of the software environment, verification of the scientific software stack, establishment of the project repository architecture, implementation of version control, creation of the documentation framework, installation of the native compilation toolchain, incorporation of all required computational biology packages, and preservation of the complete software environment through reproducibility specifications.

At the conclusion of MD-1, MaligPx possessed a validated computational infrastructure capable of supporting large-scale single-cell transcriptomic analysis. Consistent with Decision DEC-007, no biological datasets had yet been downloaded or analyzed. The project was therefore prepared to proceed to MD-2, during which dataset acquisition, provenance verification, and preparation of the preprocessing pipeline would begin.

# MD-2 — Dataset Acquisition and Preprocessing Preparation
## Objective

Establish a scientifically reproducible framework for biological dataset acquisition, provenance documentation, storage organization, repository auditing, and computational preprocessing before downloading or processing any sequencing data.

## Scientific Rationale

Unlike many published single-cell studies that begin from processed count matrices, MaligPx is designed to reconstruct gene-expression matrices directly from raw sequencing reads whenever feasible. This strategy maximizes transparency, preserves complete control over preprocessing parameters, enables generation of spliced and unspliced count matrices required for RNA velocity analysis, and ensures that every analytical result can be reproduced from the original sequencing data. Consequently, repository verification, documentation, and storage preparation were completed before any biological files were downloaded. This philosophy was subsequently formalized through Decision DEC-008.

# MD-2-001: Established High-Speed Dataset Acquisition Capability

Because the primary discovery dataset exceeds 2.6 TB in size, conventional browser-based downloads were determined to be impractical due to transfer speed limitations and increased susceptibility to interrupted downloads. The official Genome Sequence Archive (GSA) documentation recommends Aspera FASP for transferring large sequencing datasets, making installation of IBM Aspera Connect a prerequisite for efficient data acquisition.

IBM Aspera Connect (Windows x64) was downloaded and installed together with the browser integration required for initiating transfers directly from the GSA repository. Installation was verified using the IBM Aspera Connect Diagnostic Tool, which confirmed successful operation of the desktop client and readiness to perform high-throughput FASP transfers.

Alternative download methods available through the repository, including HTTPS, FTP, and QTrans, were also evaluated and documented for redundancy. Although these methods remain available, Aspera was designated as the preferred acquisition mechanism because of its superior transfer performance for terabyte-scale datasets.

## Observations

The installation completed without errors. Diagnostic testing confirmed that the Aspera client could communicate successfully with the local operating system and was correctly configured for future transfers.

## Deliverables

IBM Aspera Connect
Verified Aspera FASP client
High-speed dataset acquisition capability

## Outcome

The project infrastructure became capable of downloading multi-terabyte sequencing datasets through the recommended transfer protocol.

# MD-2-002: Established the Biological Data Management Architecture

Prior to downloading any biological data, a standardized directory hierarchy was constructed under C:\MaligPx\data\ to ensure that raw sequencing data, processed outputs, metadata, reference resources, and intermediate analytical products would remain physically separated throughout the lifetime of the project.

The following directories were established:

C:\MaligPx\data\
├── raw\
├── intermediate\
├── processed\
└── velocity\

Dataset-specific storage locations were then created for the primary discovery cohort and future validation cohorts.

For the Peng et al. (2019) dataset, dedicated directories were established for raw sequencing files, metadata, processed outputs, and supporting reference resources to ensure that every component of the dataset could be stored independently while maintaining a consistent directory structure. Equivalent placeholder directories were prepared for the Elyada et al. (2019) validation cohort to preserve identical organizational conventions throughout future analyses.

The directory hierarchy was intentionally established before any biological data were downloaded to eliminate ambiguity regarding storage locations and to prevent later restructuring of acquired datasets.

## Observations

No biological files were placed within the directory hierarchy during this milestone. The directory structure served exclusively as the permanent organizational framework supporting future dataset acquisition.

## Deliverables

The complete biological data management hierarchy rooted at:

C:\MaligPx\data\

## Outcome

A standardized and reproducible data storage architecture was successfully established prior to biological data acquisition.

# MD-2-003: Established the Dataset Documentation Framework

Comprehensive dataset documentation was created before repository auditing commenced to ensure that provenance information, metadata, acquisition history, sample inventories, and future integrity verification could be recorded continuously throughout the project rather than reconstructed retrospectively.

The following permanent documentation files were created within C:\MaligPx\docs\:

dataset_manifest.md
data_dictionary.md
acquisition_log.md

dataset_manifest.md was designated as the authoritative inventory of every biological dataset incorporated into MaligPx. The document records repository provenance, accession identifiers, publication metadata, download status, intended analytical role, storage locations, repository URLs, release dates, and future integrity verification status.

data_dictionary.md was established as the permanent inventory of all biological samples included within the project. The document will ultimately record every sequencing run, sample identifier, patient identifier, tissue source, sequencing files, processing status, and downstream analytical status. Because biological datasets had not yet been downloaded, the table intentionally remained empty apart from the predefined schema.

acquisition_log.md was established to provide a chronological record of every dataset acquisition event performed during the project. Each future download will record acquisition date, repository source, transfer protocol, verification procedure, checksum validation, download outcome, and subsequent storage location.

Creation of these documents before repository auditing ensured that all future acquisition events would be documented contemporaneously, thereby strengthening reproducibility and reducing the likelihood of incomplete provenance records.

## Observations

Documentation templates were intentionally created before the first biological download to eliminate retrospective reconstruction of acquisition history.

## Deliverables

Created:

C:\MaligPx\docs\dataset_manifest.md
C:\MaligPx\docs\data_dictionary.md
C:\MaligPx\docs\acquisition_log.md

## Outcome

The permanent documentation framework supporting biological dataset acquisition was successfully established.

# MD-2-004: Audited the Peng et al. (2019) Primary Discovery Dataset

With the computational infrastructure and documentation framework established, a comprehensive audit of the primary discovery dataset was conducted before initiating download. The objective of this audit was to verify dataset provenance, determine the availability of raw and processed sequencing data, assess repository completeness, identify any revisions affecting reproducibility, and confirm that the dataset satisfied the scientific requirements of MaligPx.

The canonical repository was confirmed to be the Genome Sequence Archive (GSA) hosted by the National Genomics Data Center under accession CRA001160, corresponding to BioProject PRJCA001063. The repository was released publicly on 2019-07-09 and contains the sequencing data supporting the publication Single-cell RNA-seq highlights intra-tumoral heterogeneity and malignant progression in pancreatic ductal adenocarcinoma published in Cell Research.

Repository inspection confirmed that the dataset contains 35 sequencing experiments, 35 sequencing runs, 35 biosamples, and 70 compressed paired-end FASTQ files, generated using the Illumina HiSeq X Ten platform with the inDrop single-cell RNA sequencing protocol. The cohort comprises 24 primary PDAC tumour samples and 11 matched normal pancreatic samples, representing the complete discovery cohort described in the publication.

Critically, the audit determined that the repository distributes raw sequencing reads only. Processed gene-expression count matrices are not provided through the GSA archive. This observation directly informed the computational strategy adopted by MaligPx and provided the scientific justification for Decision DEC-008, which establishes reconstruction of expression matrices from raw FASTQ files as the official preprocessing workflow.

Repository examination further identified that eight sequencing runs originally released in 2019 were superseded by replacement run accessions on 2021-01-14. These replacement accessions were recorded within C:\MaligPx\docs\dataset_manifest.md to ensure that all future downloads reference the current repository contents rather than obsolete sequencing runs.

The repository metadata file CRA001160.xlsx was identified as the authoritative source of experiment-level metadata and scheduled for acquisition before downloading the sequencing reads themselves.

Repository statistics indicated an expected download size of approximately 2.69 TB, confirming that acquisition would require staged downloading together with subsequent checksum verification because of the volume of sequencing data involved.

## Observations

The repository is publicly accessible without controlled-access restrictions.

The repository contains raw sequencing data but does not distribute processed count matrices.

Eight sequencing runs have been replaced since the original publication and must be downloaded using their updated accession identifiers.

The dataset size requires high-throughput transfer methods and careful integrity verification.

## Deliverables

Updated:

C:\MaligPx\docs\dataset_manifest.md

Referenced:

CRA001160
PRJCA001063
CRA001160.xlsx

## Related Decisions

DEC-008

## Outcome

The Peng et al. (2019) repository was verified as the official primary discovery cohort for MaligPx, and all prerequisite information required to begin data acquisition was successfully documented.

# MD-2-005: Standardized the Repository for Reproducible Scientific Development

Following completion of the repository audit, the focus shifted from dataset evaluation to ensuring that the project repository itself satisfied contemporary standards for reproducible computational biology. Although the computational infrastructure established during MD-1 was already operational, several repository-level improvements were identified that would strengthen long-term maintainability, scientific transparency, and external reproducibility before biological analyses commenced.

The computational environment specification was reviewed in its entirety. The project environment definition stored in C:\MaligPx\environment.yml was regenerated to reflect the finalized software environment following installation of Scrublet and the remaining scientific dependencies. In parallel, a complete Conda environment export was generated as C:\MaligPx\environment.lock.yml to preserve an exact snapshot of the Conda environment at the conclusion of infrastructure development. Because CellRank, Scrublet, and several supporting libraries are intentionally installed through pip on Windows owing to upstream packaging constraints, Conda reported the expected CondaExportWarning indicating the presence of third-party Python packages. The warning was investigated and determined to be fully consistent with Decisions DEC-003 and DEC-004. To eliminate ambiguity for future users, explanatory documentation describing the warning and the role of requirements.txt was incorporated directly into environment.yml.

Following regeneration of the Conda specifications, C:\MaligPx\requirements.txt was regenerated using pip freeze to preserve the exact versions of all pip-installed packages. Together, environment.yml, environment.lock.yml, and requirements.txt now constitute the complete software reproducibility specification for MaligPx.

Repository documentation was subsequently reviewed to ensure that project metadata accurately reflected the current state of development. The project README was rewritten to describe the scientific objectives of MaligPx, summarize the computational workflow, document repository organization, specify software requirements, identify the primary discovery dataset, reference the principal project documentation, and provide guidance for reproducing the computational environment. The repository documentation was further expanded through updates to C:\MaligPx\docs\dataset_manifest.md, C:\MaligPx\docs\data_dictionary.md, C:\MaligPx\docs\acquisition_log.md, C:\MaligPx\docs\decisions.md, C:\MaligPx\docs\project_log.md, and this research log to ensure internal consistency across all project records.

The project repository was also reviewed for licensing and public accessibility. An MIT License was added to the GitHub repository, explicitly defining the terms under which the software may be used, modified, and redistributed. Adoption of an explicit open-source license improves scientific transparency and facilitates future reuse of the computational framework by other researchers.

Upon completion of the documentation review, all modifications were committed to the local Git repository. During synchronization with GitHub, the initial push was rejected because the remote repository contained commits that were not present in the local repository. The remote changes were incorporated through a Git pull, the merge was completed successfully without conflicts, and the repository was subsequently synchronized with GitHub through a successful push. Completion of this synchronization established identical project histories between the local working copy and the public repository before biological datasets were introduced into the workflow.

## Observations

The regenerated software specifications accurately represent the finalized computational environment supporting MaligPx.

The expected Conda export warning remained consistent with the project's documented package management strategy and required no corrective action.

Repository synchronization identified minor divergence between the local and remote repositories. The divergence was resolved through a standard Git merge procedure without introducing conflicts.

At the conclusion of this milestone, the public GitHub repository accurately reflected the complete computational infrastructure and documentation framework developed during MD-1 and MD-2.

## Deliverables

Updated:

C:\MaligPx\README.md
C:\MaligPx\environment.yml
C:\MaligPx\environment.lock.yml
C:\MaligPx\requirements.txt
C:\MaligPx\docs\dataset_manifest.md
C:\MaligPx\docs\data_dictionary.md
C:\MaligPx\docs\acquisition_log.md
C:\MaligPx\docs\decisions.md
C:\MaligPx\docs\project_log.md
C:\MaligPx\docs\research_log.md

## Verified:

C:\MaligPx\LICENSE

Repository synchronized with the canonical GitHub repository.

## Related Decisions

DEC-001
DEC-002
DEC-003
DEC-004
DEC-005
DEC-006
DEC-007
DEC-008

## Outcome

The MaligPx repository was brought into a fully reproducible, internally consistent, and publicly synchronized state immediately before biological data acquisition.

# MD-2 Summary

The objective of MD-2 was to prepare the project for reproducible biological data acquisition while ensuring complete traceability of datasets, computational infrastructure, and repository metadata. This objective was achieved through installation of high-throughput data transfer software, establishment of a standardized biological data hierarchy, creation of a comprehensive dataset documentation framework, verification of the provenance and completeness of the Peng et al. (2019) primary discovery dataset, formal adoption of raw FASTQ processing as the official computational strategy through Decision DEC-008, regeneration of the reproducibility specifications describing the finalized computational environment, comprehensive review of repository documentation, verification of open-source licensing, and synchronization of the complete project with its public GitHub repository.

At the conclusion of MD-2, no biological sequencing data had yet been downloaded. This condition was intentional and reflects the project's guiding philosophy that computational reproducibility, dataset provenance, and documentation must be fully established before scientific analysis begins. The project now possesses a validated computational environment, a standardized repository architecture, complete provenance documentation, and an audited primary discovery cohort suitable for downstream preprocessing.

The next phase of development will begin with acquisition of the Peng et al. (2019) metadata package (CRA001160.xlsx), followed by staged acquisition of the raw paired-end FASTQ files comprising accession CRA001160. After download completion, file integrity will be verified through checksum validation before reconstruction of gene-expression count matrices, quality-control analysis, and subsequent integration into the Scanpy, scVelo, and CellRank workflow.

Current Scientific State of the Project

As of the completion of MD-2, the MaligPx project has successfully transitioned from computational infrastructure development to the threshold of biological data acquisition. The software environment has been fully established, verified, frozen, and documented through C:\MaligPx\environment.yml, C:\MaligPx\environment.lock.yml, and C:\MaligPx\requirements.txt. The repository architecture has been standardized and synchronized with the public GitHub repository, ensuring that future scientific development will proceed from a version-controlled and reproducible baseline.

The primary discovery dataset has been identified as Peng et al. (2019), archived under Genome Sequence Archive accession CRA001160 (BioProject PRJCA001063). Repository provenance, publication metadata, accession information, sequencing platform, experimental design, sample composition, download methods, replacement run accessions, and expected storage requirements have all been verified and documented within C:\MaligPx\docs\dataset_manifest.md.

Inspection of the repository confirmed that processed expression matrices are not distributed through the public archive. Consequently, the official computational strategy of MaligPx is to reconstruct gene-expression count matrices directly from raw paired-end FASTQ files following download and integrity verification. This strategy has been permanently adopted through Decision DEC-008 and will form the basis of every downstream biological analysis.

No biological sequencing data have yet been downloaded, processed, or analyzed. This condition is intentional and reflects the project's guiding principle that computational reproducibility, dataset provenance, repository organization, and methodological documentation must be fully established before scientific analyses begin.

# Scientific Readiness Assessment

The following components have been completed and verified:

Component	                               Status
Computational infrastructure	               Complete
Scientific software stack	               Complete
Conda environment verification	               Complete
Environment reproducibility specification      Complete
Native compilation toolchain	               Complete
Version control	                               Complete
Public GitHub synchronization	               Complete
Repository licensing	                       Complete
Project documentation framework	               Complete
Dataset provenance documentation	       Complete
Primary dataset audit	                       Complete
Biological data acquisition	               Pending
Metadata download	                       Pending
FASTQ acquisition	                       Pending
Checksum verification	                       Pending
Count matrix reconstruction	               Pending
Scanpy preprocessing	                       Pending
RNA velocity preprocessing	               Pending
CellRank analysis	                       Pending

# Outstanding Scientific Risks

Several technical considerations have been identified prior to initiating biological analysis.

The Peng et al. (2019) repository distributes approximately 2.69 TB of compressed sequencing data. Acquisition will therefore require staged downloading to avoid storage exhaustion and to permit verification of each transfer before subsequent downloads commence.

The repository distributes raw sequencing reads only. Expression matrices, spliced count matrices, and unspliced count matrices must therefore be reconstructed internally before Scanpy preprocessing can begin.

Because the sequencing data were generated using the inDrop platform, preprocessing parameters must be selected specifically for inDrop chemistry rather than assuming defaults intended for Chromium datasets. Appropriate barcode handling and reference generation will therefore be investigated before implementation of the alignment workflow.

Integrity verification through cryptographic checksum validation will be completed immediately following acquisition of every downloaded file before any computational preprocessing is performed.

# Immediate Next Milestone

The next milestone, MD-3, will begin biological data acquisition.

The planned sequence of work is as follows:

Download the metadata package (CRA001160.xlsx) into C:\MaligPx\data\raw\peng2019\metadata\.
Verify that metadata agree with the repository audit recorded in C:\MaligPx\docs\dataset_manifest.md.
Download the seventy paired-end FASTQ files into C:\MaligPx\data\raw\peng2019\fastq\, using the replacement run accessions released by the Genome Sequence Archive on 2021-01-14 where applicable.
Record every download event in C:\MaligPx\docs\acquisition_log.md.
Generate cryptographic checksums for every downloaded file and store the verification results in C:\MaligPx\docs\checksums.md.
Confirm that every sequencing run expected from the repository audit has been successfully acquired before beginning computational preprocessing.
Select and validate the preprocessing workflow capable of reconstructing gene-expression count matrices from the inDrop sequencing data.
Generate AnnData-compatible count matrices for downstream quality-control analysis.
Begin the Scanpy preprocessing pipeline described in the project methodology.
Phase Completion Statement

MD-1 and MD-2 collectively established the complete computational and documentary foundation of MaligPx. The project now possesses a validated software environment, a reproducible repository architecture, comprehensive documentation, a permanently recorded decision history, verified dataset provenance, and a publicly synchronized version-controlled codebase. All prerequisites identified during project planning have been satisfied. The next phase of development will transition from infrastructure preparation to the acquisition and reconstruction of biological sequencing data, marking the beginning of experimental data generation within the MaligPx analytical pipeline.