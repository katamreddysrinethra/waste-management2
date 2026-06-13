import streamlit as st

from database.db import (
    get_pending_pickups,
    assign_pickup,
    get_collector_pickups,
    update_pickup_status
)


def show_collector_dashboard(user):

    st.title(
        "🚛 Collector Dashboard"
    )

    tab1, tab2 = st.tabs(
        [
            "Available Pickups",
            "My Pickups"
        ]
    )

    with tab1:

        pickups = get_pending_pickups()

        if not pickups:

            st.success(
                "No Pending Pickups"
            )

        for pickup in pickups:

            with st.container():

                st.markdown("---")

                st.markdown(
    f"""
    <div class="custom-card">

    <h4>📦 Pickup #{pickup['id']}</h4>

    <p><b>Waste Type:</b> {pickup['waste_type']}</p>

    <p><b>Quantity:</b> {pickup['quantity']} kg</p>

    <p><b>Address:</b> {pickup['address']}</p>

    <p><b>Status:</b> {pickup['status']}</p>

    </div>
    """,
    unsafe_allow_html=True
)

                if st.button(
                    f"Accept #{pickup['id']}"
                ):

                    assign_pickup(
                        pickup["id"],
                        user["id"]
                    )

                    st.success(
                        "Pickup Assigned"
                    )

                    st.rerun()

    with tab2:

        my_pickups = get_collector_pickups(
            user["id"]
        )

        for pickup in my_pickups:

            st.markdown("---")

            st.write(
                f"Request ID: {pickup['id']}"
            )

            st.write(
                f"Status: {pickup['status']}"
            )

            if pickup["status"] == "In Progress":

                if st.button(
                    f"Complete #{pickup['id']}"
                ):

                    update_pickup_status(
                        pickup["id"],
                        "Completed"
                    )

                    st.success(
                        "Completed Successfully"
                    )

                    st.rerun()
