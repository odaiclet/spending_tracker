import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd
import matplotlib as mt

longmessage = """At DiscoverCard, we believe that financial empowerment begins with understanding your spending habits. Our innovative spending tracker is designed to help you take control of your finances effortlessly.

With our user-friendly interface, you can easily categorize your expenses, set budgets, and track your progress in real time. Whether you're looking to save for a special occasion, pay off debt, or simply gain insight into your daily spending, our tool provides the resources you need to make informed financial decisions.

If you have any questions or conerns, reach out to one of our 3 creators of this project:

Juan: Email

Destiny: Email

Nolan: Email"""
def about_us():
    col1, col2 = st.columns(2)

    col1.title("About Us")
    col1.write(longmessage)