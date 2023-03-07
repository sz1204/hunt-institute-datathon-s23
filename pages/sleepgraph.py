import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

data15 = pd.read_csv("cleaned-data/data_2015.csv")
data16 = pd.read_csv("cleaned-data/data_2016.csv")
data17 = pd.read_csv("cleaned-data/data_2017.csv")
data18 = pd.read_csv("cleaned-data/data_2018.csv")
data19 = pd.read_csv("cleaned-data/data_2019.csv")
data20 = pd.read_csv("cleaned-data/data_2020.csv")
data21 = pd.read_csv("cleaned-data/data_2021.csv")
data22 = pd.read_csv("cleaned-data/data_2022.csv")

link = "https://raw.githubusercontent.com/sz1204/hunt-institute-datathon-s23/main/cleaned-data/data_16"

st.set_page_config(page_title="Sleep Visual", page_icon=":books:", layout="wide")

s = "% Insufficient Sleep"

dfs = []

for i in range(15,23):
    df = pd.read_csv(link+str(i)+".csv")
    county_list = ["Cherokee", "Graham", "Clay", "Polk", "Yancey", "Alleghany", "Caswell", "Warren", "Greene", "Bladen", "Hyde", "Tyrrell"]
    county_list = ["Buncombe", "Gaston", "Cabarrus", "Catawba", "Guilford", "Alamance", "Orange", "Cumberland"]
    county_list = ["Mecklenburg", "Forsyth", "Durham", "Wake", "New Hanover"]
    county_list = ['Alexander', 'Anson', 'Ashe', 'Avery', 'Beaufort', 'Bertie', 'Brunswick', 'Burke', 'Caldwell', 'Camden', 'Carteret', 'Chatham', 'Chowan', 'Cleveland', 'Columbus', 'Craven', 'Currituck', 'Dare', 'Davidson', 'Davie', 'Duplin', 'Edgecombe', 'Franklin', 'Gates', 'Granville', 'Halifax', 'Harnett', 'Haywood', 'Henderson', 'Hertford', 'Hoke', 'Iredell', 'Jackson', 'Johnston', 'Jones', 'Lee', 'Lenoir', 'Lincoln', 'Macon', 'Madison', 'Martin', 'McDowell', 'Mitchell', 'Montgomery', 'Moore', 'Nash', 'Northampton', 'Onslow', 'Pamlico', 'Pasquotank', 'Pender', 'Perquimans', 'Person', 'Pitt', 'Randolph', 'Richmond', 'Robeson', 'Rockingham', 'Rowan', 'Rutherford', 'Sampson', 'Scotland', 'Stanly', 'Stokes', 'Surry', 'Swain', 'Transylvania', 'Union', 'Vance', 'Washington', 'Watauga', 'Wayne', 'Wilkes', 'Wilson', 'Yadkin']
    # create a boolean mask to filter the rows in the dataframe
    mask = df["County"].isin(county_list)

    # apply the mask to the dataframe
    filtered_df = df[mask]
    dfs.append(filtered_df)


counties = []

for i in dfs:
    counties.append(i[s].tolist())


import matplotlib.pyplot as plt

original_list = counties
transposed_list = list(zip(*original_list))

print(original_list)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transposed_list)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


# Loop through each sub-list in the main list and plot it as a line
for line in transposed_list:
    plt.plot(line)


# Set the axis labels and title
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Line Chart')

# Display the chart
plt.show()