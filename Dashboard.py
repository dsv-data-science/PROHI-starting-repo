import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard indiviual assigment 2 Max Altez Linhardt",
    page_icon="👋💪💪💪",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# Sidebar configuration
st.sidebar.success("About project APSoS")
st.sidebar.image("./assets/tabelo.png", caption="Sepsis Prediction Dashboard Sketch", use_column_width=True)

on = st.toggle("Do you want to read this?", value=True)
if on:
    st.write("Let's go and read!")
else: 
    st.write("It's okay, take a break  ☕  ad come back later!")


import streamlit as st
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


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



#Dataframe
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((50, 20)), columns=("col %d" % i for i in range(20))
)
st.dataframe(df)

#Line chart
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.line_chart(df)


# code from Max, first attempt
import streamlit as st
sentiment_mapping = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
selected = st.radio("How do you like this dashboard, plz be generous 😁?", sentiment_mapping)
if selected:
    st.markdown(f"You selected {selected} star(s).")



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
