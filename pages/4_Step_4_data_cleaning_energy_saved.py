import streamlit as st
import pandas as pd


def clean_data_waste_energy_saved(energy_saved):
    st.title("Data Cleaning of Energy Saved data")
    st.info("Original dataframe of energy_saved")
    st.write(energy_saved)

    st.info("As we can see the dataframe columns and rows are not in proper format. Therefore we need to follow few steps to make it in proper format.")
    st.markdown("##### **Steps to follow**")
    st.markdown("1. Transpose dataframe ")
    st.markdown("2. Removed first two columns and first row as it is useless")
    st.markdown("3. Resetting index will set the data in proper format with the ordered index")
    st.markdown("4. Renaming the columns. As we have three columns, material, energy_saved, and crude_oil_saved.")
    st.info("After following the steps mentioned above we have finally updated dataframe.")

    clean_energy_saved = (energy_saved.T.iloc[1:, 2:].reset_index(drop=True).rename(
        columns={2: "material", 3: "energy_saved", 4: "crude_oil_saved"}))
    st.session_state.clean_energy_saved = clean_energy_saved
    st.write(clean_energy_saved)


# Access the DataFrame from session state
if 'energy_saved' in st.session_state:
    energy_saved = st.session_state.energy_saved

    clean_data_waste_energy_saved(energy_saved)
else:
    st.error("No Session Found, First execute the instruction of **app** section on left sidebar")