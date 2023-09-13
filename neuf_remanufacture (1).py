
import streamlit as st
import pandas as pd

def app():
    st.title('neuf & remanufacturé')
    excel_data = pd.read_excel("path_to_excel_file.xlsx")
    ref_options = ['GOLD', 'SILVER', 'BRONZE', '01 New', '02 Bulk', 'Demo']
    selected_ref = st.multiselect("Select Reference", ref_options)
    if selected_ref:
        filtered_data = excel_data[excel_data['Condition'].isin(selected_ref)]
        st.write(filtered_data)
