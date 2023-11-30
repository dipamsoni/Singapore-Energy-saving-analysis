import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def visualize_recycled_generated_by_waste_type(combined_data_waste):
    for waste_type in combined_data_waste['waste_type'].unique():
        waste_data = combined_data_waste[combined_data_waste['waste_type'] == waste_type]
        fig = go.Figure()

        fig = make_subplots(specs=[[{'secondary_y': True}]])

        fig.add_trace(
            go.Bar(
                x=waste_data['year'],
                y=waste_data['total_waste_generated_tonne'],
                text=waste_data['total_waste_generated_tonne'], name="total_waste_generated_tonne",
                textposition='auto', hovertext="Waste generated"
            )
        )

        fig.add_trace(
            go.Bar(
                x=waste_data['year'],
                y=waste_data['total_waste_recycled_tonne'],
                text=waste_data['total_waste_recycled_tonne'], name="total_waste_recycled_tonne",
                textposition='auto', hovertext="Waste recycled"
            )
        )

        fig.add_trace(
            go.Line(
                x=waste_data['year'],
                y=waste_data['recycling_rate'],
                name='Recycling Rate',
            ),
            secondary_y=True
        )

        fig.update_layout(title_text=f"Bar Graph of Waste Type :- {waste_type}",xaxis_tickfont_size=14,
                          yaxis=dict(title=f'{waste_type}', titlefont_size=14,tickfont_size=14),
                          xaxis=dict(title='Years', titlefont_size=14, tickfont_size=14))
        fig.update_layout(width=940, height=600)
        st.plotly_chart(fig)


if 'combined_data_waste' in st.session_state:
    combined_data_waste = st.session_state.combined_data_waste

    st.title("Bar plot of generated & recycled waste by waste type")
    st.info("Created the bar plot for generated waste & recycled waste according to the waste type over the years as it will be shown in the graph, Legend will explain the category of the each barplot column and the data.")

    visualize_recycled_generated_by_waste_type(combined_data_waste)

    st.info("Reason behind creating the bar plot is to check the waste generation and recycle over the year for each waste type and then also can check the ratio of the recycle_rate. With the help of this chart decision will made that which type of waste need to recycle more and in which type need to focus.")
else:
    st.error("No Session Found, First execute the instruction of **Step 7 graph of generated vs recycles waste** section on left sidebar")