import streamlit as st
import pandas as pd
import matplotlib as mt
import pages as pg
st.set_page_config(initial_sidebar_state="collapsed",
                   layout="wide",
                   page_title="Discover Spending Tracker",
                   page_icon="images/syntax_society_logo_only.svg"
                   )
from streamlit_navigation_bar import st_navbar
from styles.nav_bar_styles import styles

# Set up the page configuration


# Top navigation bar setup
page = st_navbar(
    ["Dashboard", "Spending Score", "Spending Tracker", "About Us"],
    styles=styles, logo_page="Dashboard", logo_path="images/syntax_society_logo_only.svg",
    options={"show_menu": True, "show_sidebar": True, "hide_nav": True}
)

# Load the custom HTML styling
with open("styles/source.html", "r") as file:
    html_style = file.read()
st.html(html_style)

# Sidebar navigation using buttons

st.sidebar.image("images/syntax_society_logo.svg", width=None)
with st.sidebar:
    dashboard_button = st.button("Dashboard",)
    spending_score_button = st.button("Spending Score")
    spending_tracker_button = st.button("Spending Tracker")
    about_us_button = st.button("About Us")

if dashboard_button:
    page = "Dashboard"
elif spending_score_button:
    page = "Spending Score"
elif spending_tracker_button:
    page = "Spending Tracker"
elif about_us_button:
    page = "About Us"

# Display the content based on either the navbar or sidebar button click
if page == "Dashboard" or dashboard_button:
    pg.dashboard()
elif page == "Spending Score" or spending_score_button:
    pg.spending_score()
elif page == "Spending Tracker" or spending_tracker_button:
    pg.spending_tracker()
elif page == "About Us" or about_us_button:
    pg.about_us()