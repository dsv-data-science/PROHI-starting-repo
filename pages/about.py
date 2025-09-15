import streamlit as st

st.title("Max Altez Linhardt")
st.markdown("""
### APSoS (Alarm System Prevention of Sepsis)
The dashboard is an educational demonstration of a Clinical Decision Support tool (CDS) for early sepsis prediction in Intensive Care Unit (ICU) patients. 
It functions as an add-on to Electronic Health Records (EHR), automatically collecting vital signs and laboratory results. 
Using databases such as Medical Information Mart for Intensive Care (MIMIC-III), the system shows how predictive models can detect rising risk in real time. 
Instead of requiring staff to open the tool, alerts appear in the EHR and on mobile devices. 
Notifications are color-coded by severity (yellow = medium, red = high) and include short messages such as: “High sepsis risk! Act within 6 hours.” 
If ignored, alerts escalate to another team. 
The sepsis risk score estimates likelihood within six hours, while SHapley Additive exPlanations (SHAP) highlights key patient features. 
Artificial Intelligence (AI) tools can improve sensitivity, reduce false positives, and support timely treatment.
""")

st.image("./assets/Alert.png", caption="Figure (1): Prototype dashboard for sepsis prediction, showing patient data, vital signs, lab results, and a color-coded risk alert.", use_container_width=True)
