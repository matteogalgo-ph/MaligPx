**Dataset Manifest**



**Project**

MaligPx



**Purpose**

This document records every dataset used in the MaligPx workflow, including acquisition source, provenance, download status, integrity verification, and intended analytical use.



**Primary Dataset**



**Dataset ID:** DS-001

**Dataset:** Peng et al. (2019)

**Title:** Single-cell RNA-seq highlights intra-tumoral heterogeneity and malignant progression in pancreatic ductal adenocarcinoma

**Authors:** Junya Peng, Bao-Fa Sun, Chuan-Yuan Chen, Jia-Yi Zhou, Yu-Sheng Chen, Hao Chen, Lulu Liu, Dan Huang, Jialin Jiang, Guan-Shen Cui, Ying Yang, Wenze Wang, Dan Guo, Menghua Dai, Junchao Guo, Taiping Zhang, Quan Liao, Yi Liu, Yong-Liang Zhao, Da-Li Han, Yupei Zhao, Yun-Gui Yang, Wenming Wu

**Publication:** Cell Research, 2019, 29(9), 725–738. https://doi.org/10.1038/s41422-019-0195-y

**DOI:** 10.1038/s41422-019-0195-y

**Organization:** Beijing Institute of Genomics, Chinese Academy of Sciences

**Repository:** Genome Sequence Archive (GSA), National Genomics Data Center (NGDC)

**Repository URL:** https://ngdc.cncb.ac.cn/gsa/

**Dataset URL:** https://ngdc.cncb.ac.cn/gsa/browse/CRA001160

**BioProject:** PRJCA001063

**Accession:** CRA001160 (GSA)

**Release date:** 2019-07-09

**Date accessed:** 2026-07-18

**Organism:** Homo sapiens

**Disease:** Pancreatic ductal adenocarcinoma (PDAC)

**Data Type:** Transcriptome or Gene expression

**Sample Scope:** Single-cell

**Relevance:** Medical

**Tissue:** Primary pancreatic tumor and matched normal pancreatic tissue

**Experimental Design:** Single-cell RNA sequencing of PDAC tumor and normal pancreatic samples to characterize tumor heterogeneity, the tumor microenvironment, and determine the transcriptomes of over 50,000 individual pancreatic cells.

**Number of Patients:** 24 patients with PDAC tumors (primary); 11 normal pancreas(control)

**Number of Experiments:** 35

**Number of Runs:** 35

**Biosample:** 35

**Number of FASTQ Files:** 70

**Data Format:** Raw paired-end FASTQ files (.fastq.gz)

**Platforms:** Illumina HiSeq X Ten

**Single-cell technology:** inDrop

**Download Methods:**  HTTPS, FTP, Aspera, QTrans

**Metadata File:** CRA001160.xlsx

**Total Download Size, Repository Size:** 2694.29 GB

**License / Accessibility:** Publicly available at https://ngdc.cncb.ac.cn/gsa/browse/CRA001160

**Local Storage:** C:\\MaligPx\\data\\raw\\peng2019\\

**Notes:** Dataset contains 70 FASTQ files across 35 sequencing runs. Eight sequencing runs were replaced by GSA on 2021-01-14. Current downloads should use the replacement run accessions rather than the obsolete accessions.

**Run replacements (2021-01-14):**

Experiment accession	Run alias	Old run accession	New run accession

CRX030762	        T1	        CRR034496	        CRR241805

CRX030763	        T2	        CRR034497	        CRR241798

CRX030764	        T3	        CRR034498               CRR241799

CRX030768	        T7	        CRR034502	        CRR241800

CRX030774	        T13	        CRR034508	        CRR241801

CRX030780	        T19	        CRR034514	        CRR241802

CRX030781	        T20	        CRR034515	        CRR241804

CRX030784	        T23	        CRR034518	        CRR241803

Status:

**Repository identified -** 8/15/26

Download not yet initiated.

**Expected Contents:**

\- Tumor samples

\- Normal pancreatic samples

\- Single-cell RNA sequencing data

**Intended Analytical Use:** The repository contains raw sequencing data only. Count matrices are not provided and must be generated through the alignment pipeline. 8/15/26 update: Raw FASTQ files will be obtained from the above links, then processed through alevin-fry.



\---



**Secondary Dataset**



**Dataset ID:** DS-002

**Dataset:** Steele et al. (2020)

**Title:** Multimodal Mapping of the Tumor and Peripheral Blood Immune Landscape in Human Pancreatic Cancer

**Authors:** Nina G. Steele, Eileen S. Carpenter, Samantha B. Kemp, Veerin R. Sirihorachai, Stephanie The, Lawrence Delrosario, Jenny Lazarus, El-ad David Amir, Valerie Gunchick, Carlos Espinoza, Samantha Bell, Lindsey Harris, Fatima Lima, Valerie Irizarry-Negron, Daniel Paglia, Justin Macchia, Angel Ka Yan Chu, Heather Schofield, Erik-Jan Wamsteker, Richard Kwon, Allison Schulman, Anoop Prabhu, Ryan Law, Arjun Sondhi, Jessica Yu, Arpan Patel, Katelyn Donahue, Hari Nathan, Clifford Cho, Michelle A. Anderson, Vaibhav Sahai, Costas A. Lyssiotis, Weiping Zou, Benjamin L. Allen, Arvind Rao, Howard C. Crawford, Filip Bednar, Timothy L. Frankel \& Marina Pasca di Magliano

