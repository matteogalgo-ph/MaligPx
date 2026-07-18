MaligPx Research Log



Purpose



This document serves as the permanent scientific record of the MaligPx project. Every research activity, methodological development, computational milestone, dataset acquisition event, software validation, preprocessing decision, analytical procedure, and scientific observation shall be documented chronologically. Entries are intended to provide sufficient detail to enable an independent researcher to reconstruct the complete computational workflow without requiring external clarification. Engineering implementation details are recorded separately in C:\\MaligPx\\logs\\engineering\_log.md, project-wide milestones are summarized in C:\\MaligPx\\logs\\project\_log.md, and permanent architectural or methodological decisions are recorded in C:\\MaligPx\\docs\\decisions.md.



=====================================================================



MD-1: Software and Computational Infrastructure Initialization



Objective



Establish a fully reproducible computational environment capable of supporting the complete MaligPx analytical workflow before any biological datasets are acquired or processed. The environment shall support preprocessing of raw single-cell RNA sequencing data, quality control, clustering, trajectory inference, RNA velocity analysis, probabilistic cell-fate modeling, and future development of the Future State Artificial Intelligence (FSAI) framework.



=====================================================================



MD-1-001: Installed Git



Downloaded the current Git for Windows installer from the official Git website and completed installation using the standard Windows installation procedure.



Verified successful installation by opening Windows Terminal and executing



git --version



which returned the installed Git version without error, confirming that Git had been correctly added to the system PATH.



Git was selected as the project's version-control system because it provides complete revision history, facilitates reproducible software development, enables rollback of previous repository states, supports collaborative development, and integrates directly with GitHub for off-site version control and archival.



Git will serve as the authoritative record of all source-code modifications, documentation revisions, configuration updates, methodological changes, and computational analyses performed throughout the MaligPx project.



Status



Completed.



=====================================================================



MD-1-002: Installed Miniforge



Downloaded the latest Windows x64 installer for Miniforge from the official conda-forge distribution.



Installed Miniforge into



C:\\Miniforge



rather than the default user AppData location to establish a fixed installation path that simplifies documentation, troubleshooting, environment export, and long-term reproducibility.



Following installation, updated the base Conda installation by executing



conda update -n base -c conda-forge conda



This operation updated the core Conda package manager together with supporting security packages, including ca-certificates, certifi, and OpenSSL.



Installed Mamba into the base environment using



conda install -n base -c conda-forge mamba



Verified successful installation using



mamba --version



which reported the installed version without error.



Miniforge was selected over both Anaconda and Miniconda because it defaults to the community-maintained conda-forge repository, avoids Anaconda licensing restrictions, provides a substantially smaller installation footprint, and offers broader compatibility with contemporary computational biology software. Mamba was adopted because it provides significantly faster dependency resolution than the standard Conda solver while remaining fully compatible with Conda environments.



This installation established the package-management foundation upon which all subsequent software environments for MaligPx will be constructed.



Status



Completed.



=====================================================================



MD-1-003: Created Primary Project Environment



Created the canonical project environment by executing



mamba create -n maligpx python=3.10



The environment was intentionally named



maligpx



to provide a permanent, human-readable identifier that can be referenced consistently throughout project documentation, source code, publications, and reproducibility instructions.



Python 3.10 was selected following evaluation of compatibility across the modern single-cell computational biology ecosystem. At the time of environment creation, Python 3.10 provided stable support for Scanpy, AnnData, scVelo, CellRank, NumPy, SciPy, Pandas, and their associated scientific dependencies while minimizing dependency conflicts that were still present for newer interpreter versions.



Mamba resolved the complete dependency graph and successfully installed the required base packages into the isolated environment.



Activated the environment using



conda activate maligpx



Verified activation by confirming that subsequent Python and Conda commands executed within the newly created environment.



This isolated environment establishes a reproducible computational workspace independent of the operating-system Python installation and prevents conflicts with unrelated software.



Status



Completed.



=====================================================================



MD-1-004: Resolved Environment Execution Failure



Following successful creation of the maligpx environment, execution of



C:\\Miniforge\\envs\\maligpx\\python.exe



was unexpectedly blocked by Windows.



The operating system reported that execution had been prevented by a Device Guard policy despite the computer being a personal Windows 11 Home installation, where traditional enterprise Device Guard management is generally unavailable.



Initial troubleshooting confirmed that the Python interpreter within



C:\\Miniforge



executed normally while only the interpreter located within



C:\\Miniforge\\envs\\maligpx\\



was prevented from launching.



A systematic diagnostic procedure was performed to distinguish among possible causes, including Conda configuration errors, corrupted environment creation, antivirus interference, Windows security policies, and executable trust restrictions.



The investigation identified Windows Smart App Control as the most probable source of the restriction. Smart App Control was subsequently disabled, the system was restarted, and execution of the environment-specific Python interpreter was re-tested.



Following restart, the interpreter launched successfully without requiring modification of the Conda installation or recreation of the environment.



The issue was therefore attributed to Windows security enforcement rather than any defect within Miniforge, Conda, Mamba, or the project environment itself.



Resolving this issue before installing scientific software prevented unnecessary reinstallation of the computational stack and ensured that subsequent package installation occurred within a fully operational environment.



Status



Completed.



=====================================================================



MD-1-005: Installed Scientific Computing Ecosystem



Installed the core scientific software required for the MaligPx analytical workflow using Mamba and the conda-forge package repository.



The installed ecosystem included Scanpy, AnnData, NumPy, SciPy, Pandas, Matplotlib, JupyterLab, IPykernel, NetworkX, igraph, python-igraph, Leidenalg, Scikit-learn, Statsmodels, Black, Ruff, isort, and scVelo.



Each package was selected because it fulfills a specific role within the planned analytical pipeline. Scanpy provides preprocessing, normalization, clustering, dimensionality reduction, and visualization of single-cell transcriptomic data. AnnData supplies the standardized data structure used throughout the workflow. scVelo enables estimation of RNA velocity through analysis of spliced and unspliced transcript abundances. Leidenalg supports graph-based community detection for cell clustering. NumPy, SciPy, and Pandas provide the numerical and tabular computing foundation upon which higher-level analyses depend.



