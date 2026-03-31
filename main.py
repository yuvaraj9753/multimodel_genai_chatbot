"""
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq


# load the env variables
load_dotenv()

# streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)
st.title("💬 Generative AI Chatbot")

# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# llm initiate
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

# input box
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
"""


import streamlit as st
from dotenv import load_dotenv

from model_router import get_model, smart_route, get_groq, get_gemini
from app import setup_ui, sidebar_controls, display_chat

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import time

load_dotenv()

setup_ui()

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

mode, selected_model = sidebar_controls()

display_chat(st.session_state.chat_history)

user_input = st.chat_input("Ask something...")

def convert_messages(chat_history):
    messages = [SystemMessage(content="You are a helpful assistant")]
    for msg in chat_history:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))
    return messages


if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    messages = convert_messages(st.session_state.chat_history)

    try:
        # 🔥 MODE HANDLING
        if mode == "Manual":
            llm = get_model(selected_model)
            response = llm.invoke(messages).content

        elif mode == "Smart Router":
            llm = smart_route(user_input)
            response = llm.invoke(messages).content

        elif mode == "Compare":
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Groq")
                response_groq = get_groq().invoke(messages).content
                st.write(response_groq)

            with col2:
                st.subheader("Gemini")
                response_gemini = get_gemini().invoke(messages).content
                st.write(response_gemini)

            response = "Compared responses shown above."

        # ✨ Typing effect
        if mode != "Compare":
            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_text = ""
                for word in response.split():
                    full_text += word + " "
                    placeholder.markdown(full_text)
                    time.sleep(0.02)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": response}
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")