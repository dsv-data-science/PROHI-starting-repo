import streamlit as st
import numpy as np
import pandas as pd

# -----------------------
# Page Title
# -----------------------
st.title("My Mini Dashboard 🚀")

# -----------------------
# Sidebar Input Widgets
# -----------------------
st.sidebar.header("Input Widgets")

# Widget 1: Text input
name = st.sidebar.text_input("Enter your name:")

# Widget 2: Slider
num_samples = st.sidebar.slider("Number of random samples:", 10, 100, 50)

# Widget 3: Selectbox
category = st.sidebar.selectbox("Choose a category:", ["A", "B", "C"])

# -----------------------
# Synthetic Data
# -----------------------
st.header("Synthetic Dataset")
# Generate random data
data = pd.DataFrame({
    "Category": np.random.choice(["A", "B", "C", "D", "E"], num_samples),
    "Value": np.random.randint(1, 100, num_samples)
})
st.dataframe(data)

# -----------------------
# Bar Chart
# -----------------------
st.header("Bar Chart")
# Aggregate values by category
bar_data = data.groupby("Category")["Value"].sum()
st.bar_chart(bar_data)

# -----------------------
# Histogram
# -----------------------
st.header("Histogram of Values")
hist_values, bins = np.histogram(data["Value"], bins=10)
hist_df = pd.DataFrame({"Counts": hist_values})
st.bar_chart(hist_df)

# -----------------------
# Display Inputs
# -----------------------
st.write(f"Hello {name}! You selected {num_samples} samples and category '{category}'.")
