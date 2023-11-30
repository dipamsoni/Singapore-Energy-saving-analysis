import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def visualize_ratio_of_waste_type_by_year(combined_data_waste):
    for year in combined_data_waste['year'].unique():
        year_data = combined_data_waste[combined_data_waste['year'] == year]

        # Values to ignore
        ignore_values = ["total"]

        # Query to ignore specific values
        filtered_df = year_data.query('waste_type not in @ignore_values')

        fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])

        fig.add_trace(go.Pie(labels=filtered_df["waste_type"], values=filtered_df["total_waste_generated_tonne"],
                             name="Total waste generated"), 1, 1)
        fig.add_trace(go.Pie(labels=filtered_df["waste_type"], values=filtered_df["total_waste_recycled_tonne"],
                             name="Total waste recycled"), 1, 2)

        # Use `hole` to create a donut-like pie chart
        fig.update_traces(hole=.6, hoverinfo="label+percent+name")
        fig.update_layout(width=900, height=600)

        fig.update_layout(
            title_text=f"Year {year}'s Data",
            # Add annotations in the center of the donut pies.
            annotations=[
                dict(text='Total waste generated', x=0.22, y=0.5, font_size=14, showarrow=False, xanchor='center',
                     yanchor='middle', textangle=0),
                dict(text='Total waste recycled', x=0.77, y=0.5, font_size=14, showarrow=False, xanchor='center',
                     yanchor='middle', textangle=0)])

        st.plotly_chart(fig)


if 'combined_data_waste' in st.session_state:
    combined_data_waste = st.session_state.combined_data_waste

    st.title("Pie chart of generated & recycled waste type by year")
    st.info("Created the pie chart for generated waste & recycled waste according to the waste type over the years as it will be shown in the graph, Legend will explain the category of the each waste type and the data.")

    visualize_ratio_of_waste_type_by_year(combined_data_waste)

    st.info("Reason behind creating the pie chart is to check the waste generation and recycle ratio(percentage) of waste type per year. With the help of this chart decision will made that which type of waste are generated more in percentage and which is recycled more in percentage. It will helpful to compare previous year with the current and upcoming years for each type of waste.")
else:
    st.error("No Session Found, First execute the instruction of **Step 7 graph of generated vs recycles waste** section on left sidebar")