Attempted installation of CellRank through the conda-forge distribution using Mamba.



Dependency resolution failed because the available Windows build of CellRank depends upon pygpcca, which in turn requires PETSc. Compatible PETSc packages were not available for the Windows conda-forge ecosystem, preventing construction of a solvable dependency graph.



A detailed investigation confirmed that the failure originated from upstream package availability rather than corruption or misconfiguration of the local Conda environment.



CellRank was subsequently installed using



pip install cellrank



thereby bypassing the unavailable Conda dependency while preserving compatibility with the remainder of the environment.



Successful installation was verified by executing



python -c "import cellrank; print(cellrank.\_\_version\_\_)"



which returned CellRank version 2.0.7.



The decision to install CellRank through pip rather than Conda was later formalized as Decision DEC-004 within



C:\\MaligPx\\docs\\decisions.md



to ensure that future reconstruction of the computational environment follows the same methodology.



Status: Completed. 



=====================================================================



MD-1-006: Verified Computational Environment



Following installation of the complete scientific software ecosystem, a comprehensive verification procedure was performed to confirm that every critical dependency required by the MaligPx analytical pipeline could be successfully imported within the canonical project environment.



Created an environment verification script that sequentially imported the principal scientific libraries required throughout the project, including NumPy, SciPy, Pandas, Matplotlib, Scanpy, AnnData, scVelo, CellRank, NetworkX, igraph, Leidenalg, and supporting dependencies. The verification script was saved as



C:\\MaligPx\\scripts\\environment\_test.py



and executed from within the active



maligpx



Conda environment.



The verification procedure confirmed that all required packages imported successfully without runtime errors, unresolved dependencies, version conflicts, or missing shared libraries. Particular attention was given to CellRank because it had been installed through pip rather than Conda. Successful import confirmed that the mixed Conda/pip installation strategy adopted under Decision DEC-004 remained fully functional.



Following successful verification, the computational environment was exported to preserve its reproducible specification.



Executed



conda env export --no-builds > C:\\MaligPx\\environment.yml



to generate the portable Conda environment specification that defines the intended software environment for future reconstruction. The --no-builds option was intentionally selected because build identifiers frequently differ among operating systems while package versions remain functionally identical. Omitting build strings therefore improves portability without sacrificing reproducibility.



Executed



conda env export > C:\\MaligPx\\environment.lock.yml



to generate a fully resolved environment specification containing build identifiers and exact dependency versions. Unlike environment.yml, the lock file is intended to reproduce the precise software environment used during development whenever compatible platforms are available.



Executed



pip freeze > C:\\MaligPx\\requirements.txt



to capture every package installed through pip together with its exact version number.



During export, Conda generated a CondaExportWarning indicating that several installed packages originated from pip rather than Conda. The warning specifically identified CellRank, Scrublet, pygpcca, docrep, pygam, progressbar2, python-utils, wrapt, and their supporting dependencies.



This warning was anticipated and did not indicate corruption of the computational environment. Instead, it reflects a known limitation of Conda whereby packages installed through pip cannot be fully represented within Conda's dependency solver. Exact versions of all pip-installed packages were therefore preserved independently within



C:\\MaligPx\\requirements.txt



while Conda-managed packages remained documented within



C:\\MaligPx\\environment.yml



and



C:\\MaligPx\\environment.lock.yml



This dual-document strategy establishes complete reproducibility for both Conda-managed and pip-managed software while accurately documenting the unavoidable platform-specific limitations associated with CellRank and Scrublet installation on Windows.



Status



Completed.



=====================================================================



MD-1-007: Established Project Infrastructure



Created the canonical project repository at



C:\\MaligPx



to serve as the permanent root directory for all source code, datasets, documentation, analytical outputs, figures, notebooks, software configuration, reproducibility specifications, and project records.



The repository was intentionally organized according to a modular directory hierarchy that separates scientific data, computational code, documentation, engineering records, and analytical results into independent locations. This organization improves maintainability, simplifies navigation, minimizes accidental modification of critical resources, and aligns with widely accepted best practices for reproducible computational biology.



The following top-level directories were created:



C:\\MaligPx\\configs\\

Configuration files controlling software behavior, preprocessing parameters, analytical settings, and future pipeline configuration.



C:\\MaligPx\\data\\

Permanent storage location for all biological datasets, reference genomes, annotations, intermediate processing products, and analytical outputs directly related to sequencing data.



C:\\MaligPx\\docs\\

Permanent project documentation, methodological specifications, decision records, dataset manifests, and supporting documentation required for reproducibility.



C:\\MaligPx\\figures\\

Publication-quality figures, workflow diagrams, schematic illustrations, presentation graphics, and manuscript-ready visualizations.



C:\\MaligPx\\logs\\

Chronological project documentation including engineering activities, research milestones, and project summaries.



C:\\MaligPx\\notebooks\\

Interactive Jupyter notebooks used for exploratory analyses, validation experiments, visualization development, and methodological prototyping.



C:\\MaligPx\\references\\

Scientific publications, supplementary materials, protocols, reference manuals, software documentation, and supporting literature used throughout the project.



C:\\MaligPx\\results\\

Outputs generated by computational analyses, including processed datasets, statistical summaries, clustering results, trajectory inference, RNA velocity analyses, CellRank predictions, and future FSAI outputs.



C:\\MaligPx\\scripts\\

Standalone executable scripts responsible for environment validation, preprocessing, quality control, alignment, data integration, visualization, and automation of analytical workflows.



C:\\MaligPx\\src\\

Primary source code implementing reusable modules, helper functions, pipeline components, analytical algorithms, and future FSAI development.



C:\\MaligPx\\tests\\

Unit tests, validation scripts, regression tests, and software verification procedures used to ensure computational correctness throughout project development.



