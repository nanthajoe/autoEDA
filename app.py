import numpy as np 
import pandas as pd 
import streamlit as st 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from io import StringIO

from detect_delimiter import detect

st.markdown('''

# Exploratory Data Analysis
            
Ini adalah **Aplikasi EDA** dibuat pada Streamlit menggunakan library **YData**.
            
**Credit:** [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) + [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)] + ![detect-delimiter](https://img.shields.io/badge/detect--delimiter-gray?style=flat) oleh [Anantha Yullian Sukmadewa](https://github.com/nanthajoe)
            
---
''')

with st.sidebar.header('1. Unggah file CSV Anda'):
    uploaded_file = st.sidebar.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    # @st.cache_data
    def load_csv():
        f = StringIO(uploaded_file.getvalue().decode("utf-8"))
        firstline = f.readline()
        delimiter = detect(firstline, whitelist=[',', ';', ':', '|', '\t', '"'])
        csv = pd.read_csv(uploaded_file, sep=delimiter, engine='python')
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**YData Report**')
    st_profile_report(pr)
else:
    st.info('Menunggu file CSV untuk diunggah')
    if st.button('Tekan untuk menggunakan Dataset Sementara'):
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns = ['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**YData Profiling Report**')
        st_profile_report(pr)