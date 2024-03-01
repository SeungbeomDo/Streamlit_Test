import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Dummy data for demonstration
data = {
    'Date': ['t-1', 't-3', 't-5', 't-7', 't-10'],
    'Retention Rate': [0.75, 0.68, 0.62, 0.55, 0.49],
    'Change': [-0.012, 0.025, -0.070, -0.013, 0.023],
    'Payment': [0.01, 0.023, 0.09, 0.11, 0.115],
    'Payment_Change': [0.001, 0.001, -0.001, 0.001, 0.01]
    # Replace this with your actual retention rate data
}

df = pd.DataFrame(data)

cola, colb = st.columns([0.44, 0.56])

with cola:
    col1, col2 = st.columns([0.5, 0.5])

    # Metric 1 in the first column
    with col1:
        st.metric(label="광고클릭 수", value="507", delta_color="inverse", delta="9 {}".format('(전일비)'))
        st.metric(label="가입자 수", value="349,374", delta_color="inverse", delta="63 {}".format('(신규가입)'))
        st.metric(label="수면 평점", value="3.12", delta_color="inverse", delta="0.1 {}".format('(전일비)'))
        
    with col2:
        st.metric(label="최근 7일 AU", value="49,555", delta_color="inverse", delta="5 {}".format('(전일비)'))
        st.metric(label="월 매출", value="949,000", delta_color="inverse", delta="31,000 {}".format('(신규결제)'))
        st.metric(label="챌린지 참여", value="509", delta_color="inverse", delta="11 {}".format('(전일비)'))


# Line graph in the second column

with colb:
    fig = px.line(df, x='Date', y='Retention Rate', markers=True, line_shape='linear')  # Set the line color to red
    fig.update_layout(width=400, height=165, margin=dict(b=10, t=0, l=0))  # Adjust the graph size and bottom margin
    fig.update_traces(line_color='#FF0000')
    for i, row in df.iterrows():
        arrowhead = 4  # Set arrowhead based on positive or negative change
        arrowcolor = 'black' if row['Change'] > 0 else 'grey'  # Set arrow color based on positive or negative change
        ay = 20 if row['Change'] >= 0 else -20  # Increase the arrow y-offset for a larger gap
        fig.add_annotation(x=row['Date'], y=row['Retention Rate'], text=f"{row['Change']:.1%}p",
                           showarrow=True, arrowhead=arrowhead, arrowcolor=arrowcolor, arrowwidth=2,
                           ax=0, ay=ay, font=dict(color='black', size=10))

    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Retention', title_font=dict(size=12))
    st.plotly_chart(fig)
    
    fig = px.line(df, x='Date', y='Payment', markers=True, line_shape='linear')  # Set the line color to red
    fig.update_layout(width=400, height=165, margin=dict(b=10, t=0, l=0))  # Adjust the graph size and bottom margin
    fig.update_traces(line_color='#FF0000')
    for i, row in df.iterrows():
        arrowhead = 4  # Set arrowhead based on positive or negative change
        arrowcolor = 'black' if row['Payment_Change'] > 0 else 'grey'  # Set arrow color based on positive or negative change
        ay = 20 if row['Payment_Change'] >= 0 else -20  # Increase the arrow y-offset for a larger gap
        fig.add_annotation(x=row['Date'], y=row['Payment'], text=f"{row['Payment_Change']:.1%}p",
                           showarrow=True, arrowhead=arrowhead, arrowcolor=arrowcolor, arrowwidth=2,
                           ax=0, ay=ay, font=dict(color='black', size=10))

    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Cumulative Payment', title_font=dict(size=12))
    st.plotly_chart(fig)
