import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Singapore Energy Analysis"
)

st.title("Main Page")

# Function to load CSV data into session state
def load_csv_into_session_state():

    energy_saved = pd.read_csv("Data/energy_saved.csv")
    waste_2003_2017 = pd.read_csv("Data/wastestats.csv")
    waste_2018_2020 = pd.read_csv("Data/2018_2020_waste.csv")

    # Store the DataFrame in session state
    st.session_state.energy_saved = energy_saved
    st.session_state.waste_2003_2017 = waste_2003_2017
    st.session_state.waste_2018_2020 = waste_2018_2020

    st.success("CSV file uploaded successfully!")


# Function to display the loaded CSV data
def display_csv_data():
    # Access the DataFrame from session state
    if 'energy_saved' and 'waste_2003_2017' and 'waste_2018_2020' in st.session_state:
        energy_saved = st.session_state.energy_saved
        waste_2003_2017 = st.session_state.waste_2003_2017
        waste_2018_2020 = st.session_state.waste_2018_2020

        return energy_saved, waste_2003_2017, waste_2018_2020
    else:
        st.error("No Session Found")

# Main part of the app
if __name__ == "__main__":
    submit = st.button("Submit")

    if submit:
        # Load CSV data into session state
        load_csv_into_session_state()

        # Display the loaded CSV data
        display_csv_data()

        # st.write(energy_saved)
        # st.write(waste_2003_2017)
        # st.write(waste_2018_2020)