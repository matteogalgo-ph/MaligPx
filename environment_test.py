"""
MaligPx Environment Verification
Purpose:
    Verify that the core computational biology environment is correctly
    installed and operational before beginning analysis.
"""

import sys

import scanpy as sc
import scvelo as scv
import cellrank as cr
import anndata as ad

import numpy as np
import pandas as pd
import scipy

import matplotlib
import matplotlib.pyplot as plt

import networkx as nx
import igraph

print("=" * 60)
print("MaligPx Environment Verification")
print("=" * 60)

print(f"Python:      {sys.version.split()[0]}")
print(f"Scanpy:      {sc.__version__}")
print(f"scVelo:      {scv.__version__}")
print(f"CellRank:    {cr.__version__}")
print(f"AnnData:     {ad.__version__}")
print(f"NumPy:       {np.__version__}")
print(f"Pandas:      {pd.__version__}")
print(f"SciPy:       {scipy.__version__}")
print(f"Matplotlib:  {matplotlib.__version__}")
print(f"NetworkX:    {nx.__version__}")
print(f"igraph:      {igraph.__version__}")

print("\nPython executable:")
print(sys.executable)

print("\nEnvironment verification completed successfully.")
