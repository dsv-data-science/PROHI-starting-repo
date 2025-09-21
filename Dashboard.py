import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# # DATAFRAME MANAGEMENT
# import numpy as np

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# # Add a slider to the sidebar:
# add_slider = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )
import streamlit as st
import numpy as np
import pandas as pd

st.title("Clinical Waiting Time Dashboard")

# ---------- Generate meaningful synthetic data ----------
np.random.seed(42)
days = pd.date_range(end=pd.Timestamp.today().normalize(), periods=60)
departments = ["General Practice", "Pediatrics", "Cardiology", "Radiology", "Dermatology"]

rows = []
for d in departments:
    base = {
        "General Practice": 22,
        "Pediatrics": 28,
        "Cardiology": 35,
        "Radiology": 25,
        "Dermatology": 18
    }[d]
    for day in days:
        # add weekday effect (Mondays busier, weekends lighter)
        wd = day.weekday()
        weekday_bump = {0: +6, 1: +3, 2: +2, 3: +1, 4: 0, 5: -3, 6: -4}[wd]
        wait = np.clip(np.random.normal(base + weekday_bump, 6), 5, 90)
        sat = int(np.clip(np.round(5 - (wait - 15)/20 + np.random.normal(0, 0.6)), 1, 5))
        rows.append({
            "date": day.date(),
            "department": d,
            "weekday": day.strftime("%A"),
            "wait_minutes": round(float(wait), 1),
            "satisfaction": sat
        })

df = pd.DataFrame(rows)

# ---------- Controls (Input widgets) ----------
dept = st.selectbox("Choose department", departments, index=0)

min_day, max_day = df["date"].min(), df["date"].max()
date_range = st.slider(
    "Select date range",
    min_value=min_day,
    max_value=max_day,
    value=(max_day - pd.Timedelta(days=14), max_day),
    format="YYYY-MM-DD"
)


# When slider uses 2-tuple: (start, end)
if isinstance(date_range, tuple):
    start_date, end_date = date_range
else:
    # fallback if single date gets returned by OS quirk
    start_date, end_date = min_day, max_day

max_wait = st.slider("Filter by maximum wait (minutes)", 10, 90, 60)

weekdays = st.multiselect(
    "Include weekdays",
    options=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    default=["Monday","Tuesday","Wednesday","Thursday","Friday"]
)

show_raw = st.checkbox("Show raw filtered rows")

# ---------- Filter logic ----------
mask = (
    (df["department"] == dept) &
    (df["date"] >= start_date) &
    (df["date"] <= end_date) &
    (df["wait_minutes"] <= max_wait) &
    (df["weekday"].isin(weekdays))
)
fdf = df.loc[mask].copy()

# ---------- KPIs ----------
left, mid, right = st.columns(3)
left.metric("Records", len(fdf))
mid.metric("Avg Wait (min)", f"{fdf['wait_minutes'].mean():.1f}" if not fdf.empty else "—")
right.metric("Avg Satisfaction (1–5)", f"{fdf['satisfaction'].mean():.1f}" if not fdf.empty else "—")

# ---------- Data element ----------
st.subheader("Filtered Appointments")
st.dataframe(fdf.reset_index(drop=True), use_container_width=True)

# ---------- Chart ----------
st.subheader("Average Wait Time by Date")
if fdf.empty:
    st.info("No data for the current filters. Try widening the date range or increasing max wait.")
else:
    by_day = (
        fdf.groupby("date", as_index=False)["wait_minutes"]
        .mean()
        .rename(columns={"wait_minutes": "avg_wait"})
        .sort_values("date")
    )
    st.line_chart(by_day.set_index("date")["avg_wait"])

st.caption("Synthetic dataset for educational purposes. Patterns: higher waits on Mondays, "
           "lower on weekends; satisfaction drops as waits increase.")
