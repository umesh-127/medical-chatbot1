import openai
import streamlit as st

openai.api_key = "your_openai_key_here"

st.set_page_config(page_title="AI Medical Chatbot", page_icon="🧠")
st.title("🩺 AI Medical Chatbot")
st.markdown("Ask any health-related question below 👇")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI medical assistant that provides basic health-related information only."}
        ] + st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write("👤: " + msg["content"])
    else:
        st.write("🤖: " + msg["content"])
