
import streamlit as st
import pandas as pd

# Load the Excel data
excel_data = pd.read_excel("path_to_your_excel_file.xlsx")

st.subheader("Premium")
filtered_data = excel_data[excel_data['Condition'] == 'Premium']
st.write(filtered_data)

def app():

import streamlit as st
import pandas as pd

# Load the Excel data
excel_data = pd.read_excel("path_to_your_excel_file.xlsx")

st.subheader("Premium")
filtered_data = excel_data[excel_data['Condition'] == 'Premium']
st.write(filtered_data)
