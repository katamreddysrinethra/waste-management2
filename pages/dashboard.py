import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import get_user_pickups


def show_dashboard(user):

    st.title("📊 EcoCycle Dashboard")

    pickups = get_user_pickups(user["id"])

    total_pickups = len(pickups)

    total_waste = sum(
        row["quantity"]
        for row in pickups
    ) if pickups else 0

    total_points = user["points"]

    co2_saved = round(
        total_waste * 1.5,
        2
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Waste",
        f"{total_waste} kg"
    )

    col2.metric(
        "Pickups",
        total_pickups
    )

    col3.metric(
        "Points",
        total_points
    )

    col4.metric(
        "CO₂ Saved",
        f"{co2_saved} kg"
    )

    if pickups:

        df = pd.DataFrame(
            [
                dict(row)
                for row in pickups
            ]
        )

        fig = px.pie(
            df,
            names="waste_type",
            title="Waste Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader(
            "Recent Pickups"
        )

        st.dataframe(df)

    else:

        st.info(
            "No pickup requests available."
        )