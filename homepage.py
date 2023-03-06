import streamlit as st
import pandas as pd
import altair as alt
<<<<<<< HEAD
=======
import matplotlib.pyplot as plt
>>>>>>> 37e69edd2daccf595329e905817cc07764ca84ad

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
# health = st.sidebar.radio() # Filter side bars through type of healthcare - physical or mental

files = ["data{}.csv".format(year) for year in range(2015, 2023)]

# create a sidebar select to choose the year
selected_year = st.sidebar.selectbox("Select a year", range(2015, 2023))

# read the selected CSV file based on the selected year
data = pd.read_csv(files[selected_year - 2015])

# create a bar chart based on the % of severe housing problems
fig, ax = plt.subplots()
ax.bar(data['County'], data['% of severe housing problems'])
ax.set_xlabel("County")
ax.set_ylabel("% of severe housing problems")
ax.set_title("Severe Housing Problems in {}".format(selected_year))
st.pyplot(fig)

# Creating bar charts for graduation rate per county
df = data15[['County', 'Graduation Rate', '% Severe Housing Problems']]
bar_chart = alt.Chart(df).mark_bar(color='primary_color').encode(
    x='County',
    y='Graduation Rate'
)
# Create a line chart for % Rural using Altair
line_chart = alt.Chart(df).mark_line(color='secondary_color').encode(
    x='County',
    y='% Severe Housing Problems'
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