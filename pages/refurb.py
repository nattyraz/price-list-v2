
import streamlit as st
import pandas as pd

# Load the Excel data
excel_data = pd.read_excel("path_to_your_excel_file.xlsx")

st.subheader("refurb")
grade_options = ['Grade A', 'Grade B', 'Grade C', 'Defekt', '08 Ref.', '04 Demo']
selected_grade = st.multiselect("Select Grade", grade_options)
if selected_grade:
    filtered_data = excel_data[excel_data['Condition'].isin(selected_grade)]
    st.write(filtered_data)

def app():

import streamlit as st
import pandas as pd

# Load the Excel data
excel_data = pd.read_excel("path_to_your_excel_file.xlsx")

st.subheader("refurb")
grade_options = ['Grade A', 'Grade B', 'Grade C', 'Defekt', '08 Ref.', '04 Demo']
selected_grade = st.multiselect("Select Grade", grade_options)
if selected_grade:
    filtered_data = excel_data[excel_data['Condition'].isin(selected_grade)]
    st.write(filtered_data)
