import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* =====================================
       GLOBAL APP STYLING
    ===================================== */

    .stApp {
        background-color: #F4F6F8;
    }

    /* =====================================
       PAGE HEADERS
    ===================================== */

    .main-header {
        font-size: 36px;
        font-weight: 700;
        color: #2E7D32;
        margin-bottom: 20px;
    }

    .section-header {
        font-size: 24px;
        font-weight: 600;
        color: #1B5E20;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* =====================================
       CUSTOM CARDS
    ===================================== */

    .custom-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 15px;
        transition: 0.3s;
    }

    .custom-card:hover {
        transform: translateY(-3px);
        box-shadow: 0px 6px 15px rgba(0,0,0,0.12);
    }

    /* =====================================
       KPI CARDS
    ===================================== */

    .kpi-card {
        background: white;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    }

    /* =====================================
       STATUS BADGES
    ===================================== */

    .pending {
        background-color: #FFC107;
        color: black;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
    }

    .progress {
        background-color: #2196F3;
        color: white;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
    }

    .completed {
        background-color: #4CAF50;
        color: white;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
    }

    /* =====================================
       SIDEBAR
    ===================================== */

    section[data-testid="stSidebar"] {
        background-color: #2E7D32;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* =====================================
       BUTTONS
    ===================================== */

    .stButton > button {
        background-color: #2E7D32;
        color: white;
        border-radius: 10px;
        border: none;
        width: 100%;
        height: 45px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #1B5E20;
        color: white;
    }

    /* =====================================
       TABLES
    ===================================== */

    .dataframe {
        border-radius: 10px;
    }

    /* =====================================
       SUCCESS ALERT
    ===================================== */

    .success-box {
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
    }

    /* =====================================
       FOOTER
    ===================================== */

    .footer {
        text-align: center;
        color: gray;
        margin-top: 50px;
        padding-top: 20px;
        font-size: 14px;
    }

    /* =====================================
       METRICS
    ===================================== */

    div[data-testid="metric-container"] {
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    }

    /* =====================================
       FORM ELEMENTS
    ===================================== */

    .stTextInput,
    .stTextArea,
    .stSelectbox,
    .stDateInput {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True)