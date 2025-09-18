import streamlit as st
import numpy as np
import pandas as pd

st.title("Dashboard Page 🚀")

# Sidebar for input widgets
st.sidebar.header("Input Widgets")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.slider("Select your age:", 0, 100, 25)
option = st.sidebar.selectbox("Choose a category:", ["A", "B", "C"])


# Main data section
st.header("Sample Data")
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E"],
    "Values": np.random.randint(0, 100, 5)
})
st.dataframe(data)

# Bar chart
st.header("Bar Chart")
st.bar_chart(data.set_index("Category"))


st.write(f"Hello {name}, you selected age {age} and category {option}.")
