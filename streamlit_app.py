import streamlit as st
import plotly as px
import pandas as pd

# Load data
file_path1 = 'rfm_output.csv'
rfmoutput_df = pd.read_csv(file_path1)

file_path2 = 'summary_result.csv'
summaryresult_df = pd.read_csv(file_path2)

st.set_page_config(
    page_title="RFM Approaches for Retail Customer Segmentation",
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="auto",  # or "collapsed"
)
st.markdown(
    """
    <style>
        body {
            background-color: #f9f9f9;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: #ffffff;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #004080;
            padding: 20px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; margin-top: -20px;'>RFM Approaches for Retail Customer Segmentation</h1>", unsafe_allow_html=True)

# Cluster Visualization
st.subheader('Cluster Visualization')

# Layout for visualizations
col1, col2, col3, col4 = st.columns(4)

# Visualizations
with col1:
    fig_percentile = px.pie(
        names=rfmoutput_df['Cluster_Percentile'].value_counts().index,
        values=rfmoutput_df['Cluster_Percentile'].value_counts().values,
        title='Cluster_Percentile Distribution',
        height=300, width=200
    )
    fig_percentile.update_layout(
        title=dict(x=0.5, y=0.95, xanchor='center', yanchor='top', font=dict(size=12)),
        margin=dict(l=0, r=0, t=30, b=0),
        autosize=False
    )
    st.plotly_chart(fig_percentile)

with col2:
    fig_weighted = px.pie(
        names=rfmoutput_df['Cluster_Weighted'].value_counts().index,
        values=rfmoutput_df['Cluster_Weighted'].value_counts().values,
        title='Cluster_Weighted Distribution',
        height=300, width=200
    )
    fig_weighted.update_layout(
        title=dict(x=0.5, y=0.95, xanchor='center', yanchor='top', font=dict(size=12)),
        margin=dict(l=0, r=0, t=30, b=0),
        autosize=False
    )
    st.plotly_chart(fig_weighted)
    

with col3:
    fig_equal = px.pie(
        names=rfmoutput_df['Cluster_Equal'].value_counts().index,
        values=rfmoutput_df['Cluster_Equal'].value_counts().values,
        title='Cluster_Equal Distribution',
        height=300, width=200
    )
    fig_equal.update_layout(
        title=dict(x=0.5, y=0.95, xanchor='center', yanchor='top', font=dict(size=12)),
        margin=dict(l=0, r=0, t=30, b=0),
        autosize=False
    )
    st.plotly_chart(fig_equal)

with col4:
    fig_std = px.pie(
        names=rfmoutput_df['Cluster_StandardDev'].value_counts().index,
        values=rfmoutput_df['Cluster_StandardDev'].value_counts().values,
        title='Cluster_StandardDev Distribution',
        height=300, width=200
    )
    fig_std.update_layout(
        title=dict(x=0.5, y=0.95, xanchor='center', yanchor='top', font=dict(size=12)),
        margin=dict(l=5, r=0, t=30, b=0),
        autosize=False
    )
    st.plotly_chart(fig_std)


# Layout for visualizations
st.subheader('Evaluation Score Distribuition')
col1, col2, col3 = st.columns(3)

# Bar chart for Silhouette Score
with col1:
    silhouette_fig = px.bar(
        summaryresult_df,
        x='RFM Approach',
        y='Silhouette Score',
        title='Silhouette Score by RFM Approach',
        height=300, width=300
    )
    silhouette_fig.update_layout(
        margin=dict(l=10, r=10, t=30, b=0),
        title=dict(font=dict(size=16))
    )
    st.plotly_chart(silhouette_fig)

# Line chart for Calinski-Harabasz Score
with col2:

    calinski_fig = px.line(
        summaryresult_df,
        x='RFM Approach',
        y='Calinski-Harabasz Score',
        title='Calinski-Harabasz Score by RFM Approach',
        height=300, width=300
    )
    calinski_fig.update_layout(
        margin=dict(l=10, r=10, t=30, b=0),
        title=dict(font=dict(size=16))
    )
    st.plotly_chart(calinski_fig)

# Line chart for Inertia
with col3:
    inertia_fig = px.line(
        summaryresult_df,
        x='RFM Approach',
        y='Inertia',
        title='Inertia by RFM Approach',
        height=300, width=300
    )
    inertia_fig.update_layout(
        margin=dict(l=10, r=10, t=30, b=0),
        title=dict(font=dict(size=16))
    )
    st.plotly_chart(inertia_fig)

# Streamlit App
st.subheader('RFM Approach Evaluation')

# Dropdown to select RFM Approach
selected_rfm_approach = st.selectbox("Select RFM Approach:", summaryresult_df['RFM Approach'])

# Dropdown to select Evaluation Metric
selected_metric = st.selectbox("Select Evaluation Metric:", ['Silhouette Score', 'Calinski-Harabasz Score', 'Inertia'])

# Display result based on selected Evaluation Metric
st.text(f"Result for {selected_rfm_approach} - {selected_metric}:")
selected_rfm_details = summaryresult_df[summaryresult_df['RFM Approach'] == selected_rfm_approach]
result_value = selected_rfm_details[selected_metric].values[0]
st.write(result_value)

# Display selected RFM Approach details
st.text("Selected RFM Approach Details:")
st.write(selected_rfm_details)

# Customer Information
st.subheader('Customer Level Customer Segmentation Details')

# Dropdown for selecting CustomerID
selected_customer = st.selectbox('Select CustomerID:', rfmoutput_df['CustomerID'])

# Display selected customer information
selected_customer_info = rfmoutput_df[rfmoutput_df['CustomerID'] == selected_customer].squeeze()
st.subheader("Selected Customer Information:")

# Convert Series to DataFrame and transpose
selected_customer_df = pd.DataFrame(selected_customer_info).transpose()

# Display the dataframe horizontally
st.dataframe(selected_customer_df.style.highlight_max(axis=1))

