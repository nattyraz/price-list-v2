
import streamlit as st
from pages import neuf_remanufacture, refurb, premium

st.set_page_config(
    page_title="Multipage App",
    page_icon="🚀",
)

PAGES = {
    "neuf & remanufacturé": neuf_remanufacture,
    "refurb": refurb,
    "Premium": premium,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
