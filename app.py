import streamlit as st
import openai

# ✅ Use OpenAI's NEW API client (v1.x)
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit page setup
st.set_page_config(page_title="AI Medical Chatbot", page_icon="🩺")
st.title("🧠 AI Medical Chatbot")
st.markdown("Ask any health-related question below 👇")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:")

if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # ✅ OpenAI v1.0 ChatCompletion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI medical assistant who provides basic non-professional medical information."}
        ] + st.session_state.messages
    )

    # Extract the assistant reply
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Show chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write("👤: " + msg["content"])
    else:
        st.write("🤖: " + msg["content"])
