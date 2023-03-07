import streamlit as st
import pandas as pd

data15 = pd.read_csv("cleaned-data/data_2015.csv")
data16 = pd.read_csv("cleaned-data/data_2016.csv")
data17 = pd.read_csv("cleaned-data/data_2017.csv")
data18 = pd.read_csv("cleaned-data/data_2018.csv")
data19 = pd.read_csv("cleaned-data/data_2019.csv")
data20 = pd.read_csv("cleaned-data/data_2020.csv")
data21 = pd.read_csv("cleaned-data/data_2021.csv")
data22 = pd.read_csv("cleaned-data/data_2022.csv")

st.set_page_config(page_title="Sleep Visual", page_icon=":books:", layout="wide")

st.header("Sleep Visual")

data = {"2016":[data16], "2022":[data22]}
 
df = pd.DataFrame(data)
df
st.line_chart(data=df)