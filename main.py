import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd
import matplotlib as mt
import pages as pg
from styles.nav_bar_styles import styles


st.set_page_config(initial_sidebar_state="collapsed",
                   layout="wide",
                   page_title="Discover Spending Tracker",
                   page_icon="images/top_logo.svg",
                   )

with open("styles/source.html", "r") as file:
    html_style = file.read()
st.html(html_style)

page = st_navbar(["Dashboard", "Spending Score", "Spending Tracker", "About Us"],
                 styles=styles, logo_page="Dashboard", logo_path="images/logo_white.svg")

if page == "Dashboard":
    pg.dashboard()
if page == "Spending Score":
    pg.spending_score()
if page == "Spending Tracker":
    pg.spending_tracker()
if page == "About Us":
    pg.about_us()
