import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Singapore Energy Analysis"
)

st.title("Singapore Recycling and Waste")

st.info("Singapore has reached a new milestone in its quest to become a zero-waste nation, since the government is concerned about the growing number of garbage disposals. The Semakau Landfill would run out of room by 2035 if present trends continue, which is a concerning issue for Singaporeans [Official Site](https://www.towardszerowaste.gov.sg/). To make matters worse, Singapore has a scarcity of land for new incinerator facilities or landfills. The government would want to incentivize residents by sharing the entire amount of energy saved by united recycling efforts each year.")

st.header("From 2003 to 2020, we will use recycling information to compute energy savings based on five waste types: ")
st.write("1) Plastics")
st.write("2) Paper")
st.write("3) Glass")
st.write("4) Ferrous")
st.write("5) Nonferrous metals")

st.info("**In this analysis, Total 3 datasets are available. By clicking **Submit** button below all 3 datasets will be added into the session and kindly follow the steps from the left sidebar panel for smooth and error free running process.**")


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