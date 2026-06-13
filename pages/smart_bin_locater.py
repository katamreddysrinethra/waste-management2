import streamlit as st
import importlib


def show_bin_locator():

    st.title(
        "🗺 Smart Bin Locator"
    )

    if importlib.util.find_spec("folium") is None:
        st.error("Folium is not installed. Install it to view the smart bin locator map.")
        return

    folium = importlib.import_module("folium")

    try:
        st_folium = importlib.import_module("streamlit_folium").st_folium
    except ModuleNotFoundError:
        st.error("streamlit_folium is not installed. Install it to view the smart bin locator map.")
        return

    m = folium.Map(
        location=[17.3850,78.4867],
        zoom_start=10
    )

    locations = [

        {
            "name":"Central Recycling Hub",
            "lat":17.40,
            "lon":78.49,
            "type":"Plastic, Paper, Glass"
        },

        {
            "name":"E-Waste Center",
            "lat":17.38,
            "lon":78.47,
            "type":"Electronics"
        },

        {
            "name":"Metal Collection Point",
            "lat":17.42,
            "lon":78.50,
            "type":"Metal"
        }
    ]

    for loc in locations:

        folium.Marker(
            [loc["lat"],loc["lon"]],
            popup=
            f"""
            {loc['name']}
            <br>
            {loc['type']}
            """
        ).add_to(m)

    st_folium(
        m,
        width=900,
        height=500
    )