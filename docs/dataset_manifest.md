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

**Organisms:** Homo sapiens

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

&#x09;Repository identified.

&#x09;Download not yet initiated.

Expected Contents:

\- Tumor samples

\- Normal pancreatic samples

\- Single-cell RNA sequencing data

Notes: The repository contains raw sequencing data only. Count matrices are not provided and must be generated through the alignment pipeline.



\---



**Secondary Dataset**



Dataset:

Elyada et al. (2019)



Status:

Not yet acquired.



Purpose:

Tumor microenvironment validation dataset.



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
|Elyada et al. (2019)|Pending|No|
|GRCh38|Pending|No|
|GENCODE|Pending|No|



**Permanent Record**



|**Resource**|**URL**|**Purpose**|
|-|-|-|
|Peng et al. (2019), genome sequence analysis (GSA) dataset|https://ngdc.cncb.ac.cn/gsa/browse/CRA001160<br /><br />May also be accessed through:<br />https://zenodo.org/records/3969339|Primary discovery cohort|
|Elyada et al. (2019) dataset|https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129455|Stromal validation|
|GENCODE|https://www.gencodegenes.org|Gene annotation|
|Ensembl|https://www.ensembl.org|Genome annotation|
|CellRank|https://cellrank.readthedocs.io|Fate inference|
|scVelo|https://scvelo.readthedocs.io|RNA velocity|
|scanpy|https://scanpy.readthedocs.io|Single-cell preprocessing|



