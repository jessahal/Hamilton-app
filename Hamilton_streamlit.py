import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Lewis Hamilton F1 Race Stats")

url = "https://raw.githubusercontent.com/jessahal/Hamilton-app/main/hamilton_stats.csv"

ham_df = pd.read_csv(url)

tab1, tab2 = st.tabs(['Mercedes', 'McLaren'])

with tab1:
    merc_data = ham_df[ham_df['Team'] == "Mercedes"]
    sns.lineplot(data = merc_data, x = "Date", y = 'Position', palette = 'turquoise')

    # Flip the y-axis so higher positions are at the top 
    plt.gca().invert_yaxis()
    plt.ylim(1, 25)
    plt.title("Hamilton's Races over the Years")
    plt.legend(loc = (1.01, 0))
    plt.subplots_adjust(right=0.8);  # Increase the right margin to make room for the legend

    plt.savefig("Hamilton_races.png")

