import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define your columns list
columns = ['Column1', 'Column2', 'Column3']  # Replace with your actual column names

# Title of the dashboard
st.title("Data Intelligence Dashboard")

# Sidebar for navigation
st.sidebar.title("Dashboard Menu")
uploaded_file = st.sidebar.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Load the file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Data Preview:")
    st.dataframe(df)

    columns = df.columns.tolist()

    # Bar Chart
    st.subheader("Bar Chart")
    bar_column = st.sidebar.selectbox("Column for Bar Chart", columns, key="bar_column")
   
    # Prepare data for bar chart
    bar_data = df[bar_column].value_counts()

    # Create a new figure for the bar chart
    fig_bar, ax_bar = plt.subplots()
    sns.barplot(x=bar_data.index, y=bar_data.values, ax=ax_bar)
    ax_bar.set_xlabel(bar_column)
    ax_bar.set_ylabel("Counts")
    ax_bar.set_title(f'Bar chart of {bar_column}')
    st.pyplot(fig_bar)

    # Histogram
    st.subheader("Histogram")
    hist_column = st.sidebar.selectbox("Column for Histogram", columns, index=0, key="hist_column")
   
    # Create a new figure for the histogram
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(df[hist_column], bins=30, edgecolor='black')
    ax_hist.set_xlabel(hist_column)
    ax_hist.set_ylabel('Frequency')
    ax_hist.set_title(f'Histogram of {hist_column}')
    st.pyplot(fig_hist)
    
     # Scatter Plot
    st.subheader("Scatter Plot")
    scatter_x = st.sidebar.selectbox("X-axis for Scatter Plot", columns, key="scatter_x")
    scatter_y = st.sidebar.selectbox("Y-axis for Scatter Plot", columns, key="scatter_y")
    
    # Create a new figure for the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df[scatter_x], df[scatter_y], alpha=0.7)
    ax.set_xlabel(scatter_x)
    ax.set_ylabel(scatter_y)
    ax.set_title(f'Scatter Plot: {scatter_x} vs {scatter_y}')
    st.pyplot(fig)

    # Pie Chart
    st.subheader("Pie Chart")
    pie_column = st.sidebar.selectbox("Column for Pie Chart", columns, key="pie_column")
    pie_data = df[pie_column].value_counts()

    # Create a new figure for the pie chart
    fig, ax = plt.subplots()
    ax.pie(pie_data.values, labels=pie_data.index, autopct='%1.1f%%', startangle=90, counterclock=False)
    ax.set_title(f'Pie Chart of {pie_column}')
    st.pyplot(fig)

    # Line Chart
    st.subheader("Line Chart")
    line_x = st.sidebar.selectbox("X-axis for Line Chart", columns, key="line_x")
    line_y = st.sidebar.selectbox("Y-axis for Line Chart", columns, key="line_y")
    
    # Create a new figure for the line chart
    fig, ax = plt.subplots()
    ax.plot(df[line_x], df[line_y], marker='o', linestyle='-', linewidth=2)
    ax.set_xlabel(line_x)
    ax.set_ylabel(line_y)
    ax.set_title(f'Line Chart: {line_x} vs {line_y}')
    st.pyplot(fig)
