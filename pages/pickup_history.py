import streamlit as st
import pandas as pd

from database.db import get_user_pickups


st.markdown(
    """
    <div class="custom-card">
    <h3>📋 Pickup History</h3>
    <p>View and track all your waste collection requests.</p>
    </div>
    """,
    unsafe_allow_html=True
)
def show_pickup_history(user):

    st.title(
        "📋 Pickup History"
    )

    pickups = get_user_pickups(
        user["id"]
    )

    if not pickups:

        st.warning(
            "No Pickup Requests Found"
        )

        return

    df = pd.DataFrame(
        [
            dict(row)
            for row in pickups
        ]
    )

    waste_filter = st.selectbox(
        "Filter by Waste Type",
        ["All"]
        + list(
            df["waste_type"].unique()
        )
    )

    status_filter = st.selectbox(
        "Filter by Status",
        ["All"]
        + list(
            df["status"].unique()
        )
    )

    if waste_filter != "All":

        df = df[
            df["waste_type"]
            == waste_filter
        ]

    if status_filter != "All":

        df = df[
            df["status"]
            == status_filter
        ]

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(
        index=False
    )

    st.download_button(
        "⬇ Download CSV",
        csv,
        "pickup_history.csv",
        "text/csv"
    )