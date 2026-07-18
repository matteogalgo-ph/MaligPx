\# Data Dictionary



\## Project



MaligPx



\## Purpose



This document records every biological sample incorporated into the MaligPx project. It functions as the authoritative inventory of sequencing runs, biological specimens, associated metadata, local storage locations, processing status, and quality-control progress throughout the complete computational workflow.



Unlike the Dataset Manifest, which documents dataset-level provenance, this document records sample-level information. Every sequencing run that enters the project will receive one corresponding entry in this file. No sequencing data may progress beyond acquisition until its metadata have been documented here.



\---



\# Dataset Status



\## DS-001



Dataset



Peng et al. (2019)



Accession



CRA001160



Repository



Genome Sequence Archive (GSA)



Current Status



Repository audited.



Metadata documented.



Download not initiated.



FASTQ verification pending.



Checksum verification pending.



Expression matrix generation pending.



Quality-control pending.



Velocity preprocessing pending.



\---



\# Sample Status Definitions



Every sample progresses through the following lifecycle.



| Status | Definition |

|----------|------------|

| Repository Identified | Sample exists within the public repository but has not yet been downloaded. |

| Downloaded | FASTQ files have been transferred successfully to local storage. |

| Checksum Verified | File integrity has been confirmed using repository-provided checksum values. |

| Metadata Verified | Sample metadata have been inspected and confirmed against the repository. |

| Matrix Generated | Raw sequencing reads have been converted into a gene-expression count matrix. |

| Quality Controlled | Cell- and gene-level filtering have been completed. |

| Velocity Processed | Spliced and unspliced matrices have been generated for RNA velocity. |

| Integrated | Sample has entered the integrated AnnData object. |

| Completed | All preprocessing has been completed successfully. |



\---



\# Peng et al. (2019)



\## Repository Summary



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



\---



\# Sample Inventory



The following table will be populated immediately after dataset acquisition.



| Run Alias | Run Accession | Experiment | Sample Accession | Tissue | Classification | FASTQ Forward | FASTQ Reverse | Download Status | Checksum | Matrix | QC | Velocity | Notes |

|------------|---------------|------------|------------------|---------|----------------|---------------|---------------|-----------------|----------|--------|----|----------|-------|



No sequencing runs have been downloaded at this stage.



\---



\# Expected Local Storage



FASTQ files



C:\\MaligPx\\data\\raw\\peng2019\\fastq\\



Repository metadata



C:\\MaligPx\\data\\raw\\peng2019\\metadata\\



Generated count matrices



C:\\MaligPx\\data\\processed\\peng2019\\



Velocity outputs



C:\\MaligPx\\data\\velocity\\peng2019\\



Intermediate preprocessing files



C:\\MaligPx\\data\\intermediate\\peng2019\\



\---



\# Quality-Control Tracking



The following information will be recorded for every sequencing run after preprocessing.



\- Total sequencing reads

\- Number of detected cells

\- Number of detected genes

\- Median UMIs per cell

\- Median genes per cell

\- Percentage mitochondrial RNA

\- Number of filtered cells

\- Number of retained cells

\- Doublet detection summary

\- Ambient RNA correction status

\- Batch assignment

\- RNA velocity compatibility

\- Final inclusion status



\---



\# Notes



At the current project stage, no biological data have been downloaded. This document establishes the structure that will receive sample-level metadata throughout MD-2, beginning with FASTQ acquisition and continuing through preprocessing, quality control, matrix generation, RNA velocity preparation, and integration into the unified MaligPx analytical dataset.

