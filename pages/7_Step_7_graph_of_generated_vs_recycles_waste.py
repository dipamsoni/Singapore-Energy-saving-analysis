import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime


def bar_graph(clean_waste_03_17, clean_waste_18_20):
    st.title("Analysis of Recycle waste and generated waste over the years")

    data = pd.concat([clean_waste_18_20, clean_waste_03_17]).sort_values(by="year")
    overall = data[(data["waste_type"] == "Overall") | (data["waste_type"] == "Total")]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=overall["year"],
            y=overall["total_waste_generated_tonne"],
            name="Waste Generated",
        )
    )

    fig.add_trace(
        go.Bar(
            x=overall["year"],
            y=overall["total_waste_recycled_tonne"],
            name="Waste Recycled",
        )
    )

    st.plotly_chart(fig)
    st.session_state.combined_data_waste = data


if 'clean_waste_03_17' and 'clean_waste_18_20' in st.session_state:
    clean_waste_03_17 = st.session_state.clean_waste_03_17
    clean_waste_18_20 = st.session_state.clean_waste_18_20

    bar_graph(clean_waste_03_17, clean_waste_18_20)
else:
    st.error("No Session Found, First execute the instruction of **Step 5 data clean waste 2003 2017** and **Step 6 recycle rate for waste 2018 2020** section on left sidebar")