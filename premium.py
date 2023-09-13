
import streamlit as st
import pandas as pd

def app():
    st.title("Premium")
    
    # Load the data (this should be adjusted to your data loading method)
    excel_data = pd.read_excel("path_to_your_excel_file.xlsx")

    filtered_data = excel_data[excel_data['Condition'] == 'Premium']
    st.write(filtered_data)
