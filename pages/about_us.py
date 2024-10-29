import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd
import matplotlib as mt
from misc.about_us_text import temp_text

st.markdown(
    """
    <style>
        .column
        {
            text-align: end;
        } 
    </style>
    """, unsafe_allow_html=True
)


def about_us():
    
    st.title("About Us")

    col1, col2, col3, = st.columns(3)
    col4, col5, col6, = st.columns(3)

    with st.container(border=True, height=None):
        col1.write("column 1")
        col2.write("column 2")
        col3.write("column 3")
        col1.write(temp_text)

    with st.container():
        col4.write("column 1")
        col5.write("column 2")
        col6.write("column 3")

    # col1.write(longmessage)
