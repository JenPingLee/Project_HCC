# 把model 設計成streamlit app (offline)
## reference: 
## https://github.com/dataprofessor/code/blob/master/streamlit/part3/penguins-app.py

### ['SERPINA7', 'KRT23', 'F9', 'ALDOB', 'SLC10A1', 'MT2A', 'SPP1', 'CYP1A1', 'S100P', 'PIGR', 'PGC', 'DLK1', 'AGXT', 'ACSL4', 'HGFAC', 'APOA4', 'DEFB1', 'S100A14', 'LGALS4', 'CES1']
gene_ls = ['AKR1D1', 'TIPARP', 'CYP3A4', 'HSD17B10', 'HSD17B8', 'AKR1C4',
'PPARGC1A', 'CYP19A1', 'SPP1', 'HSD17B3', 'ADM', 'SGPL1', 'HSD17B6',
'CYP17A1', 'SCARB1', 'SRD5A1', 'HSD17B11', 'WNT4', 'ESR1', 'HSD17B4','HSD3B1', 
'DHRS9', 'SHH', 'HSD3B2', 'PLEKHA1', 'SRD5A2']


# import time
import streamlit as st
import numpy as np
import pandas as pd



# st.title('測試版(accuracy = 0.91')
st.markdown("# HCC subgroup classifier")
st.markdown("> This classifier allows you to identify HCC subgroups based on the expression of 26 genes involved in androgen metabolic process pathway. You can choose to upload a csv file for multiple samples or manually input values for single sample.")
st.markdown("---")

st.sidebar.markdown("# Data Input")
st.sidebar.subheader("Multiple samples")

