import streamlit as st
import os
from uuid import uuid4

from database.db import (
    create_complaint,
    get_user_complaints,
    get_all_complaints,
    update_complaint_status
)


def show_complaints(user):

    st.title("📢 Complaint Management")

    if user["role"] == "Citizen":

        tab1, tab2 = st.tabs(
            [
                "Submit Complaint",
                "My Complaints"
            ]
        )

        with tab1:

            with st.form("complaint_form"):

                complaint_type = st.selectbox(
                    "Complaint Type",
                    [
                        "Missed Pickup",
                        "Illegal Dumping",
                        "Overflowing Bin",
                        "Service Issue"
                    ]
                )

                title = st.text_input(
                    "Complaint Title"
                )

                description = st.text_area(
                    "Description"
                )

                image = st.file_uploader(
                    "Upload Photo",
                    type=["png","jpg","jpeg"]
                )

                submit = st.form_submit_button(
                    "Submit"
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
                        + image.name
                    )

                    image_path = (
                        f"assets/uploads/{filename}"
                    )

                    with open(
                        image_path,
                        "wb"
                    ) as f:
                        f.write(
                            image.getbuffer()
                        )

                create_complaint(
                    user["id"],
                    complaint_type,
                    title,
                    description,
                    image_path
                )

                st.success(
                    "Complaint Submitted"
                )

        with tab2:

            complaints = get_user_complaints(
                user["id"]
            )

            for complaint in complaints:

                with st.expander(
                    complaint["title"]
                ):

                    st.write(
                        complaint["description"]
                    )

                    st.write(
                        f"Status: {complaint['status']}"
                    )

    elif user["role"] == "Admin":

        st.subheader(
            "All Complaints"
        )

        complaints = get_all_complaints()

        for complaint in complaints:

            st.markdown("---")

            st.write(
                f"ID: {complaint['id']}"
            )

            st.write(
                complaint["title"]
            )

            st.write(
                complaint["description"]
            )

            status = st.selectbox(
                f"Status {complaint['id']}",
                [
                    "Open",
                    "In Progress",
                    "Resolved"
                ]
            )

            if st.button(
                f"Update {complaint['id']}"
            ):

                update_complaint_status(
                    complaint["id"],
                    status
                )

                st.success(
                    "Updated"
                )

                st.rerun()