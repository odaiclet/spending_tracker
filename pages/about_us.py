import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd
import matplotlib as mt
from .misc.descriptions import personalDescription


def about_us():

    st.title("About Us")
    col1, col2, col3, = st.columns(3)

    with st.container():
        
        col1.image("images/Placeholder_Profile_Pic.svg", use_column_width=True)
        col1.markdown(f"<div style='text-align: center;'>{personalDescription}</div>", unsafe_allow_html=True)
        col2.image("images/Placeholder_Profile_Pic.svg", use_column_width=True)
        col2.markdown(f"<div style='text-align: center;'>{personalDescription}</div>", unsafe_allow_html=True)
        col3.image("images/Placeholder_Profile_Pic.svg", use_column_width=True)
        col3.markdown(f"<div style='text-align: center;'>{personalDescription}</div>", unsafe_allow_html=True)

    # col1.write("bottomDesc") #placeholder
