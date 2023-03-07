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

rural_counties = ["Cherokee", "Graham", "Clay", "Polk", "Yancey", "Alleghany", "Caswell", "Warren", "Greene", "Bladen", "Hyde", "Tyrrell"]
mixed_rural_counties = ['Alexander', 'Anson', 'Ashe', 'Avery', 'Beaufort', 'Bertie', 'Brunswick', 'Burke', 'Caldwell', 'Camden', 'Carteret', 'Chatham', 'Chowan', 'Cleveland', 'Columbus', 'Craven', 'Currituck', 'Dare', 'Davidson', 'Davie', 'Duplin', 'Edgecombe', 'Franklin', 'Gates', 'Granville', 'Halifax', 'Harnett', 'Haywood', 'Henderson', 'Hertford', 'Hoke', 'Iredell', 'Jackson', 'Johnston', 'Jones', 'Lee', 'Lenoir', 'Lincoln', 'Macon', 'Madison', 'Martin', 'McDowell', 'Mitchell', 'Montgomery', 'Moore', 'Nash', 'Northampton', 'Onslow', 'Pamlico', 'Pasquotank', 'Pender', 'Perquimans', 'Person', 'Pitt', 'Randolph', 'Richmond', 'Robeson', 'Rockingham', 'Rowan', 'Rutherford', 'Sampson', 'Scotland', 'Stanly', 'Stokes', 'Surry', 'Swain', 'Transylvania', 'Union', 'Vance', 'Washington', 'Watauga', 'Wayne', 'Wilkes', 'Wilson', 'Yadkin']
mixed_urban_counties = ["Buncombe", "Gaston", "Cabarrus", "Catawba", "Guilford", "Alamance", "Orange", "Cumberland"]
urban_counties = ["Mecklenburg", "Forsyth", "Durham", "Wake", "New Hanover"]

density_categories = {
    'Rural': rural_counties,
    'Mixed Rural': mixed_rural_counties,
    'Mixed Urban': mixed_urban_counties,
    'Urban': urban_counties
}

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Homepage", page_icon=":books:", layout="wide")

st.image("assets/hunt-institute.jpg", width=100)

st.title("Welcome to the Steminists' Hunt Institute Datathon 2023 dashboard!")
st.markdown("Our project focused on measuring how certain legislation affecting affordable housing and youth mental health impacted student physical health, mental health, and graduation.")
st.markdown('   ')


# Sidebar
st.sidebar.title("Please Filter Here")
selected_densities = st.sidebar.multiselect('Select population densities', list(density_categories.keys()))
mask = data15['County'].isin(sum([density_categories[d] for d in selected_densities], []))
filtered_data = data15[mask]


merged_data = pd.merge(data15, data22, on="County", suffixes=("_2015", "_2022"))

# create a scatter plot using Altair

merged_data = pd.merge(data16, data22, on='County', suffixes=("_2016", "_2022"))
scatter_plot = alt.Chart(merged_data).mark_circle(size=60).encode(
    x="% Insufficient Sleep_2016",
    y="% Insufficient Sleep_2022",
    tooltip=["County", "% Insufficient Sleep_2016", "% Insufficient Sleep_2022"]
).interactive()

scatterplot = alt.Chart(data22).mark_circle().encode(
    x='% Insufficient Sleep',
    y='Median Household Income',
    tooltip=['County', '% Insufficient Sleep', 'Median Household Income']
).properties(
    width=600,
    height=400,
    title='Relationship between % Insufficient Sleep and Median Household Income'
)

scatterplot = alt.Chart(data22).mark_circle().encode(
    x='% Insufficient Sleep',
    y='% Food Insecure',
    tooltip=['County', '% Insufficient Sleep', '% Food Insecure']
).properties(
    width=600,
    height=400,
    title='Relationship between % Insufficient Sleep and % Food Insecure'
)

# Show the plot using Streamlit
st.altair_chart(scatterplot)


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