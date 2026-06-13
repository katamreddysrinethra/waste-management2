import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from database.db import (
    get_user_pickups
)


def show_environmental_impact(
    user
):

    st.title(
        "🌱 Environmental Impact"
    )

    pickups = get_user_pickups(
        user["id"]
    )

    total_waste = sum(
        row["quantity"]
        for row in pickups
    ) if pickups else 0

    co2_saved = round(
        total_waste * 1.5,
        2
    )

    trees_saved = round(
        total_waste / 10,
        1
    )

    landfill_reduction = round(
        total_waste * 0.8,
        2
    )

    col1,col2,col3 = st.columns(3)

    col1.metric(
        "CO₂ Saved",
        f"{co2_saved} kg"
    )

    col2.metric(
        "Trees Equivalent",
        trees_saved
    )

    col3.metric(
        "Landfill Reduction",
        f"{landfill_reduction} kg"
    )

    score = min(
        int(total_waste),
        100
    )

    st.subheader(
        "Sustainability Score"
    )

    st.progress(
        score/100
    )

    chart_df = pd.DataFrame({

        "Metric":[
            "CO₂ Saved",
            "Trees Saved",
            "Landfill Reduction"
        ],

        "Value":[
            co2_saved,
            trees_saved,
            landfill_reduction
        ]
    })

    fig = px.bar(
        chart_df,
        x="Metric",
        y="Value",
        title="Impact Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )