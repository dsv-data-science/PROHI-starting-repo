import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="PROHI Dashboard LALE7029",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Wholesale product sales dashboard. Welcome! 👋")

# INPUT WIDGETS 
selected_region = st.selectbox("Select region", ["Lisbon", "Oporto", "Other region"])
selected_channel = st.radio("Select channel", ["Hotel, restaurant and cafe", "Retail"])
selected_products = st.multiselect("Choose product categories", ["Fresh", "Frozen", "Milk", "Grocery", "Delicatessen", "Detergents"])

# DATA ELEMENT
st.markdown("Product data")
df = pd.DataFrame(np.random.randint(100, 5000, size=(10, 6)), columns=["Fresh", "Frozen", "Milk", "Grocery", "Delicatessen", "Detergents"])
st.dataframe(df)

# CHART
st.markdown("Product chart")
st.bar_chart(df[["Fresh", "Frozen", "Milk", "Grocery", "Delicatessen", "Detergents"]].sum())