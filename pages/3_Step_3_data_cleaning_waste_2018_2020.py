import streamlit as st
import pandas as pd


def clean_data_waste_2018_2020(waste_2018_2020):
    st.title("Data Cleaning of Waste 2018 to 2020 data")
    st.info("Original dataframe columns of waste_2018_2020")
    st.write(waste_2018_2020.columns)

    clean_waste_18_20 = waste_2018_2020.rename(
        columns={
            "Waste Type": "waste_type",
            "Total Generated ('000 tonnes)": "total_waste_generated_tonne",
            "Total Recycled ('000 tonnes)": "total_waste_recycled_tonne",
            "Year": "year",
        }
    )
    st.info("Need to change the column name because of we will match waste_2003_2017 dataframe with waste_2018_2020 "
            "dataframe. There are most columns data are same and the column is representing the data in tons which "
            "has {'000} in present column name. Here is the updated renamed column of waste_2018_2020 dataframe.")
    st.write(clean_waste_18_20)

    clean_waste_18_20["total_waste_generated_tonne"] = (
            clean_waste_18_20["total_waste_generated_tonne"] * 1000
    )
    clean_waste_18_20["total_waste_recycled_tonne"] = (
            clean_waste_18_20["total_waste_recycled_tonne"] * 1000
    )
    st.session_state.clean_waste_18_20 = clean_waste_18_20
    st.info("After rename of the columns we also need to convert the data into the tons representing the full number "
            "instead of the label. Here the calculation is done with the respected columns {*}multiply by 1000 as "
            "there were {'000} in the original dataframe. Here is the updated data which showing the data with full "
            "numbers in tons.")
    st.write(clean_waste_18_20)


# Access the DataFrame from session state
if 'waste_2018_2020' in st.session_state:
    waste_2018_2020 = st.session_state.waste_2018_2020

    clean_data_waste_2018_2020(waste_2018_2020)

else:
    st.error("No Session Found, First execute the instruction of **app** section on left sidebar")
