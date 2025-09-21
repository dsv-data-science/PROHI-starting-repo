import streamlit as st

# Title must be your name
st.title("Dharinisri Magudapathy Saravanakumar")

# 100–150 words, Markdown formatted
st.markdown("""
My DSHI course mini-project investigates **depression among students** using a tabular dataset
(~18 features). After initial data understanding, I performed **data cleaning** (renaming columns,
removing low-information fields, fixing types, and handling missing values) and then conducted
**exploratory data analysis** with group-bys, pivot tables, and visualizations (stacked bars and a
heatmap). Clear signals emerged: **higher academic pressure** aligns with greater depression
prevalence; **short or irregular sleep** (<5 hours or 5–7 hours) is associated with higher risk;
**financial stress** relates strongly to suicidal thoughts; and **family history** shows a modest
elevation. A heatmap combining pressure, sleep, and maximal financial stress highlighted the
highest-risk cells. The **Pearson correlation** between age and study hours was near zero,
suggesting other drivers. Overall, the project demonstrates how transparent preprocessing plus
simple statistics and visuals can surface actionable hypotheses for student well-being—while
acknowledging that causality cannot be inferred.
""")
