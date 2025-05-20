import streamlit as st
import pandas as pd
import os

# Setup project path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_root, "data", "steelers_season_summary.csv")

# Load CSV
df = pd.read_csv(data_path)

# Streamlit page settings
st.set_page_config(page_title="Steelers Season Summary", layout="wide")

# Tabs layout
tab1, tab2, tab3 = st.tabs(["📊 Season Summary", "📈 Win % Trend", "🤝 Opponent Analysis"])

with tab1:
    st.title("🏈 Pittsburgh Steelers Season Summary")
    st.markdown("Win/loss/tie breakdown and win percentage by season.")

    st.subheader("📋 Full Season Summary Table")
    st.dataframe(df.style.format({"Win%": "{:.2f}"}))

    years = sorted(df["Year"].unique())
    start_year, end_year = st.select_slider("🎚 Select Season Range", options=years, value=(min(years), max(years)))
    filtered_df = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]

    st.subheader("📊 Wins, Losses, and Ties per Season")
    st.bar_chart(filtered_df.set_index("Year")[["W", "L", "T"]])

with tab2:
    st.header("📈 Win Percentage Over Time")
    st.line_chart(df.set_index("Year")["Win%"])

with tab3:
    st.header("🤝 Wins and Losses by Opponent")

    # Load game-level data for opponent analysis
    game_data_path = os.path.join(project_root, "data", "steelers_games_by_year.csv")
    games_df = pd.read_csv(game_data_path)

    is_postseason = st.checkbox("Show only postseason games")
    if is_postseason:
        # Filter by postseason if available (assuming it's marked somehow)
        if "Game Type" in games_df.columns:
            games_df = games_df[games_df["Game Type"] == "POST"]
        else:
            st.warning("No postseason marker found in the dataset.")

    opp_summary = games_df.groupby(["Opponent", "Result"]).size().unstack(fill_value=0)
    st.dataframe(opp_summary)
    st.bar_chart(opp_summary)