The repository root additionally received the foundational configuration and reproducibility files required by every subsequent phase of development.



Created



C:\\MaligPx\\.gitignore



to prevent temporary files, generated outputs, virtual environments, large biological datasets, operating-system artifacts, IDE configuration files, and other non-source resources from being committed into version control.



Created



C:\\MaligPx\\.gitattributes



to establish repository-wide file handling behavior and prepare the project for consistent cross-platform version control.



Created



C:\\MaligPx\\environment.yml



to define the intended Conda software environment.



Created



C:\\MaligPx\\environment.lock.yml



to preserve the fully resolved software environment.



Created



C:\\MaligPx\\requirements.txt



to document pip-managed package versions required for exact reconstruction of the computational environment.



Created



C:\\MaligPx\\README.md



to serve as the primary entry point describing project objectives, repository organization, computational requirements, installation instructions, analytical workflow, licensing, citation information, and future development roadmap.



Created



C:\\MaligPx\\LICENSE



through GitHub using the MIT License template. Adoption of the MIT License establishes explicit legal permission for reuse, modification, and redistribution of the project while preserving attribution to the original author.



Created



C:\\MaligPx\\docs\\decisions.md



to permanently record architectural, methodological, and computational decisions that influence project development.



Created



C:\\MaligPx\\logs\\project\_log.md



to summarize major project milestones throughout development.



Created



C:\\MaligPx\\logs\\research\_log.md



to serve as the authoritative chronological record of scientific progress.



Created



C:\\MaligPx\\logs\\engineering\_log.md



to document software implementation activities separately from scientific methodology.



This repository architecture constitutes the permanent organizational framework upon which every subsequent phase of the MaligPx project will be developed.



Status



Completed 



=====================================================================



MD-1-008: Initialized Version Control and Published the Repository



Initialized the MaligPx repository as a Git repository by navigating to



C:\\MaligPx



and executing



git init



This operation created the hidden



C:\\MaligPx\\.git\\



directory, establishing Git as the project's distributed version-control system and enabling complete tracking of all future modifications to source code, documentation, configuration files, and analytical resources.



Immediately after repository initialization, the repository status was verified using



git status



to confirm that Git correctly recognized the repository root and detected the initial project files awaiting version control.



The initial repository contents were staged using



git add .



and committed using



git commit



with the message



Initial commit



This first commit established the immutable baseline from which every subsequent revision of the project can be traced.



Following the initial commit, additional commits were created as project infrastructure matured, allowing major milestones to be isolated into logically coherent revisions. Rather than combining unrelated modifications into a single commit, repository history was intentionally organized into incremental commits that separately documented infrastructure development, documentation creation, computational environment refinement, and reproducibility updates. This commit strategy improves long-term traceability, simplifies debugging through selective rollback, and provides an auditable development history suitable for scientific software projects.



A new GitHub repository named



MaligPx



was subsequently created under the project's GitHub account.



The local repository was linked to the remote GitHub repository by configuring the remote origin using



git remote add origin <repository URL>



The configured remote was verified using



git remote -v



to ensure that both fetch and push URLs correctly referenced the intended GitHub repository.



The primary development branch was standardized as



main



and synchronized with GitHub using



git push -u origin main



Successful completion of the initial push confirmed that local and remote repositories had been correctly linked and established GitHub as the project's permanent off-site version-control host.



The repository was configured as publicly accessible to maximize scientific transparency, facilitate reproducibility, support future collaboration, and align with open-science principles commonly expected for computational biology research.



During repository publication, the official MIT License was added through GitHub, creating



C:\\MaligPx\\LICENSE



The MIT License was intentionally selected because it permits unrestricted academic and non-commercial reuse while requiring preservation of attribution to the original author. Adoption of an established open-source license removes legal ambiguity surrounding reuse of the project's software and documentation and aligns the repository with widely accepted scientific software practices.



Following synchronization with GitHub, subsequent development proceeded using the distributed Git workflow, with all major milestones committed locally before being pushed to the remote repository. This workflow establishes GitHub as the authoritative external archive of the project's complete development history while preserving the local repository as the active development environment.



Status



Completed.



=====================================================================



MD-1-009: Installed Microsoft Visual Studio 2022 Build Tools



During installation of additional scientific software, it became apparent that certain Python packages required native compilation because compatible precompiled Windows wheels were unavailable.



Downloaded Microsoft Visual Studio 2022 Build Tools from Microsoft's official distribution site and completed installation using the Visual Studio Installer.



Selected the Desktop Development with C++ workload together with its required components, including the Microsoft Visual C++ v143 compiler toolchain, the Windows Software Development Kit (SDK), and CMake support for Windows.



The installation provides a standards-compliant C/C++ compiler capable of compiling Python extension modules that cannot be installed directly from precompiled binary wheels.



Following installation, opened the Developer Command Prompt supplied by Visual Studio and verified successful installation by executing



cl



which returned the Microsoft C/C++ compiler version information, confirming that the native compilation toolchain had been correctly installed.



Although the Build Tools are not directly involved in biological analysis, they constitute a critical dependency for several scientific Python packages that distribute source code rather than precompiled Windows binaries. Installation at this stage prevented future interruptions during package installation and ensured compatibility with scientific software requiring local compilation.



Status



Completed.



=====================================================================



MD-1-010: Installed and Verified Scrublet



Following completion of the primary computational environment, additional preprocessing software required for doublet detection was evaluated.



Attempted installation of Scrublet through the conda-forge ecosystem using Mamba.



Package resolution failed because Scrublet was unavailable for the Windows 64-bit conda-forge distribution, resulting in a PackagesNotFoundError.



An alternative installation strategy was therefore adopted using



pip install scrublet



The initial pip installation did not complete successfully because the dependency Annoy required compilation of native C++ source code and no compatible precompiled wheel was available for the target platform.



Following installation of the Microsoft Visual Studio Build Tools documented in MD-1-009, the Scrublet installation procedure was repeated.



