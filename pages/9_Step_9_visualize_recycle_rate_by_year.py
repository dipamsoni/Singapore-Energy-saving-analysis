import streamlit as st
import plotly.graph_objects as go

def visualize_recycle_rate(combined_data_waste):
    st.title("Visualization of recycle rate over the years")
    st.info("In previous step we did the rename of the similar fields and now need to visualize the recycle rate from the 2003 till 2020 with bar graph.")

    df_total = combined_data_waste[combined_data_waste['waste_type'] == 'total']
    df_total = df_total.sort_values('year')

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df_total['year'],
            y=df_total['recycling_rate'],
            text=df_total['recycling_rate'],
            textposition='auto',
        )
    )
    fig.update_layout(title_text="Bar Graph of Recycle rate",
                      xaxis_tickfont_size=14,
                      yaxis=dict(
                          title='Recycle rate',
                          titlefont_size=14,
                          tickfont_size=14,
                      ),
                      xaxis=dict(
                          title='Years',
                          titlefont_size=14,
                          tickfont_size=14,
                      ))
    st.plotly_chart(fig)

if 'combined_data_waste' in st.session_state:
    combined_data_waste = st.session_state.combined_data_waste

    visualize_recycle_rate(combined_data_waste)
else:
    st.error("No Session Found, First execute the instruction of **Step 7 graph of generated vs recycles waste** section on left sidebar")