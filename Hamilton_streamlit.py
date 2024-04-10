import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Lewis Hamilton F1 Race Stats")

url = "https://raw.githubusercontent.com/jessahal/Hamilton-app/main/hamilton_stats.csv"

ham_df = pd.read_csv(url)

tab1, tab2 = st.tabs(['Mercedes', 'McLaren'])

with tab1:
    merc_data = ham_df[ham_df['Team'] == "Mercedes"]
    merc_fig = sns.lineplot(data = merc_data, x = "Date", y = 'Position', palette = 'turquoise')

    # Flip the y-axis so higher positions are at the top 
    merc_fig.gca().invert_yaxis()
    merc_fig.ylim(1, 25)
    merc_fig.title("Hamilton's Races over the Years")
    merc_fig.legend(loc = (1.01, 0))
    merc_fig.subplots_adjust(right=0.8);  # Increase the right margin to make room for the legend
    st.header(f'Team {tab1}')
    st.plotly_chart(merc_fig)

with tab2:
    mclar_data = ham_df[ham_df['Team'] == "McLaren"]
    mclar_fig = sns.lineplot(data = mclar_data, x = "Date", y = 'Position', palette = 'orange')

    # Flip the y-axis so higher positions are at the top 
    mclar_fig.gca().invert_yaxis()
    mclar_fig.ylim(1, 25)
    mclar_fig.title("Hamilton's Races over the Years")
    mclar_fig.legend(loc = (1.01, 0))
    mclar_fig.subplots_adjust(right=0.8);  # Increase the right margin to make room for the legend
    st.header(f'Team {tab2}')
    st.plotly_chart(mclar_fig)