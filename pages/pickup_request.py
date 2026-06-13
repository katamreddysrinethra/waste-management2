import streamlit as st
import os
from uuid import uuid4

from database.db import create_pickup_request


def show_pickup_request(user):

    st.title(
        "♻️ Request Waste Pickup"
    )

    with st.form("pickup_form"):

        waste_type = st.selectbox(
            "Waste Type",
            [
                "Plastic",
                "Paper",
                "Glass",
                "Metal",
                "Food Waste",
                "E-Waste",
                "Hazardous Waste"
            ]
        )

        quantity = st.number_input(
            "Quantity (kg)",
            min_value=1.0
        )

        address = st.text_area(
            "Address"
        )

        pickup_date = st.date_input(
            "Pickup Date"
        )

        notes = st.text_area(
            "Additional Notes"
        )

        image = st.file_uploader(
            "Upload Waste Image",
            type=["png", "jpg", "jpeg"]
        )

        submit = st.form_submit_button(
            "Submit Request"
        )

    if submit:

        image_path = ""

        if image:

            os.makedirs(
                "assets/uploads",
                exist_ok=True
            )

            filename = (
                str(uuid4())
                + "_"
                + image.name
            )

            image_path = (
                f"assets/uploads/{filename}"
            )

            with open(
                image_path,
                "wb"
            ) as f:
                f.write(image.getbuffer())

        create_pickup_request(
            user["id"],
            waste_type,
            quantity,
            address,
            str(pickup_date),
            image_path,
            notes
        )

        st.success(
            "Pickup Request Submitted Successfully"
        )