The Microsoft C++ compiler successfully compiled the Annoy extension module, allowing pip to complete installation of Scrublet together with its supporting dependencies, including scikit-image, imageio, tifffile, lazy-loader, and Cython.



Following installation, package availability was verified by executing



python -c "import scrublet; print(scrublet.\_\_file\_\_)"



The command returned the installed package location within



C:\\Miniforge\\envs\\maligpx\\



thereby confirming successful integration into the project's computational environment.



Scrublet will later be incorporated into the preprocessing workflow to identify probable doublets prior to downstream quality control, dimensionality reduction, clustering, and lineage analysis. Early removal of doublets reduces technical artifacts that could otherwise distort biological interpretation and trajectory inference.



Status



Completed.



=====================================================================



MD-1-011: Generated Final Reproducibility Specifications



Following installation of all required Conda and pip packages, the project's reproducibility specifications were regenerated to ensure that every installed dependency was accurately documented.



Executed



conda env export --no-builds > C:\\MaligPx\\environment.yml



to update the portable environment specification.



Executed



conda env export > C:\\MaligPx\\environment.lock.yml



to generate the exact lock specification representing the fully resolved software environment.



Executed



pip freeze > C:\\MaligPx\\requirements.txt



to regenerate the inventory of pip-managed packages after installation of CellRank, Scrublet, and all associated dependencies.



During export, Conda again reported the expected CondaExportWarning indicating the presence of packages installed through pip. Inspection of the exported environment confirmed that the warning corresponded to intentionally installed packages, including CellRank, Scrublet, pygpcca, Annoy, docrep, pygam, progressbar2, wrapt, imageio, scikit-image, tifffile, Cython, python-utils, and supporting libraries.



The exported files were manually reviewed to verify that environment.yml contained the intended portable environment specification, environment.lock.yml preserved the complete dependency graph, and requirements.txt accurately reflected every pip-installed package required for exact reconstruction of the computational environment.



These three files collectively constitute the official reproducibility specification for the MaligPx software environment.



Status



Completed.



=====================================================================



MD-SUMMARY



The computational infrastructure required for MaligPx has been successfully established. The project now possesses a fully reproducible scientific computing environment based on Miniforge, Conda, Mamba, Python 3.10, Scanpy, AnnData, scVelo, CellRank, Scrublet, and the supporting computational biology ecosystem.



The repository architecture has been standardized, comprehensive project documentation has been established, reproducibility specifications have been generated and verified, Git version control has been initialized, the repository has been synchronized with GitHub, the project has been released under the MIT License, and all software dependencies required for future preprocessing and downstream analysis have been successfully validated.



The computational foundation is therefore considered complete. Subsequent work transitions from software infrastructure into scientific data acquisition, repository auditing, preprocessing pipeline development, and biological analysis beginning with MD-2.



=====================================================================



MD-2: Dataset Acquisition, Documentation, and Provenance Management



Objective



Establish the complete data management infrastructure required for reproducible acquisition, documentation, verification, storage, preprocessing, and long-term maintenance of all biological datasets used throughout the MaligPx project.



Unlike the computational infrastructure established during MD-1, which focused on software reproducibility, MD-2 establishes scientific data reproducibility. Every dataset used by MaligPx shall possess complete provenance documentation, acquisition history, storage organization, integrity verification, metadata tracking, processing status, and permanent references before any biological analyses commence.



The objectives of MD-2 are therefore to construct the project's standardized data hierarchy, establish permanent dataset documentation, audit the repositories from which biological data will be obtained, define the preprocessing strategy required to generate expression matrices from raw sequencing reads, and ensure that every future computational result can be traced directly to its originating sequencing files.



=====================================================================



MD-2-001: Installed IBM Aspera Connect



The primary discovery dataset selected for MaligPx, Peng et al. (2019), is hosted by the Genome Sequence Archive (GSA) of the National Genomics Data Center (NGDC). Repository inspection demonstrated that the complete sequencing archive occupies approximately 2.69 TB and contains seventy compressed paired-end FASTQ files representing thirty-five independent sequencing runs.



Because downloading multiple terabytes through standard HTTPS connections would be unreliable and significantly slower than dedicated high-performance transfer protocols, an optimized transfer solution was required before biological data acquisition could begin.



Downloaded the Windows x64 release of IBM Aspera Connect from IBM's official distribution site.



Completed installation using the default installer configuration.



Installed the accompanying browser integration required by the NGDC download portal to initiate FASP-based transfers directly from the repository interface.



Following installation, executed the IBM Aspera Connect Diagnostic Tool supplied with the software package.



Verified that the desktop transfer client was correctly installed, that browser integration was functioning, and that the Aspera background service was operational.



Confirmed that the installation was capable of accepting transfer requests originating from supported repository pages.



IBM Aspera Connect was selected because it implements the FASP (Fast, Adaptive, Secure Protocol), which utilizes UDP-based transfer rather than conventional TCP-based file transmission. Unlike traditional HTTP or FTP downloads, FASP dynamically adapts transmission speed to available bandwidth while minimizing degradation caused by high latency and packet loss. This substantially reduces transfer time for very large sequencing datasets and decreases the probability of interrupted downloads requiring complete restart.



The installation of Aspera was completed before initiating any biological downloads to ensure that the primary dataset could later be transferred using the most reliable and efficient method supported by the Genome Sequence Archive.



Status



Completed.



=====================================================================



MD-2-002: Established the Standardized Biological Data Directory Structure



Following completion of the computational infrastructure, a permanent directory hierarchy was established under



C:\\MaligPx\\data\\



to provide a reproducible organizational framework for every biological dataset generated or acquired throughout the project.



The directory structure was intentionally created before downloading any sequencing data. Separating raw data, intermediate processing products, finalized analytical datasets, and RNA velocity resources prevents accidental overwriting of irreplaceable sequencing files while ensuring that every stage of the computational workflow remains independently reproducible.



The following primary directories were created.



C:\\MaligPx\\data\\raw\\



