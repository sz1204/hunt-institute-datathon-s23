import streamlit as st
import pandas as pd
import altair as alt

data15 = pd.read_csv("cleaned-data/data_2015.csv")
data16 = pd.read_csv("cleaned-data/data_2016.csv")
data17 = pd.read_csv("cleaned-data/data_2017.csv")
data18 = pd.read_csv("cleaned-data/data_2018.csv")
data19 = pd.read_csv("cleaned-data/data_2019.csv")
data20 = pd.read_csv("cleaned-data/data_2020.csv")
data21 = pd.read_csv("cleaned-data/data_2021.csv")
data22 = pd.read_csv("cleaned-data/data_2022.csv")

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Homepage", page_icon=":books:", layout="wide")

st.image("assets/hunt-institute.jpg", width=100)

st.title("Welcome to the Steminists' Hunt Institute Datathon 2023 dashboard!")
st.markdown("Our project focused on measuring how certain legislation affecting affordable housing and youth mental health impacted student physical health, mental health, and graduation.")
st.markdown('   ')


# Sidebar
st.sidebar.title("Please Filter Here")
# demographic = st.sidebar.radio() # Filter side bars through urban-rural density
#density = st.sidebar.multiselect(
#    "Select the Density:",
#    options=df[""].unique()
#)
# health = st.sidebar.radio() # Filter side bars through type of healthcare - physical or mental



# Creating bar charts for graduation rate per county
df = data15[['County', 'Graduation Rate', '% Rural']]
bar_chart = alt.Chart(df).mark_bar(color='orange').encode(
    x='County',
    y='Graduation Rate'
)
# Create a line chart for % Rural using Altair
line_chart = alt.Chart(df).mark_line(color='blue').encode(
    x='County',
    y='% Rural'
)
# Overlay the two charts
chart = (bar_chart + line_chart)
st.altair_chart(chart, use_container_width=True)


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