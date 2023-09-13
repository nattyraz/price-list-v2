
import streamlit as st
from pages import neuf_remanufacture, refurb, premium  # Assuming the pages are named this way

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Create a dict to hold the pages and their titles
PAGES = {
    "Welcome to Streamlit! 👋": None,
    "neuf & remanufacturé": neuf_remanufacture,
    "refurb": refurb,
    "Premium": premium
}

# Sidebar content
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Page navigation logic
if selection == "Welcome to Streamlit! 👋":
    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")
    st.markdown(
        '''
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
            forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
            Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    '''
    )
else:
    page = PAGES[selection]
    page.app()  # Assuming each page has an 'app' function to run its content