**Publication:** Nature Cancer, 1(11), 1097–1112, https://doi.org/10.1038/s43018-020-00121-4

**DOI:** 10.1038/s43018-020-00121-4

**Organization:** Michigan Medicine - University of Michigan 

**Repository:** National Center for Biotechnology Information Gene Expression Omnibus 

**Repository URL:** https://www.ncbi.nlm.nih.gov/

**Dataset URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE155698

**BioProject:** PRJNA655238

**Accession:** GSE155698 (GEO)

**Release date:** 2020-01-10

**Date accessed:** 2026-08-15

**Organism:** Homo sapiens

**Disease:** Pancreatic ductal adenocarcinoma (PDAC)

**Data Type:** Transcriptome or Gene expression

**Sample Scope:** Single-cell

**Relevance:** Medical

**Tissue:** Primary pancreatic tumor and matched normal pancreatic tissue

**Experimental Design:** This repository contains 16 PDA tissue samples, 3 adjacent normal pancreas samples, 16 PBMC samples isolated from human PDA patients, and 4 PBMC samples isolated from healthy volunteers. Tissues were mechanically minced and enzymatically digested with collagenase P (1mg/mL DMEM) and subsequently filtered through a 40μm mesh to obtain single cells. Dead cells were removed using MACS®Dead Cell Removal Kit (Miltenyi Biotec Inc.). Single-cell cDNA libraries were prepared and sequenced at the University of Michigan Sequencing Core using the 10x Genomics Platform. Samples were run using paired end 50 cycle reads on HiSeq 4000 or the NovaSeq 6000 (Illumina) to a depth of 100,000 reads. The raw data were processed and aligned by the University of Michigan DNA Sequencing Core. Cellranger count version 3.0.0 with default settings was used, with an initial expected cell count of 10,000.

Submitter states the raw data is deposted in the dbGaP: accession number phs002071.v1.p1

**Number of Patients:** 25 patients (participants enrolled in dbGaP cohort)**Number of Experiments:** 39 single-cell sample libraries (GSM4710688 through GSM4710726)

**Number of Runs:** 39 (matching the sample libraries pooled across sequencing lines)

**Biosample:** 39 unique Biosample entries

**Number of FASTQ Files:** 156 files (Paired-end sequencing containing R1, R2, and I1/I2 index configurations per sample run)

**Data Format:** Raw paired-end FASTQ files (.fastq.gz). However note that raw FASTQ files are controlled-access.

**Platforms:** Illumina HiSeq 4000 / Illumina NovaSeq 6000

**Single-cell technology:** 10x Genomics Chromium Single Cell 3' (v3)

**Download Methods:**  HTTPS, FTP

**Metadata File:** GSE155698\_series\_matrix.txt.gz

**Total Download Size, Repository Size:** \~450 MB (For public GEO processed matrices); \~2.1 TB (For controlled dbGaP raw sequencing reads)

**License / Accessibility:** Processed matrices are public; Raw data requires controlled Data Access Committee (DAC) approval through dbGaP.

**Local Storage: C:\\MaligPx\\data\\validation\\steele2020\\**

**Notes:** Raw data is controlled-access, but I do not need the spliced and unspliced raw reads as CellRank 2 will build the main directed transition model using the PseudotimeKernel built on top of Slingshot pseudotime, meaning the open-access expression matrices are completely sufficient to compute the three Hill-based components.



\---



**Reference Resources**



***Human Reference Genome:***

Pending (GRCh38)

***Gene Annotation:***

Pending (GENCODE)

***Velocity Reference:***

Pending



\---



**Download Status**



|**Dataset**|**Status**|**Verified**|
|-|-|-|
|Peng et al. (2019)|Pending|No|
|Steele et al. (2020)|Pending|No|
|GRCh38|Pending|No|
|GENCODE|Pending|No|



**Permanent Record**



|**Resource**|**URL**|**Purpose**|
|-|-|-|
|Peng et al. (2019), genome sequence analysis (GSA) dataset|https://ngdc.cncb.ac.cn/gsa/browse/CRA001160<br /><br />May also be accessed through:<br />https://zenodo.org/records/3969339|Primary discovery cohort|
|Steele et al. (2020)|https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE155698|Cross-species validation of tumor-stromal evolutionary dynamics|
|GENCODE|https://www.gencodegenes.org|Gene annotation|
|Ensembl|https://www.ensembl.org|Genome annotation|
|CellRank|https://cellrank.readthedocs.io|Fate inference|
|scVelo|https://scvelo.readthedocs.io|RNA velocity|
|scanpy|https://scanpy.readthedocs.io|Single-cell preprocessing|



