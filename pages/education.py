import streamlit as st


def show_education():

    st.title(
        "📚 Education Hub"
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Waste Segregation",
            "Recycling Tips",
            "Composting",
            "Videos"
        ]
    )

    with tab1:

        st.subheader(
            "Waste Segregation"
        )

        st.info(
            """
            Separate waste into:

            • Dry Waste
            • Wet Waste
            • E-Waste
            • Hazardous Waste
            """
        )

    with tab2:

        st.subheader(
            "Recycling Tips"
        )

        st.success(
            """
            • Reuse plastic bottles
            • Recycle newspapers
            • Donate electronics
            """
        )

    with tab3:

        st.subheader(
            "Composting Guide"
        )

        st.write(
            """
            Compost kitchen waste
            to create natural fertilizer.
            """
        )

    with tab4:

        st.video(
            "https://www.youtube.com/watch?v=OasbYWF4_S8"
        )