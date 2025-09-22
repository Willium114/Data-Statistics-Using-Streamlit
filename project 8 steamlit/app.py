# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Data Statistics Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)

    st.subheader("🔎 Preview of Data")
    st.write(df.head())  # Show first 5 rows

    st.subheader("📈 Data Summary")
    st.write(df.describe())  # Show statistics (mean, std, min, max)

    # Column selection
    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns
    column = st.selectbox("Choose a column to visualize", numeric_columns)

    if column:
        st.subheader(f"📊 Distribution of {column}")

        # Plotting
        fig, ax = plt.subplots()
        df[column].hist(ax=ax, bins=10, edgecolor="black")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        ax.set_title(f"{column} Distribution")
        st.pyplot(fig)

        st.subheader(f"📈 Line Chart of {column}")
        st.line_chart(df[column])
else:
    st.info("⬆ Please upload a CSV file to get started")
