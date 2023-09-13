
import streamlit as st
from pages import neuf_remanufacture, refurb, premium

# Page configuration
st.set_page_config(
    page_title="Your App Title",
    page_icon="📊",
)

# Sidebar welcome message
st.sidebar.title("Navigation")
st.sidebar.info("Choose a page from the above to navigate.")

# Main content
st.write("# Welcome to Your App! 📊")

# Sidebar links to documentation, etc.
st.sidebar.header("More Information")
st.sidebar.text("You can add more links or info here.")

# Mapping of page functions to their names
PAGES = {
    "Neuf & Remanufacturé": neuf_remanufacture,
    "Refurb": refurb,
    "Premium": premium,
}

# Sidebar selection of page
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# Run the selected page
page = PAGES[selection]
page.app()

