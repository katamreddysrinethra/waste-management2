# Import streamlit, pandas and plotly lazily inside the function to avoid
# import-time issues in environments where those packages are not installed.
from typing import TYPE_CHECKING, Any

from database.db import (
    execute_query,
    get_leaderboard
)

# Help static analysis / linters understand streamlit is used without importing it at
# module import time in runtime environments where streamlit may be unavailable.
if TYPE_CHECKING:
    import streamlit as st
else:
    st: Any = None  # type: ignore

# Attempt a safe import at module import time so editors/linters don't report a
# missing import. If streamlit isn't available at runtime this will simply set
# `st` to None and the function will try to import it when executed.
# Defer importing streamlit until runtime in show_admin_analytics to avoid
# import-time errors in environments where streamlit is not installed.


def show_admin_analytics():
    # Import runtime dependencies lazily. If streamlit wasn't available at
    # module import time, try to import it now; if still unavailable, exit.
    if st is None:
        try:
            import streamlit as st  # type: ignore
        except Exception:
            # Streamlit not available in this environment; nothing to show.
            return
    import pandas as pd
    import importlib

    try:
        px = importlib.import_module("plotly.express")
    except Exception:
        px = None

    st.title("📈 Admin Analytics")

    users = execute_query(
        "SELECT * FROM users"
    ) or []

    pickups = execute_query(
        "SELECT * FROM pickup_requests"
    ) or []

    total_users = len(users)
    total_pickups = len(pickups)

    total_waste = sum(
        float(p.get("quantity", 0) or 0)
        for p in pickups
    ) if pickups else 0

    completed = len(
        [
            p for p in pickups
            if p.get("status") == "Completed"
        ]
    )

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "Users",
        total_users
    )

    col2.metric(
        "Pickups",
        total_pickups
    )

    col3.metric(
        "Waste Collected",
        f"{total_waste} kg"
    )

    col4.metric(
        "Completed",
        completed
    )

    if pickups:

        df = pd.DataFrame(
            [
                dict(row)
                for row in pickups
            ]
        )

        waste_fig = px.pie(
            df,
            names="waste_type",
            title="Waste Categories"
        )

        st.plotly_chart(
            waste_fig,
            use_container_width=True
        )

        status_fig = px.histogram(
            df,
            x="status",
            title="Pickup Status"
        )

        st.plotly_chart(
            status_fig,
            use_container_width=True
        )

    st.subheader(
        "Top Contributors"
    )

    leaders = get_leaderboard()

    leader_df = pd.DataFrame(
        [
            dict(row)
            for row in leaders
        ]
    )

    st.dataframe(
        leader_df,
        use_container_width=True
    )