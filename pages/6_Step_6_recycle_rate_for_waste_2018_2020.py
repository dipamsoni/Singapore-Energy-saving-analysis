import streamlit as st
import pandas as pd


def recycle_rate(waste_2018_2020):
    st.title("Calculate Recycle rate for waste of 2018 to 2020 dataset")

    st.info("Original data of waste 2018 to 2020")
    st.write(waste_2018_2020)

    st.info("Here, Considering the data it is possible to create the recycling_rate with the division of the 2 columns. Which is **{totle_waste_generated_tonne}** and **{totle_waste_recycled_tonne}**")
    clean_waste_18_20 = waste_2018_2020
    clean_waste_18_20["recycling_rate"] = round(clean_waste_18_20["total_waste_recycled_tonne"] / clean_waste_18_20["total_waste_generated_tonne"], 2)
    st.session_state.clean_waste_18_20 = clean_waste_18_20
    st.write(clean_waste_18_20)


if 'clean_waste_18_20' in st.session_state:
    clean_waste_18_20 = st.session_state.clean_waste_18_20

    recycle_rate(clean_waste_18_20)
else:
    st.error("No Session Found, First execute the instruction of **Step 3 data cleaning waste 2018 2020** section on left sidebar")