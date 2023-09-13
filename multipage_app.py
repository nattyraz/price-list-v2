
import streamlit as st
from pages import neuf_remanufacture, refurb, premium

# Sidebar navigation for the multipage app
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "neuf & remanufacturé", "refurb", "Premium"])

if selection == "Home":
    st.title("Home")
    st.write("Welcome to the multipage application. Please select a page from the sidebar.")
elif selection == "neuf & remanufacturé":
    neuf_remanufacture.app()
elif selection == "refurb":
    refurb.app()
elif selection == "Premium":
    premium.app()
