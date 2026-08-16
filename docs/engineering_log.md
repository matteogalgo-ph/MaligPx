MD-1: Software \& Environment Initialization

&#x09;Set up a new GitHub account under matteogalgo.ph@gmail.com.

MD-1-001: Installed Git



&#x09;Downloaded and installed Git.

&#x09;MD-1-002: Installed Miniforge

&#x09;Downloaded and installed Miniforge to C:\\Miniforge.

&#x09;Ran conda update -n base -c conda-forge conda to update the base Conda installation from the public conda-	forge repository.

&#x09;Updated ca-certificates, certifi, conda, and openssl.

&#x09;Installed Mamba v2.5.0 (conda install -n base -c conda-forge mamba) and verified installation using 	mamba --version.



MD-1-003: Created Primary Project Environment



&#x09;Created the primary project environment.

&#x09;Ran mamba create -n maligpx python=3.10.

&#x09;Created the Conda environment maligpx with Python 3.10.

&#x09;Mamba resolved dependencies and installed 19 packages.

&#x09;Activated the environment using conda activate maligpx.

&#x09;MD-1-004: Resolved Environment Execution Failure

&#x09;Encountered environment execution failure.

&#x09;Windows blocked execution of C:\\Miniforge\\envs\\maligpx\\python.exe, reporting a "Device Guard policy" 	restriction despite the system being a personal Windows 11 Home installation.

&#x09;Confirmed that the base Miniforge interpreter executed correctly while only the environment interpreter 	was blocked.

&#x09;Performed systematic diagnostics to distinguish Conda configuration issues from Windows security 	enforcement.

&#x09;Identified Windows Smart App Control (SAC) as the most probable source of the restriction.

&#x09;Disabled Smart App Control, restarted the system, and confirmed successful execution of the maligpx Python 	interpreter.

&#x09;Environment execution restored without modifying the Conda installation.

&#x09;Ready to install scientific software stack.



MD-1-005: Installed Scientific Computing Ecosystem



&#x09;Installed the core computational biology ecosystem using Mamba, including Scanpy, AnnData, NumPy, SciPy, 	Pandas, Matplotlib, JupyterLab, IPykernel, NetworkX, igraph, python-igraph, Leidenalg, Scikit-learn, 	Statsmodels, Black, Ruff, isort, scVelo.

&#x09;Attempted installation of CellRank using the conda-forge distribution through Mamba.

&#x09;Dependency resolution failed because the current Windows package requires pygpcca, which depends on PETSc. 	Windows PETSc builds are presently unavailable through conda-forge, preventing a solvable dependency 	graph.

&#x09;Confirmed that the issue originated from upstream package availability rather than the local Conda 	environment.

&#x09;Installed CellRank using pip install cellrank

&#x09;Verified successful installation: python -c "import cellrank; print(cellrank.\_\_version\_\_)" Installed 	version: CellRank 2.0.7. The scientific software stack is considered successfully installed.



MD-1-006: Verified Computational Environment



&#x09;Created an environment verification script (environment\_test.py) to validate successful imports of the 	core scientific computing ecosystem.

&#x09;Verified successful import of the primary project dependencies, confirming that the computational 	environment was fully operational.

&#x09;Exported the Conda environment specification: conda env export --no-builds > environment.yml

&#x09;Exported the Python package inventory:

&#x09;pip freeze > requirements.txt

&#x09;Recorded the expected Conda export warning indicating the presence of pip-installed packages. Confirmed 	that the warning resulted from the intentional installation of CellRank via pip and did not affect 	reproducibility.



MD-1-007: Established Project Infrastructure



&#x09;Created the canonical project root: C:\\MaligPx

&#x09;Constructed the standardized project directory structure, including:

&#x09;	configs/

&#x09;	data/

&#x09;	docs/

&#x09;	figures/

&#x09;	logs/

&#x09;	notebooks/

&#x09;	references/

&#x09;	results/

&#x09;	scripts/

&#x09;	src/

&#x09;	tests/

&#x09;Created the initial project files:

&#x09;	.gitignore

&#x09;	.gitattributes

&#x09;	environment.yml

&#x09;	requirements.txt

&#x09;Established the documentation framework by creating:

&#x09;	project\_log.md

&#x09;	engineering\_log.md

&#x09;	research\_log.md

&#x09;	decisions.md



MD-1-008: Initialized Version Control



&#x09;Initialized the MaligPx Git repository.

&#x09;Created the root commit:

&#x09;	8fde32a

&#x09;Message:

&#x09;	Initial commit

&#x09;Subsequently committed the project scaffold and finalized the repository structure through incremental 	commits, establishing the reproducible baseline for all future development.

MD-3(August 16, 2026) — Environment Verification



The MaligPx computational environment was verified on Windows 64-bit.



Core packages successfully imported:

\- Python 3.10.20

\- Scanpy 1.11.5

\- AnnData 0.11.4

\- scVelo 0.3.4

\- CellRank 2.0.7

\- scvi-tools 1.3.3

\- Scrublet 0.2.3

\- PyTorch 2.13.0+cpu

\- TorchMetrics 1.9.0



A Windows-specific Conda lockfile was generated:

`environment.lock.yml`



Command:

`conda-lock lock --file environment.yml --platform win-64 --lockfile environment.lock.yml`



Lockfile generation completed successfully.

