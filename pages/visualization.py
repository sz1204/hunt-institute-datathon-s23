import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sleep Visual", page_icon=":books:", layout="wide")

st.header("Data Correlation Visualization")

uploaded_file = st.file_uploader("Sleep vs. Grad", type=[jpeg])

st.image(uploaded_file, width = 200)