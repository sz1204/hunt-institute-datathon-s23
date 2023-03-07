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


merged_data = pd.merge(data16, data22, on="Insufficient Sleep", suffixes=("_2016", "_2022"))

# create a scatter plot using Altair
scatter_plot = alt.Chart(merged_data).mark_circle(size=60).encode(
    x="% Insufficient Sleep_2016",
    y="% Insufficient Sleep_2022",
    tooltip=["County", "% Insufficient Sleep_2016", "% Insufficient Sleep_2022"]
).interactive()

# display the scatter plot using Streamlit
st.altair_chart(scatter_plot, use_container_width=True)


primary_color = "#bf293c"
secondary_color = "#3a3d7f"
text_color = "#37393e"

# Add CSS to customize text colors
st.markdown(f"""
    <style>
        div.css-edivx2.e16fv1kl3 {{
            color: {secondary_color};
        }}
        p {{
            color: {text_color};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {primary_color};
        }}
    </style>
""", unsafe_allow_html=True)