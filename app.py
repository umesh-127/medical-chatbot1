import streamlit as st
import openai

# ✅ Create OpenAI client
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.set_page_config(page_title="AI Medical Chatbot", page_icon="🩺")
st.title("🧠 AI Medical Chatbot")
st.markdown("Ask any health-related question below 👇")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 🔁 Call GPT-3.5 with chat history
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a medical chatbot that gives basic, non-diagnostic health information. You are not a doctor."}
        ] + st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write("👤: " + msg["content"])
    else:
        st.write("🤖: " + msg["content"])
