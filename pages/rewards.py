import streamlit as st
import pandas as pd

from database.db import (
    get_leaderboard
)


def show_rewards(user):

    st.title(
        "🏆 Rewards & Leaderboard"
    )

    points = user["points"]

    if points < 100:
        level = "Beginner"

    elif points < 300:
        level = "Green Warrior"

    elif points < 700:
        level = "Eco Champion"

    else:
        level = "Sustainability Hero"

    st.metric(
        "Total Points",
        points
    )

    st.metric(
        "Current Level",
        level
    )

    progress = min(
        points / 700,
        1.0
    )

    st.progress(progress)

    st.subheader(
        "Leaderboard"
    )

    leaders = get_leaderboard()

    df = pd.DataFrame(
        [
            dict(row)
            for row in leaders
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )