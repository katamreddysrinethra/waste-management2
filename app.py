import streamlit as st  # type: ignore

from database.db import initialize_database
from utils.auth import register_user
from utils.auth import login_user

from pages.dashboard import show_dashboard
from pages.pickup_request import show_pickup_request
from pages.pickup_history import show_pickup_history

from pages.complaints import show_complaints
# Import smart bin locator safely: some environments (static analysis/test) may not have the module.
try:
    import importlib

    smart_bin_locator = importlib.import_module("pages.smart_bin_locator")
    show_bin_locator = smart_bin_locator.show_bin_locator
except Exception:
    # Fallback if the module can't be imported
    def show_bin_locator(*_args, **_kwargs):
        import streamlit as st  # type: ignore
        st.warning("Smart Bin Locator is unavailable.")
from pages.environmental_impact import show_environmental_impact

from pages.marketplace import show_marketplace
from pages.education import show_education
from pages.admin_analytics import show_admin_analytics
from pages.collector_dashboard import show_collector_dashboard
from pages.rewards import show_rewards

initialize_database()

st.set_page_config(
    page_title="EcoCycle",
    page_icon="♻️",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

# -------------------
# LOGIN
# -------------------

if not st.session_state.logged_in:

    st.title(
        "♻️ EcoCycle"
    )

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    with tab1:

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = login_user(
                email,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.user = dict(user)

                st.rerun()

            else:

                st.error(
                    "Invalid Credentials"
                )

    with tab2:

        name = st.text_input(
            "Name"
        )

        reg_email = st.text_input(
            "Register Email"
        )

        reg_password = st.text_input(
            "Register Password",
            type="password"
        )

        role = st.selectbox(
            "Role",
            [
                "Citizen",
                "Waste Collector",
                "Recycler"
            ]
        )

        if st.button(
            "Create Account"
        ):

            success = register_user(
                name,
                reg_email,
                reg_password,
                role
            )

            if success:

                st.success(
                    "Account Created"
                )

            else:

                st.error(
                    "Email Exists"
                )

# -------------------
# MAIN APP
# -------------------

else:

    user = st.session_state.user

    page = None

    with st.sidebar:

        st.title("♻️ EcoCycle")

        st.write(user["full_name"])
        st.write(user["role"])

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()

        # Role-specific navigation
        
        if user["role"] == "Citizen":
            page = st.radio(
                "Navigation",
                [
                    "Dashboard",
                    "Request Pickup",
                    "Pickup History",
                    "Rewards",
                    "Complaints",
                    "Environmental Impact",
                    "Smart Bin Locator",
                    "Education Hub",
                ],
            )

        elif user["role"] == "Waste Collector":
            page = st.radio(
                "Navigation",
                [
                    "Collector Dashboard",
                    "Marketplace",
                ],
            )

        else:
            page = st.radio(
                "Navigation",
                [
                    "Dashboard",
                    "Complaints",
                    "Analytics",
                ],
            )
        st.write("DEBUG PAGE=", page)
        if page == "Dashboard":
            show_dashboard(user)
        elif page == "Request Pickup":
            show_pickup_request(user)

        elif page == "Pickup History":
            show_pickup_history(user)

        elif page == "Collector Dashboard":
            show_collector_dashboard(user)

        elif page == "Complaints":
            show_complaints(user)

        elif page == "Environmental Impact":
            show_environmental_impact(user)

        elif page == "Smart Bin Locator":
            show_bin_locator()
        elif page == "Rewards":
            show_rewards(user)
        elif page == "Marketplace":
            show_marketplace(user)
        elif page == "Education Hub":
            show_education()
        elif page == "Analytics":
            show_admin_analytics()
            from utils.styles import load_css

load_css()