This directory will permanently store immutable raw biological data exactly as distributed by external repositories. Files within this directory shall never be modified manually. Any preprocessing performed on these files will produce new outputs elsewhere rather than altering the original repository downloads.



C:\\MaligPx\\data\\intermediate\\



This directory will store transient outputs generated during preprocessing, including alignment products, barcode correction results, quality-control summaries, temporary matrices, conversion products, and other computational artifacts required to construct finalized datasets. Files in this location may be regenerated whenever necessary because they are derived entirely from the raw data.



C:\\MaligPx\\data\\processed\\



This directory will contain finalized datasets ready for downstream biological analysis. These products include filtered AnnData objects, normalized expression matrices, integrated datasets, quality-controlled count matrices, annotated metadata, and other stable outputs that directly enter the Scanpy and CellRank analytical workflow.



C:\\MaligPx\\data\\velocity\\



This directory has been reserved specifically for RNA velocity analyses. Future preprocessing steps will generate spliced count matrices, unspliced count matrices, loom files, velocity-specific AnnData objects, CellRank transition kernels, absorption probabilities, lineage inference outputs, and other velocity-derived resources within this location. Separating velocity resources from conventional processed datasets simplifies workflow management while preserving reproducibility.



Following creation of the primary hierarchy, dataset-specific directories were established.



For the primary discovery cohort, the following structure was created.



C:\\MaligPx\\data\\raw\\peng2019\\



Within this directory, additional subdirectories were established.



C:\\MaligPx\\data\\raw\\peng2019\\fastq\\



This directory has been reserved for the seventy compressed paired-end FASTQ files distributed by the Genome Sequence Archive. These files constitute the immutable sequencing source from which all downstream analyses will ultimately originate.



C:\\MaligPx\\data\\raw\\peng2019\\metadata\\



This directory has been designated for repository metadata associated with the Peng et al. (2019) dataset, including the CRA001160.xlsx metadata spreadsheet, repository manifests, sample annotations, sequencing summaries, and accession records required for provenance tracking.



C:\\MaligPx\\data\\raw\\peng2019\\references\\



This directory has been reserved for documentation specific to the Peng et al. (2019) dataset, including supplementary information, repository records, publication resources, processing notes, and additional reference materials that directly describe the sequencing dataset.



Equivalent dataset-specific directories were also established for the future validation dataset.



C:\\MaligPx\\data\\raw\\elyada2019\\



with corresponding



C:\\MaligPx\\data\\raw\\elyada2019\\fastq\\



C:\\MaligPx\\data\\raw\\elyada2019\\metadata\\



and



C:\\MaligPx\\data\\raw\\elyada2019\\references\\



subdirectories.



Although the Elyada dataset has not yet been acquired, pre-establishing its storage hierarchy ensures that future acquisition follows the same reproducible organizational standard as the primary discovery cohort.



The complete directory hierarchy was reviewed following creation to verify consistency with the planned preprocessing workflow documented within the MaligPx methodology.



The standardized data architecture now provides dedicated locations for every category of biological resource that will be produced during subsequent preprocessing, quality control, integration, RNA velocity analysis, CellRank lineage inference, and future FSAI development.



Status



Completed.



=====================================================================



MD-2-003: Established the Scientific Data Documentation Framework



Before initiating acquisition of any biological datasets, a comprehensive documentation framework was established to ensure that every future dataset, preprocessing operation, repository audit, integrity verification, metadata update, and analytical product could be traced throughout the lifetime of the MaligPx project.



Rather than documenting datasets only after they had been downloaded, the documentation system was intentionally created beforehand. Establishing documentation prior to acquisition guarantees that provenance information is captured contemporaneously with every subsequent operation instead of being reconstructed retrospectively. This approach minimizes transcription errors, preserves complete historical context, and aligns with FAIR (Findable, Accessible, Interoperable, and Reusable) data-management principles that are widely recognized throughout computational biology and biomedical informatics.



The documentation framework was implemented within



C:\\MaligPx\\docs\\



through the creation and initialization of multiple complementary documents, each serving a distinct purpose within the overall data-management strategy.



Created



C:\\MaligPx\\docs\\dataset\_manifest.md



This document serves as the authoritative inventory of every biological dataset incorporated into MaligPx.



Unlike an acquisition log, which records chronological download events, the dataset manifest functions as a permanent reference catalogue describing the datasets themselves. Each dataset entry records scientific provenance, publication metadata, repository information, accession identifiers, sequencing platform, experimental design, download methods, storage location, licensing status, repository accessibility, expected file contents, processing status, and intended analytical role within the project.



The manifest was intentionally designed so that future readers can determine precisely which biological resources were used by the project without consulting external repositories.



At initialization, the document established the overall purpose of the manifest and created dedicated sections for the primary discovery cohort, future validation datasets, reference genomic resources, download-status tracking, and permanent repository references.



The initial version documented the Peng et al. (2019) Genome Sequence Archive repository, reserved space for the Elyada et al. (2019) validation cohort, identified future dependencies including the GRCh38 human reference genome and GENCODE gene annotation, and established a permanent table that will track acquisition and verification status throughout the project.



Created



C:\\MaligPx\\docs\\data\_dictionary.md



This document was created to maintain the biological inventory of every sample processed during the project.



Whereas the dataset manifest describes datasets at the repository level, the data dictionary records information at the individual sample level.



The document was initialized with a standardized sample inventory table containing columns for sequencing run accession, sample identifier, patient identifier, tissue source, tumor-versus-normal classification, paired FASTQ filenames, and processing status.



Because no sequencing files had yet been downloaded, the table was intentionally left empty. A note was inserted indicating that population of the table would occur immediately following successful acquisition and verification of the Peng et al. (2019) sequencing archive.



This separation between repository-level documentation and sample-level documentation ensures that project metadata remain scalable as additional datasets are incorporated into MaligPx.



Created



C:\\MaligPx\\docs\\acquisition\_log.md



This document serves as the chronological history of every biological data acquisition event performed during the project.



