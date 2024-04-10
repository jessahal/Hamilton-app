import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Lewis Hamilton F1 Race Stats")
st.markdown("""
## Description
The purpose of this app is to explore the stats of one of the greatest Formula 1 Drivers of all time: Lewis Hamilton.
Users can...
    - Explore different years of Hamilton's career
    - See stats on Hamilton's top 5 races of each season
    - Some more stuff that hasn't been decided yet lol
            """)

url = "https://raw.githubusercontent.com/jessahal/Hamilton-app/main/hamilton_stats.csv"

ham_df = pd.read_csv(url)

tab1, tab2 = st.tabs(['McLaren', 'Mercedes'])

with tab1:
    mclar_data = ham_df[ham_df['Team'] == "McLaren"]
    mclar_fig = px.line(mclar_data, x="Date", y='Position', title="Hamilton's Races over the Years")
    mclar_fig.update_traces(line_color = "orange")
    mclar_fig.update_yaxes(autorange="reversed")  # Flip y-axis range
    start_year = mclar_data['Season'].min()
    end_year = mclar_data['Season'].max()
    st.header(f'Team McLaren: {start_year}-{end_year}')
    st.plotly_chart(mclar_fig)  # Display the Plotly chart using st.plotly_chart

with tab2:
    merc_data = ham_df[ham_df['Team'] == "Mercedes"]
    merc_fig = px.line(merc_data, x="Date", y='Position', title="Hamilton's Races over the Years")
    merc_fig.update_traces(line_color = "turquoise")
    merc_fig.update_yaxes(autorange="reversed")  # Flip  y-axis range
    start_year = merc_data['Season'].min()
    end_year = merc_data['Season'].max()
    st.header(f'Team Mercedes: {start_year}-{end_year}')
    st.plotly_chart(merc_fig)  # Display the Plotly chart using st.plotly_chart

with st.sidebar:
    year = st.slider('Choose a year', 2007, 2024)
    st.header(f'Top Races of {year}')
    st.sidebar.markdown("*Speed in MPH")

    year_df = ham_df[ham_df['Season']==year]

    races = year_df.sort_values('Position', ascending=True).head(5)
    races = races.reset_index(drop = True)
    races.index += 1
    st.dataframe(races[['Race', 'Position', 'Time', 'Avg Speed']])
    
    with st.expander("See explanation on Time"):
        st.write("""
            If Hamilton was P1, 'Time' represents his total race time. 
            Otherwise, it's the time between him and P1, usually represented in seconds.
                 """)