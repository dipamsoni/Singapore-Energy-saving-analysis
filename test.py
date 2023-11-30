import streamlit as st
import pandas as pd

# Function to initialize session state
def initialize_session_state():
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame()

# Streamlit app
st.title('Pandas Operations with Session State')

# Initialize session state
initialize_session_state()

# Upload CSV file
uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])
if uploaded_file is not None:
    st.session_state.df = pd.read_csv(uploaded_file)
    st.write('Uploaded DataFrame:')
    st.write(st.session_state.df)

# Perform Pandas operations on the stored DataFrame
if not st.session_state.df.empty:
    st.write('DataFrame Info:')
    st.write(st.session_state.df.info())

    st.write('Descriptive Statistics:')
    st.write(st.session_state.df.describe())

    # You can add more Pandas operations based on your needs

    # Display a specific column
    selected_column = st.selectbox('Select a column to display:', st.session_state.df.columns)
    st.write(f'Selected Column - {selected_column}:')
    st.write(st.session_state.df[selected_column])

    # # Filter data based on a condition
    # age_threshold = st.slider('Select an age threshold:', min_value=20, max_value=40, value=30)
    # filtered_df = st.session_state.df[st.session_state.df['Age'] > age_threshold]
    # st.write(f'People older than {age_threshold} years:')
    # st.write(filtered_df)