Unlike the dataset manifest, which records static information describing datasets, the acquisition log records actions performed by the research team.



Every future download, integrity verification, checksum validation, interrupted transfer, resumed download, metadata update, replacement file, repository revision, and acquisition-related observation will be entered into this log in chronological order.



The initial entries documented creation of the standardized biological data directory structure, initialization of the documentation framework, and confirmation that no sequencing data had yet been downloaded.



This establishes a clear historical boundary separating repository preparation from biological acquisition.



The acquisition log will subsequently document checksum verification, successful completion of Aspera transfers, validation of downloaded file sizes, confirmation of repository completeness, and any future repository revisions identified by the data providers.



Together, these three documents establish complementary layers of scientific documentation.



C:\\MaligPx\\docs\\dataset\_manifest.md



answers the question of which datasets are used.



C:\\MaligPx\\docs\\data\_dictionary.md



answers the question of which biological samples are present within those datasets.



C:\\MaligPx\\docs\\acquisition\_log.md



answers the question of what acquisition actions were performed, when they occurred, and whether the downloaded resources were verified successfully.



This separation of responsibilities reduces duplication of information while improving long-term maintainability of the project's documentation infrastructure.



The documentation framework established during this milestone will accompany every subsequent stage of dataset acquisition, preprocessing, quality control, integration, RNA velocity analysis, CellRank lineage inference, and future FSAI development, thereby ensuring that all biological resources remain completely traceable from their originating repositories through their final analytical outputs.



Status



Completed.



=====================================================================



MD-2-004: Completed Repository Audit of the Peng et al. (2019) Primary Discovery Cohort



Following establishment of the documentation framework, a comprehensive audit of the primary biological dataset was performed before any files were downloaded.



The purpose of the audit was to establish complete scientific provenance, verify public availability of the sequencing archive, document repository metadata, identify the expected biological contents, determine download requirements, estimate storage demands, identify any repository revisions affecting reproducibility, and ensure that sufficient information had been recorded to reproduce the acquisition process independently.



The selected primary discovery cohort was identified as the single-cell RNA sequencing dataset published by Peng et al. in 2019.



Publication title



Single-cell RNA-seq highlights intra-tumoral heterogeneity and malignant progression in pancreatic ductal adenocarcinoma.



Journal



Cell Research



Publication year



2019\.



Digital Object Identifier (DOI)



10.1038/s41422-019-0195-y.



The publication investigates cellular heterogeneity within pancreatic ductal adenocarcinoma through large-scale single-cell transcriptomic profiling of malignant and matched normal pancreatic tissues. Because the study includes malignant epithelial cells together with multiple stromal and immune populations, it provides an appropriate foundation for development of lineage inference, RNA velocity, CellRank analyses, and future FSAI modelling within the MaligPx project.



The public sequencing repository associated with the publication was identified within the Genome Sequence Archive (GSA) maintained by the National Genomics Data Center (NGDC).



Repository



Genome Sequence Archive (GSA), National Genomics Data Center.



Repository accession



CRA001160.



Associated BioProject



PRJCA001063.



Repository release date



9 July 2019.



Repository inspection confirmed that the archive remains publicly accessible without controlled-access approval or institutional authorization. Consequently, dataset acquisition may be performed directly through the repository using the download mechanisms supplied by the National Genomics Data Center.



The repository provides four officially supported download mechanisms.



HTTPS download.



FTP download.



IBM Aspera FASP transfer.



QTrans download.



Because the complete repository occupies approximately 2.69 terabytes, IBM Aspera was selected as the preferred acquisition method during MD-2-001 due to its substantially greater reliability and transfer efficiency for very large sequencing datasets.



Inspection of the repository metadata demonstrated that the complete sequencing archive contains thirty-five sequencing experiments corresponding to thirty-five sequencing runs.



Each sequencing run consists of paired-end sequencing data distributed as two compressed FASTQ files.



Consequently, the complete repository contains seventy compressed FASTQ files.



Repository metadata further identified the sequencing platform as



Illumina HiSeq X Ten.



The sequencing chemistry employed by the study was reported as



inDrop



which was recorded because preprocessing software, barcode parsing, and downstream expression matrix generation depend upon the underlying single-cell capture technology.



Biological inspection of the repository confirmed that the study consists of twenty-four pancreatic ductal adenocarcinoma specimens together with eleven matched normal pancreatic tissue specimens, yielding a total of thirty-five biological samples.



The repository metadata spreadsheet



CRA001160.xlsx



was identified as the primary source of sample-level metadata and designated for storage within



C:\\MaligPx\\data\\raw\\peng2019\\metadata\\



immediately following acquisition.



The expected sequencing files were designated for storage within



C:\\MaligPx\\data\\raw\\peng2019\\fastq\\



without modification following download.



Inspection of repository contents further demonstrated that the archive distributes raw sequencing reads only.



No processed gene-expression matrices, normalized expression matrices, filtered count matrices, AnnData objects, Seurat objects, loom files, RNA velocity matrices, or downstream analytical products are supplied by the repository.



This observation has important methodological implications because it establishes that all expression matrices required by MaligPx must be reconstructed directly from the raw sequencing reads rather than obtained from external processed resources.



This requirement was subsequently formalized as Decision DEC-008 recorded within



C:\\MaligPx\\docs\\decisions.md



thereby incorporating raw-sequence preprocessing into the official computational methodology.



Repository inspection additionally identified an important post-publication revision issued by the Genome Sequence Archive.



On 14 January 2021, eight sequencing runs were replaced by the repository administrators.



The obsolete accessions and their replacement accessions were documented as follows.



CRX030762, sample T1, replaced run CRR034496 with CRR241805.



CRX030763, sample T2, replaced run CRR034497 with CRR241798.



CRX030764, sample T3, replaced run CRR034498 with CRR241799.



CRX030768, sample T7, replaced run CRR034502 with CRR241800.



CRX030774, sample T13, replaced run CRR034508 with CRR241801.



CRX030780, sample T19, replaced run CRR034514 with CRR241802.



