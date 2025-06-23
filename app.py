import streamlit as st
import openai

# ✅ Create OpenAI client (NEW v1 syntax)
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# UI Layout
st.set_page_config(page_title="AI Medical Chatbot", page_icon="🩺")
st.title("🧠 AI Medical Chatbot")
st.markdown("Ask any health-related question below 👇")

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input box
user_input = st.text_input("You:")

if user_input:
    # Save user input
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 🆕 OpenAI API v1 format
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant who gives reliable health information but does not provide professional diagnosis."}
        ] + st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write("👤: " + msg["content"])
    else:
        st.write("🤖: " + msg["content"])
