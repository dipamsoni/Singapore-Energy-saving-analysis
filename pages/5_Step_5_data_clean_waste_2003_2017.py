import streamlit as st
import pandas as pd


def clean_data_waste_2003_2017(waste_2003_2017):
    st.title("Data Cleaning of Waste 2003 to 2017 data")
    st.info("Original dataframe of waste_2003_2017")
    st.write(waste_2003_2017)

    st.info("As we just want to drop the **{waste_disposed_of_tonne}** column from the dataframe we will just select the rest of the columns or we can use drop command. Here, .loc command used to select necessary columns.")
    clean_waste_03_17 = waste_2003_2017.loc[:,["waste_type", "total_waste_generated_tonne", "total_waste_recycled_tonne", "recycling_rate", "year",]]
    st.markdown("##### **Updated dataframe**")

    st.session_state.clean_waste_03_17 = clean_waste_03_17
    st.write(clean_waste_03_17)


# Access the DataFrame from session state
if 'waste_2003_2017' in st.session_state:
    waste_2003_2017 = st.session_state.waste_2003_2017

    clean_data_waste_2003_2017(waste_2003_2017)

else:
    st.error("No Session Found, First execute the instruction of **app** section on left sidebar")