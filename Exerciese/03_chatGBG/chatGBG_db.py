import streamlit as st
from bot import Bot


def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "bot" not in st.session_state:
        st.session_state.bot = Bot()

def display_chat_messages():
    """Display chat messages from history"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    """Handle user input and generate bot response."""
    # prompt = st.chat_input("What is up?")
    # if prompt:
    # := walrus operator
    st.write(st.session_state)

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_state.bot.chat(prompt)
        response = f"Ro Båt: {bot_response}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

def layout():

    st.title("Chat bot for making fun of stockholm dialect")
    st.write("Hello wolrd")

    display_chat_messages()
    handle_user_input()


if __name__ == "__main__":
    initialize_session_state()
    layout()