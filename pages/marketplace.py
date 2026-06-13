import streamlit as st
import pandas as pd

from database.db import (
    create_marketplace_listing,
    get_marketplace_items,
    create_transaction
)


def show_marketplace(user):

    st.title("♻ Recycler Marketplace")

    if user["role"] == "Waste Collector":

        st.subheader(
            "Create Listing"
        )

        with st.form("listing"):

            material = st.selectbox(
                "Material",
                [
                    "Plastic",
                    "Paper",
                    "Glass",
                    "Metal",
                    "E-Waste"
                ]
            )

            quantity = st.number_input(
                "Quantity (kg)"
            )

            price = st.number_input(
                "Price"
            )

            description = st.text_area(
                "Description"
            )

            submit = st.form_submit_button(
                "Create Listing"
            )

        if submit:

            create_marketplace_listing(
                material,
                quantity,
                price,
                description,
                user["id"]
            )

            st.success(
                "Listing Added"
            )

    st.subheader(
        "Marketplace Listings"
    )

    items = get_marketplace_items()

    for item in items:

        with st.container():

            st.markdown("---")

            st.markdown(
    f"""
    <div class="custom-card">

    <h4>♻️ {item['material_type']}</h4>

    <p><b>Quantity:</b> {item['quantity']} kg</p>

    <p><b>Price:</b> ₹{item['price']}</p>

    <p>{item['description']}</p>

    </div>
    """,
    unsafe_allow_html=True
)

            

            if user["role"] == "Recycler":

                if st.button(
                    f"Purchase #{item['id']}"
                ):

                    create_transaction(
                        item["id"],
                        user["id"],
                        item["quantity"],
                        item["price"]
                    )

                    st.success(
                        "Purchase Request Sent"
                    )