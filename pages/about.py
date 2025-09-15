import streamlit as st

st.title("Max Altez Linhardt")
st.markdown("""
### Educational Demonstration: Clinical Decision Support Tool for Early Sepsis Prediction
The dashboard will be an educational demonstration of a “clinical decision support tool” to help doctors and nurses predict sepsis early in ICU patients. The system will work as an add-on to any electronic health record (EHR) and automatically read vital signs and lab results. Databases like MIMIC-III show that vital signs and lab values can be collected in a structured manner and used to develop tools for early sepsis prediction [8]. Instead of requiring staff to check the dashboard, the system works quietly in the background. Healthcare workers can continue their work in the medical record system or with other patients. When sepsis risk increases, the tool sends an alert to the care team.
Alerts appear as pop-ups in the EHR and as notifications on mobile devices staff already use. Each alert is color-coded by risk level (yellow = medium and red = high) and includes a short message, for example: “High sepsis risk – act within 6 hours.” If no one acknowledges the alert within a set time, the system escalates the warning to another healthcare team.
A central feature is the sepsis risk score, showing the likelihood a patient will develop sepsis within 6 hours. Model explainability will be demonstrated through SHAP analysis, highlighting which patient features contribute most to risk scores and helping doctors trust the prediction. Evidence suggests AI-based tools can outperform physicians in early detection, increasing sensitivity by up to 32% while reducing false positives [9]. By warning staff early, the dashboard enables timely treatment, which is critical for survival in sepsis [4].
""")

st.image("./assets/Alert.png", caption="Figure (1): Prototype dashboard for sepsis prediction, showing patient data, vital signs, lab results, and a color-coded risk alert.", use_container_width=True)
