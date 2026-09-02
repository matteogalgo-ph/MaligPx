# **MaligPx Decision Log**



## **DEC-001**



Title: Adopt Miniforge as the project distribution.

Date: 2026-06-28



### Decision



Miniforge will serve as the canonical Python distribution for MaligPx.



### Rationale



Miniforge defaults to the conda-forge ecosystem, provides a smaller installation than Anaconda, avoids licensing concerns, and offers the best compatibility with the modern single-cell analysis ecosystem (Scanpy, scVelo, AnnData, etc.).



### Alternatives Considered

Anaconda

Miniconda



### Impact:

All future environment specifications assume Miniforge.



## **DEC-002**



Title: Fix the project environment.

Date: 2026-06-28



### Decision



The official project environment will be named maligpx and will use Python 3.10.



### Rationale



Python 3.10 provides stable compatibility across the required computational biology ecosystem while minimizing dependency conflicts.



### Impact:

Future development must target this environment unless compatibility requirements change.



## **DEC-003**



Title: Adopt a Conda-first package management strategy.

Date: 2026-06-28



#### Decision



Software packages will be installed through Mamba/Conda whenever possible. Pip will be used only when no viable Conda package exists.



### Rationale



Conda provides better dependency management for scientific computing libraries.



### Impact:

The environment remains maximally reproducible while retaining flexibility when required.



## **DEC-004**



Title: Install CellRank through pip.

Date: 2026-06-28



### Decision



CellRank will be installed using pip rather than conda-forge.



### Rationale



Current Windows conda-forge builds are unsatisfiable because CellRank depends on pygpcca, which requires PETSc, and compatible Windows PETSc packages are unavailable through conda-forge.



### Alternatives Considered

Conda-forge installation

Building PETSc manually



### Impact:

requirements.txt becomes part of the project's reproducibility specification alongside environment.yml.



## **DEC-005**



Title: Standardize the repository architecture.

Date: 2026-06-28



### Decision



MaligPx will use a modular repository structure separating source code, notebooks, datasets, documentation, figures, logs, references, tests, and configuration files.



### Rationale



A modular architecture improves maintainability, reproducibility, and long-term scalability.



### Impact:

All future project development will follow this directory structure.



## **DEC-006**



Title: Separate engineering and scientific workflows.

Date: 2026-06-28



### Decision



Software engineering activities, scientific research, project milestones, and methodological decisions will be documented in independent logs.



### Rationale



Separating technical implementation from scientific reasoning simplifies auditing, debugging, manuscript preparation, and project management.



### Impact:

Engineering changes, research findings, and architectural decisions can be traced independently throughout the project lifecycle.



## **DEC-007**



Title: Freeze the computational infrastructure before scientific analysis.

Date: 2026-06-28



### Decision



No biological analyses or FSAI development will begin until the computational environment is fully reproducible and version-controlled.



### Rationale



Establishing a stable software baseline minimizes downstream debugging and ensures that future analytical results can be reproduced exactly.



### Impact:

Future work will begin with dataset acquisition and validation of the baseline Scanpy → scVelo → CellRank pipeline.



## **DEC-008**

Title: Generate expression matrices directly from raw sequencing reads.

Date: 2026-07-18



### Decision



The MaligPx project will reconstruct gene-expression count matrices directly from the raw FASTQ files released by Peng et al. (2019) rather than relying on externally processed count matrices.



### Rationale



Inspection of the CRA001160 archive confirmed that the public release contains only raw sequencing reads. Constructing expression matrices internally ensures complete control over preprocessing, alignment parameters, barcode correction, quality control, and downstream reproducibility.



Direct processing also enables future generation of spliced and unspliced count matrices for RNA velocity analysis without dependence on third-party preprocessing pipelines.



### Alternatives Considered



Use publicly available processed count matrices.



### Impact



The computational preprocessing stage becomes part of the official analytical pipeline and will precede all Scanpy quality-control procedures.



# **DEC-009**

Title: Phase 2 Dataset Provenance Corrections

Date: 2026-09-02



### Decision 

* The following corrections supersede conflicting statements in earlier

working documents:



1\. Peng et al. (2019)

&#x20;  Repository: Genome Sequence Archive (GSA)

&#x20;  Accession: CRA001160

&#x20;  BioProject: PRJCA001063

&#x20;  Sequencing chemistry: 10x Genomics Chromium Single Cell 3' v2



&#x20;  Previous inDrop-specific instructions in past dataset\_manifest.md versions are incorrect and must not be

&#x20;  used for FASTQ processing.



2\. Steele et al. (2020)

&#x20;  \*Added raw-data accession to dataset\_manifest.md: phs002071.v1.p1



### Rationale



To correct otherwise misleading information about the datasets used in MaligPx, and to add extra information for reference further on.



### Alternatives considered



Not applicable



### Impact



More specific and defensible details moving forward. Of course, it also enhances the accuracy of the study's logs.

