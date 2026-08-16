\# MaligPx Analysis Plan



\## Objective



MaligPx will characterize malignant-cell state and fate plasticity in pancreatic ductal adenocarcinoma (PDAC) using single-cell transcriptomic data and a prespecified computational workflow integrating dimensionality reduction, malignant-cell identification, trajectory inference, RNA velocity, and CellRank fate probabilities.



\## Primary Analysis Workflow



1\. Obtain or reconstruct the input expression matrices from the selected PDAC single-cell datasets.



2\. Perform dataset-specific quality control using the prespecified operational thresholds.



3\. Identify and retain malignant cells using the prespecified epithelial-marker and CNV-based annotation strategy.



4\. Select highly variable genes using the prespecified feature-selection method.



5\. Train a scVI model using 50 latent dimensions.



6\. Construct a 30-nearest-neighbor graph using the resulting latent representation.



7\. Perform Leiden clustering.



8\. Generate UMAP embeddings for visualization and assessment of the resulting cellular structure.



9\. Prepare the malignant-cell object for trajectory inference.



10\. Perform the trajectory and RNA-velocity preparation required for CellRank.



11\. Infer cellular transition probabilities and terminal-state fate probabilities using CellRank.



12\. Calculate the prespecified Fate Plasticity Index (FPI) from the resulting fate-probability distributions.



13\. Perform the prespecified statistical analyses and sensitivity analyses.



\## Primary Parameters



|Parameter|Primary value|
|-|-|
|-----|-----|
|Highly variable genes|3000|
|scVI latent dimensions|50|
|kNN neighbors|30|
|CellRank backward-transition parameter (b) |10|
|Cellrank shape parameter (v)|0.5|
|GPCCA macrostates|2-6|



Sensitivity-analysis parameters are documented separately in docs/parameter\_log.md.



\## Reproducibility



The computational environment is defined by:



\- `environment.yml` — project environment specification

\- `environment.lock.yml` — platform-specific locked environment

\- `requirements.txt` — pip-installed package versions



Execution records are maintained in the `logs/` directory.

