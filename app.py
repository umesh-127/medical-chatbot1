import streamlit as st

# Disease data dictionary
disease_info = {
    "malaria": "Symptoms include high fever, chills, sweating, headache, nausea, and vomiting.",
    "dengue": "Symptoms include severe headache, joint and muscle pain, skin rash, and bleeding.",
    "typhoid": "Symptoms include prolonged fever, abdominal pain, weakness, and constipation.",
    "cold": "Common cold symptoms are sneezing, runny nose, sore throat, and mild fever.",
    "covid": "COVID-19 symptoms include fever, cough, tiredness, and loss of taste or smell.",
    "tuberculosis": "Symptoms include chronic cough, weight loss, night sweats, and blood in sputum.",
    "cholera": "Cholera causes severe diarrhea and dehydration, often due to contaminated water.",
    "asthma": "Symptoms include wheezing, breathlessness, chest tightness, and coughing.",
    "diabetes": "Symptoms include increased thirst, frequent urination, hunger, fatigue, and blurred vision."
}

# Streamlit UI
st.set_page_config(page_title="AI Medical Chatbot", page_icon="🩺")
st.title("🧠 AI Medical Chatbot")
st.markdown("Type the name of a disease to see its symptoms/effects 👇")

# Input box
disease = st.text_input("Enter Disease Name:")

# Convert to lowercase for matching
disease_lower = disease.lower().strip()

# Response
if disease:
    if disease_lower in disease_info:
        st.success(f"🩺 **{disease.title()}**: {disease_info[disease_lower]}")
    else:
        st.error("❌ Sorry, I don't have information about that disease. Try another one.")
