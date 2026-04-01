import streamlit as st

def setup_ui():
    st.set_page_config(
        page_title="Multi LLM Chatbot",
        page_icon="🤖",
        layout="wide"
    )
    st.title("🤖 Multi-Model Chatbot")
    st.caption("🚀 Groq + Gemini | Smart AI Router")

def sidebar_controls():
    st.sidebar.header("⚙️ Settings")

    mode = st.sidebar.radio(
        "Mode",
        ["Manual", "Smart Router", "Compare"]
    )

    model = None
    if mode == "Manual":
        model = st.sidebar.selectbox("Choose Model", ["Groq", "Gemini"])

    if st.sidebar.button("🗑 Clear Chat"):
        st.session_state.chat_history = []

    if st.sidebar.button("📥 Export Chat"):
        export_chat()

    return mode, model


def display_chat(chat_history):
    for msg in chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def export_chat():
    text = ""
    for msg in st.session_state.chat_history:
        role = "User" if msg["role"] == "user" else "Assistant"
        text += f"{role}: {msg['content']}\n\n"

    st.download_button("Download Chat", text, file_name="chat.txt")