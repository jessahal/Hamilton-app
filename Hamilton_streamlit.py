import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Lewis Hamilton F1 Race Stats")

url = 'https://github.com/jessahal/Hamilton-app/blob/main/hamilton_stats.csv'

ham_df = pd.read_csv(url)

tab1, tab2 = st.tabs(['Mercedes', 'McLaren'])


