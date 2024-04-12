import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.title("Lewis Hamilton F1 Race Stats")
st.markdown("""
## Welcome to the F1 Lewis Hamilton App!
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
    
    selected_years = st.multiselect('Select years for comparison', ham_df["Season"].unique())

    if selected_years:
        selected_data = ham_df[ham_df['Season'].isin(selected_years)]
    
        # Drop rows with NaN values in 'Position' or 'Avg Speed'
        selected_data = selected_data.dropna(subset=['Position', 'Avg Speed'])
        
        # Group data by 'Season' and calculate the average position and speed
        avg_data = selected_data.groupby('Season').agg({
            'Position': 'mean',
            'Avg Speed': 'mean'
        }).reset_index()
        
        # Rename columns for clarity
        avg_data = avg_data.rename(columns={'Season': 'Year', 'Position': 'Avg Position', 'Avg Speed': 'Avg Speed'})
        avg_data['Year'] = avg_data['Year'].astype(str)
        # Display the average position and average speed for each selected year
        st.header('Average Position and Speed')
        st.dataframe(avg_data)
            
        
# Create the initial box plot for all races
race_fig = px.box(ham_df, x="Race", y="Position", color="Race")
race_fig.update_yaxes(autorange="reversed")
race_fig.update_layout(
    title="Hamilton's Races vs Position",
    xaxis_title="Race",
    yaxis_title="Ending Position",
    xaxis_tickangle=-45
)

# Display the initial box plot using Streamlit
st.plotly_chart(race_fig)

# Create a dropdown menu for selecting a specific race
selected_race = st.selectbox("Select a Race to see Stats", ham_df["Race"].unique())

# Filter the data for the selected race
filtered_data = ham_df[ham_df["Race"] == selected_race]

# Display statistics for the selected race
if not filtered_data.empty:
    mean_position = filtered_data["Position"].mean()
    avg_start = filtered_data["Starting Grid Position"].mean()
    min_position = filtered_data["Position"].min()
    max_position = filtered_data["Position"].max()
    avg_speed = filtered_data["Avg Speed"].dropna().mean()
    race_count = len(filtered_data)

    st.write(f"Race Count: {race_count}")
    st.write(f"Mean Position: {round(mean_position)}")
    st.write(f"Avg Starting Position: {round(avg_start)}")
    st.write(f"Best Position: {min_position}")
    st.write(f"Worst Position: {max_position}")
    st.write(f"Avg Speed: {round(avg_speed, 4)}")
else:
    st.write("No data available for the selected race.")

tab3, tab4, tab5 = st.tabs(['Position', 'Speed', 'Start v End'])

with tab3:
# Create a scatter plot where only the selected race is colored in
    scatter_fig = px.scatter(ham_df, x="Date", y="Position", 
                            color=ham_df["Race"] == selected_race, color_discrete_map={True: 'red', False: 'rgba(128, 128, 128, 0.5)'})
    
    scatter_fig.update_traces(marker=dict(size=12))
    scatter_fig.update_yaxes(autorange="reversed")
    scatter_fig.update_layout(
        title=f"Hamilton's Position over the Years - {selected_race}",
        xaxis_title="Race",
        yaxis_title="Ending Position",
        showlegend= False
    )
    st.plotly_chart(scatter_fig)

with tab4:
    # Create a scatter plot where only the selected race is colored in
    scatter_fig = px.scatter(ham_df, x="Date", y="Avg Speed", 
                            color=ham_df["Race"] == selected_race, color_discrete_map={True: 'red', False: 'rgba(128, 128, 128, 0.5)'})
    scatter_fig.update_traces(marker=dict(size=12))
    scatter_fig.update_layout(
        title=f"Hamilton's Speed Bver the Years - {selected_race}",
        xaxis_title="Race",
        yaxis_title="Ending Position",
        showlegend= False
    )
    st.plotly_chart(scatter_fig)

with tab5:
    st.write("""This graph shows Hamilton's Starting Grid Position compared to his ending grid position.
                Races where Hamilton started well and finished well are in the top left corner. """)
    scatter_fig = px.scatter(ham_df, x="Starting Grid Position", y="Position", 
                            color=ham_df["Race"] == selected_race, color_discrete_map={True: 'red', False: 'rgba(128, 128, 128, 0.5)'})
    
    scatter_fig.update_traces(marker=dict(size=12))
    scatter_fig.update_yaxes(autorange="reversed")
    scatter_fig.update_layout(
        title=f"Hamilton's Start Position vs End Position - {selected_race}",
        xaxis_title="Starting Grid Position",
        yaxis_title="Ending Position",
        showlegend= False
    )
    st.plotly_chart(scatter_fig)