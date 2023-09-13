
import streamlit as st
import pandas as pd

def app():
    st.title("Neuf & Remanufacturé")
    
    # Load the data (this should be adjusted to your data loading method)
    excel_data = pd.read_excel("path_to_your_excel_file.xlsx")

    ref_options = ['GOLD', 'SILVER', 'BRONZE', '01 New', '02 Bulk', 'Demo']
    selected_ref = st.multiselect("Select Reference", ref_options)
    if selected_ref:
        filtered_data = excel_data[excel_data['Condition'].isin(selected_ref)]
        st.write(filtered_data)
