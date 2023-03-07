import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sleep Visual", page_icon=":books:", layout="wide")

st.header("Data Correlation Visualization")

st.image("Sleep vs. Grad.jpg", width=500)