CRX030781, sample T20, replaced run CRR034515 with CRR241804.



CRX030784, sample T23, replaced run CRR034518 with CRR241803.



The replacement accession numbers were incorporated into the dataset documentation to ensure that all future downloads retrieve the current repository versions rather than obsolete sequencing runs referenced by earlier versions of the archive.



Failure to recognize these repository revisions could produce inconsistencies between locally acquired sequencing data and the current public archive. Recording the updated accession numbers therefore strengthens long-term reproducibility by explicitly documenting the repository state used by MaligPx.



Following completion of the repository audit, the collected metadata were incorporated into



C:\\MaligPx\\docs\\dataset\_manifest.md



including publication metadata, repository identifiers, BioProject accession, release date, sequencing platform, single-cell technology, biological scope, download methods, repository size, expected file inventory, local storage locations, replacement sequencing runs, processing status, and planned analytical role within the project.



No biological data were downloaded during this milestone.



The purpose of the activity was exclusively to establish complete scientific provenance before initiating data acquisition.



Status



Completed.



=====================================================================



MD-2-005: Established the Official Raw Sequencing Data Processing Strategy



Completion of the repository audit established that the Genome Sequence Archive release associated with Peng et al. (2019) distributes only raw paired-end FASTQ sequencing files together with sample metadata. No processed expression matrices, quality-controlled count matrices, normalized expression matrices, AnnData objects, Seurat objects, loom files, RNA velocity matrices, or downstream analytical products are included within the public repository.



This finding required a methodological review of the originally proposed Phase 2 workflow.



The original computational methodology assumed that raw count matrices would be imported directly into AnnData objects before preprocessing. Repository inspection demonstrated that this assumption was incompatible with the publicly available data because no count matrices exist within the official archive.



Rather than replacing the primary discovery cohort with an alternative dataset containing processed matrices, the project formally adopted reconstruction of gene-expression matrices directly from the released raw sequencing reads.



This decision preserves complete analytical independence from third-party preprocessing pipelines while ensuring that every computational transformation performed throughout MaligPx is reproducible from the original sequencing data released by Peng et al. (2019).



The revised workflow establishes the raw FASTQ files as the permanent computational starting point of the project.



Accordingly, every downstream biological result generated by MaligPx will ultimately be traceable to the original sequencing reads archived within CRA001160.



The preprocessing workflow will therefore precede every Scanpy analysis.



The official preprocessing sequence adopted by MaligPx is as follows.



The complete sequencing archive will first be downloaded into



C:\\MaligPx\\data\\raw\\peng2019\\fastq\\



using IBM Aspera FASP transfer.



Immediately following download, file integrity will be verified through cryptographic checksum validation.



Checksum values will be recorded within



C:\\MaligPx\\docs\\checksums.md



thereby establishing permanent verification that each downloaded file exactly matches the version distributed by the Genome Sequence Archive.



Following integrity verification, the complete metadata spreadsheet



CRA001160.xlsx



will be stored within



C:\\MaligPx\\data\\raw\\peng2019\\metadata\\



where it will serve as the authoritative reference for sample identifiers, experimental design, sequencing runs, and biological annotations.



The raw sequencing reads will subsequently undergo expression matrix reconstruction using preprocessing software appropriate for the inDrop single-cell sequencing chemistry employed by Peng et al. (2019).



The preprocessing stage will perform all required operations for reconstruction of gene-level expression matrices from the raw sequencing reads, including barcode identification, barcode correction where applicable, unique molecular identifier (UMI) processing, read alignment against the selected human reference genome, transcript assignment, gene counting, and generation of sparse expression matrices suitable for downstream single-cell analysis.



The resulting count matrices will become the first computational products generated entirely within the MaligPx analytical framework.



Only after completion of expression matrix reconstruction will the processed outputs be imported into AnnData objects for Scanpy preprocessing.



This revision changes the first executable step of Phase 2 from



"Raw count matrices and metadata are imported into AnnData objects and processed separately per dataset before integration."



to



"Raw paired-end FASTQ sequencing files are processed through an expression-matrix reconstruction pipeline to generate gene-level count matrices. The reconstructed count matrices, together with the accompanying sample metadata, are subsequently imported into AnnData objects and processed separately for each dataset before downstream integration."



This modification substantially strengthens the scientific rigor of the computational methodology because every preprocessing decision becomes transparent, reproducible, and completely controlled by the project rather than inherited from external investigators.



The revised workflow additionally enables generation of spliced and unspliced transcript counts required for RNA velocity analyses.



Because RNA velocity estimation depends upon distinguishing mature spliced transcripts from nascent unspliced transcripts during preprocessing, direct reconstruction from raw sequencing reads provides considerably greater flexibility than reliance upon externally processed count matrices.



The revised computational strategy therefore improves compatibility with the downstream scVelo and CellRank analyses planned within later phases of the MaligPx project.



The methodological revision was formally adopted through Decision DEC-008 recorded within



C:\\MaligPx\\docs\\decisions.md



which establishes reconstruction of expression matrices from raw sequencing reads as the official preprocessing strategy for all future analyses involving the Peng et al. (2019) discovery cohort.



The consequences of this decision extend throughout the analytical pipeline.



Future preprocessing documentation, quality-control procedures, intermediate outputs, processed datasets, RNA velocity analyses, lineage inference, and final biological interpretations will all originate from computational products generated directly within MaligPx.



This eliminates dependence upon externally processed count matrices, improves methodological transparency, strengthens computational reproducibility, and increases confidence that every downstream biological conclusion can be reproduced independently beginning from the original sequencing reads archived within CRA001160.



Status



Completed.



=====================================================================



MD-SUMMARY



The objectives established for MD-2 were to prepare the MaligPx project for reproducible acquisition and processing of biological sequencing datasets while ensuring that every computational, organizational, and methodological component required for subsequent analyses had been established before any sequencing data entered the repository. These objectives have now been completed.



