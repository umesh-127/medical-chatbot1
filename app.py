import streamlit as st

st.set_page_config(page_title="AI Medical Chatbot", page_icon="🩺")
st.title("🧠 AI Medical Chatbot (Demo Version)")
st.markdown("This is a demo version due to OpenAI API limits. Below are example conversations.")

sample_conversations = [
    {"question": "What are the symptoms of malaria?", "answer": "Symptoms include high fever, chills, sweating, headache, nausea, and vomiting."},
    {"question": "How can I treat a common cold?", "answer": "Rest, drink fluids, and take over-the-counter medication like paracetamol."},
    {"question": "Is it safe to take paracetamol and ibuprofen together?", "answer": "Generally, yes in recommended doses. But always consult a doctor for medical advice."}
]

for i, conv in enumerate(sample_conversations):
    st.write(f"**👤 You:** {conv['question']}")
    st.write(f"**🤖 Bot:** {conv['answer']}")
    st.markdown("---")
