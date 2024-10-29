import streamlit as st

def set_app_config():
    st.set_page_config(
        initial_sidebar_state="collapsed",
        layout="wide",
        page_title="Discover Spending Tracker",
        page_icon="images/syntax_society_logo_only.svg"
    )