import streamlit as st

# 🔥 Lazy load chatbot (ONLY ONCE)
@st.cache_resource
def load_chatbot():
    from chatbot import get_response
    return get_response

get_response = load_chatbot()

# UI (lightweight)
st.set_page_config(page_title="Chatbot", page_icon="🤖")

st.title("🤖NLP CHATBOT")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔥 Chat UI (NO text_input lag)
user_input = st.chat_input("Type your message...")

if user_input:
    response = get_response(user_input)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display messages
for sender, message in st.session_state.messages:
    if sender == "You":
        with st.chat_message("user"):
            st.write(message)
    else:
        with st.chat_message("assistant"):
            st.write(message)

# Clear button
if st.button("Clear Chat"):
    st.session_state.messages = []