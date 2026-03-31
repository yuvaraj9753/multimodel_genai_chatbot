from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI


def get_groq():
    return ChatGroq(model="llama-3.3-70b-versatile")


def get_gemini():
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash")


def get_model(model_name):
    if model_name == "Groq":
        return get_groq()
    elif model_name == "Gemini":
        return get_gemini()


def smart_route(prompt):
    prompt = prompt.lower()

    if "code" in prompt or "python" in prompt:
        return get_groq()
    else:
        return get_gemini()