IBM Aspera Connect was successfully installed and verified, establishing a high-performance data-transfer mechanism capable of downloading multi-terabyte sequencing repositories from the Genome Sequence Archive using the FASP protocol. Installation of the browser integration, desktop client, and diagnostic utilities confirmed that the transfer infrastructure was operational before any biological datasets were accessed.



The project data architecture was designed and implemented beneath the canonical project root located at



C:\\MaligPx\\



The standardized directory hierarchy now separates raw sequencing data, intermediate computational products, processed analytical datasets, RNA velocity resources, documentation, scripts, notebooks, references, configuration files, figures, logs, source code, and testing resources. Dataset-specific storage locations were established before acquisition to prevent future restructuring of biological data after analysis has begun.



Within the project data hierarchy, dedicated storage locations were established for the Peng et al. (2019) discovery cohort and the Elyada et al. (2019) validation cohort. Independent directories were created for raw sequencing reads, metadata, processed outputs, reference resources, and future analytical products so that every computational artifact generated throughout the project can be traced directly to its originating dataset.



The documentation framework supporting dataset provenance and acquisition was completed before downloading biological data. The following project documentation files now constitute the permanent record governing dataset management throughout MaligPx.



C:\\MaligPx\\docs\\dataset\_manifest.md



records complete provenance information, repository identifiers, publication metadata, download methods, accession numbers, release information, repository status, intended analytical purpose, and long-term acquisition status for every dataset incorporated into the project.



C:\\MaligPx\\docs\\data\_dictionary.md



provides the master inventory of biological samples, sequencing runs, metadata, processing status, and future sample-level annotations that will be expanded as datasets enter the computational pipeline.



C:\\MaligPx\\docs\\acquisition\_log.md



serves as the chronological record of every download event, repository audit, integrity verification procedure, checksum validation, and acquisition milestone performed throughout the project.



C:\\MaligPx\\docs\\checksums.md



was introduced as the permanent integrity-verification register for downloaded sequencing files and reference resources. SHA-256 checksum verification will be recorded within this document immediately following each completed acquisition, thereby providing cryptographic confirmation that locally stored files exactly match the versions distributed by their original repositories.



The primary discovery dataset associated with Peng et al. (2019) underwent a comprehensive repository audit before download. The official Genome Sequence Archive release CRA001160, belonging to BioProject PRJCA001063, was verified as the authoritative public repository. Publication metadata, repository metadata, accession identifiers, sequencing platform, sequencing chemistry, organism, disease context, tissue origin, experimental design, patient composition, experiment count, sequencing-run count, download methods, metadata availability, repository size, public accessibility, and archival update history were documented within the permanent project records.



Repository inspection further confirmed that the public archive distributes seventy compressed paired-end FASTQ sequencing files corresponding to thirty-five sequencing runs and thirty-five biological experiments. The repository contains raw sequencing data together with accompanying metadata but does not distribute processed expression matrices suitable for direct import into Scanpy.



Identification of this repository characteristic required revision of the originally proposed preprocessing methodology. Rather than relying upon externally generated count matrices, MaligPx formally adopted reconstruction of gene-expression matrices directly from the raw sequencing reads distributed by the Genome Sequence Archive. This methodological revision has been permanently recorded within



C:\\MaligPx\\docs\\decisions.md



as Decision DEC-008 and establishes raw sequencing data as the official computational starting point of the analytical workflow.



The revised preprocessing strategy substantially strengthens computational reproducibility because every transformation performed throughout the pipeline will originate from publicly archived sequencing reads rather than from processed matrices generated by external investigators. Barcode processing, unique molecular identifier correction, alignment, transcript quantification, generation of expression matrices, quality control, RNA velocity preparation, lineage inference, and downstream biological analyses will therefore remain completely reproducible from the original sequencing archive.



The computational reproducibility framework established during MD-1 was further strengthened during MD-2 through refinement of repository metadata. The official project environment specification contained within



C:\\MaligPx\\environment.yml



was updated to reflect the finalized computational environment while documenting the expected Conda export warning associated with Windows-specific pip-installed scientific packages.



The complete exported Conda environment was preserved within



C:\\MaligPx\\environment.lock.yml



to capture the exact dependency state of the computational environment at the conclusion of infrastructure preparation.



The pip dependency inventory contained within



C:\\MaligPx\\requirements.txt



was regenerated and frozen, ensuring that packages unavailable through conda-forge—including CellRank, Scrublet, pygpcca, and their associated dependencies—remain reproducible across future installations.



Repository metadata underwent additional refinement before commencement of biological analyses. The GitHub repository now includes an MIT License as its official software license, thereby permitting open scientific reuse while preserving attribution requirements. Synchronization between the local Git repository and the published GitHub repository was successfully completed, establishing the remote repository as the canonical public version of MaligPx. The repository now maintains synchronized local and remote histories, enabling transparent version control throughout the remainder of the project.



Project documentation was expanded to improve reproducibility, transparency, and long-term maintainability. The project README was revised to describe the scientific objectives, computational architecture, repository organization, installation procedure, software environment, reproducibility strategy, licensing information, project status, and future development roadmap. The project log, research log, decision log, acquisition log, dataset manifest, data dictionary, and checksum register together now provide complete documentation of the scientific and computational state of the repository before biological data acquisition begins.



Completion of MD-2 signifies that the computational infrastructure established during MD-1 has now been extended into a fully documented, reproducible, and acquisition-ready scientific repository. No biological sequencing data have yet entered the computational workflow, thereby ensuring that all subsequent preprocessing, quality control, alignment, expression-matrix reconstruction, RNA velocity estimation, trajectory inference, and downstream analyses will be performed within a fully version-controlled environment whose computational state has been frozen before data acquisition.



The project is therefore prepared to enter the next phase of development, during which the Peng et al. (2019) sequencing archive will be downloaded, verified using cryptographic checksums, reconstructed into expression matrices through the approved preprocessing pipeline, and imported into AnnData objects for downstream single-cell analysis.



Status



Completed.



=====================================================================

