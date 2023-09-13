
import streamlit as st
import pandas as pd

def app():
    st.title('Premium')
    excel_data = pd.read_excel("path_to_excel_file.xlsx")
    filtered_data = excel_data[excel_data['Condition'] == 'Premium']
    st.write(filtered_data)
