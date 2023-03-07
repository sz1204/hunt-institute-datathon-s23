import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sleep Visual", page_icon=":books:", layout="wide")

st.header("Data Correlation Visualization")

st.image("Sleep vs. Grad.jpeg", width=100)

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