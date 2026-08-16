\#This .md file will contain the parameters used for relevant analyses.



|**Parameter**|**Primary**|**Sensitivity**|**Reason**|
|-|-|-|-|
|Highly variable genes (HVGs)|3000|2000; 5000|Prespecified|
|scVI latent dimensions|50|30; 75|Prespecified|
|kNN (k-nearest-neighbor) neighbors|30|15; 50|Prespecified|
|CellRank(b) <br />> How sharply CellRank switches from allowing to penalizing backward transitions|10|None|Fixed CellRank parameter|
|CellRank(ν)<br />> How the penalty curve is shaped|0.5|None|Fixed CellRank parameter|
|Generalized Perron Cluster-Cluster Analysis|2-6|-|Prespecified model-selection range|



\## CellRank Parameters



\### Backward-transition threshold 10 (b)



The CellRank parameter (b) controls the thresholding behavior applied to

backward transition probabilities in the transition matrix construction.

The primary value is fixed at b = 10.



No sensitivity analysis is prespecified for b.



\### Transition-kernel exponent (v)



The CellRank parameter (v, or Greek nu) controls the shape of the transition-kernel

weighting function. The primary value is fixed at v.



No sensitivity analysis is prespecified for v.



\## GPCCA



Generalized Perron Cluster-Cluster Analysis (GPCCA) is used to coarse-grain

the cell-level transition matrix into macrostates. The number of macrostates

(K) is evaluated over the prespecified range of 2–6.



\## Sensitivity Analysis



Sensitivity analyses are performed only for parameters with explicitly

prespecified alternative values in this table. CellRank (b) and (v)

remain fixed in the primary and sensitivity workflows and are therefore not

treated as sensitivity parameters.

