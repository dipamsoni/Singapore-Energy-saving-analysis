import streamlit as st
import pandas as pd


def clean_combined_data(combined_data_waste):
    st.title("Clean combined dataframe of waste from 2003 to 2020")
    st.info("Here, 2 dataframes combined into 1 and all fields (unique waste types) are same in both dataframe")

    combined_data_waste['waste_type'] = combined_data_waste['waste_type'].str.lower()
    st.write(combined_data_waste['waste_type'].value_counts())
    st.info("As per the unique_count function, the name of the **unique data in both dataframe is not same** and the **condition is that it must be same**. So need to rename the similar field to make it in one simple understandable word format.")

    combined_data_waste = combined_data_waste.replace('plastic', 'plastics')
    combined_data_waste = combined_data_waste.replace('overall', 'total')
    combined_data_waste = combined_data_waste.replace('horticultural', 'horticultural waste')
    combined_data_waste = combined_data_waste.replace('ferrous metal', 'ferrous metals')
    combined_data_waste = combined_data_waste.replace('non-ferrous metal', 'non-ferrous metals')
    combined_data_waste = combined_data_waste.replace(['construction& demolition', 'construction & demolition', 'c&d'], 'construction debris')
    combined_data_waste = combined_data_waste.replace(['others (stones, ceramic, rubber, ect)', 'others (stones, ceramics, etc.)', 'others', 'others (stones, ceramic, rubber, etc.)', 'others (stones, ceramics & rubber etc.)'], 'others (stones, ceramics & rubber etc)')
    combined_data_waste = combined_data_waste.replace('food waste', 'food')
    combined_data_waste = combined_data_waste.replace('wood', 'wood/timber')
    combined_data_waste = combined_data_waste.replace(['ash & sludge', 'sludge'], 'ash and sludge')

    st.write(combined_data_waste['waste_type'].value_counts())

    st.info("As per the conclusion and the requirement of the cleaning, Now the unique data of each waste type is equal from both dataframe as renamed the similar field.")
    st.session_state.combined_data_waste = combined_data_waste


if 'combined_data_waste' in st.session_state:
    combined_data_waste = st.session_state.combined_data_waste

    clean_combined_data(combined_data_waste)
else:
    st.error("No Session Found, First execute the instruction of **Step 7 graph of generated vs recycles waste** section on left sidebar")