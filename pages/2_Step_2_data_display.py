import streamlit as st

st.title("Showcase Data")


def column_selection(energy_saved, waste_2003_2017, waste_2018_2020):
    st.title("Display specific Columns")

    # Display a specific column
    selected_column = st.selectbox("Column selection from energy_saved data:", st.session_state.energy_saved.columns)
    st.write(f'Selected Column - {selected_column}:')
    st.write(st.session_state.energy_saved[selected_column])

    # Display a specific column
    selected_column = st.selectbox('Column selection from waste_2003_2017 data:', st.session_state.waste_2003_2017.columns)
    st.write(f'Selected Column - {selected_column}:')
    st.write(st.session_state.waste_2003_2017[selected_column])

    # Display a specific column
    selected_column = st.selectbox('Column selection from waste_2018_2020 data:', st.session_state.waste_2018_2020.columns)
    st.write(f'Selected Column - {selected_column}:')
    st.write(st.session_state.waste_2018_2020[selected_column])

    st.title("Display Column names only")
    st.write("Columns of energy_saved data")
    st.write(st.session_state.energy_saved.columns)

    st.write("Columns of waste_2003_2017 data")
    st.write(st.session_state.waste_2003_2017.columns)

    st.write("Columns of waste_2018_2020 data")
    st.write(st.session_state.waste_2018_2020.columns)


def describe_dataframe(energy_saved, waste_2003_2017, waste_2018_2020):
    st.title("Describe Data")

    st.write(energy_saved.describe())
    st.write(waste_2003_2017.describe())
    st.write(waste_2018_2020.describe())

# Access the DataFrame from session state
if 'energy_saved' and 'waste_2003_2017' and 'waste_2018_2020' in st.session_state:
    st.header("Energy Saved")
    st.write(st.session_state.energy_saved)
    energy_saved = st.session_state.energy_saved

    st.header("Waste of 2003 to 2017")
    st.write(st.session_state.waste_2003_2017)
    waste_2003_2017 = st.session_state.waste_2003_2017

    st.header("Waste of 2018 to 2020")
    st.write(st.session_state.waste_2018_2020)
    waste_2018_2020 = st.session_state.waste_2018_2020

    describe_dataframe(energy_saved, waste_2003_2017, waste_2018_2020)

    column_selection(energy_saved, waste_2003_2017, waste_2018_2020)


else:
    st.error("No Session Found, First execute the instruction of **app** section on left sidebar")