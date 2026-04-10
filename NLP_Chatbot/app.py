import streamlit as st
from NLP_Chatbot.chat_loader import get_chat

# ⚡ cache chatbot permanently
@st.cache_resource(show_spinner=False)
def load_chatbot():
    return get_chat()

chat = load_chatbot()

st.title("🤖 NLTK Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:")

if user_input:
    response = chat.respond(user_input)

    st.session_state.messages += [
        ("You", user_input),
        ("Bot", response)
    ]

for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")