# 🤖 Multi-Model AI Chatbot (Groq + Gemini)

A powerful **Streamlit-based chatbot** that lets you interact with multiple LLMs (Groq & Gemini) with flexible modes like **Manual Selection**, **Smart Routing**, and **Model Comparison**.

---

## 🚀 Features

### 🔹 Multi-Model Support

* **Groq (LLaMA 3.3 70B)** for fast and powerful responses
* **Google Gemini (2.5 Flash)** for general-purpose tasks

---

### 🔹 Smart Router Mode

Automatically selects the best model:

* 🧠 Coding / technical queries → **Groq**
* 💬 General queries → **Gemini**

---

### 🔹 Manual Mode

* Choose which model you want to use manually from the sidebar

---

### 🔹 Compare Mode

* See responses from **both models side-by-side**
* Helps evaluate performance and accuracy

---

### 🔹 Chat Features

* 🗂 Chat history maintained using session state
* ✨ Typing animation effect for responses
* 📥 Export chat as `.txt` file
* 🗑 Clear chat instantly

---

## 📁 Project Structure

```
📦 project
 ┣ 📜 main.py              # Main Streamlit app logic
 ┣ 📜 model_router.py     # Model selection & smart routing
 ┣ 📜 app.py              # UI components & sidebar controls
 ┣ 📜 .env                # API keys (NOT pushed to GitHub)
 ┣ 📜 requirements.txt    # Dependencies
 ┗ 📜 README.md           # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/multi-llm-chatbot.git
cd multi-llm-chatbot
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

⚠️ **Important:**

* Never push `.env` to GitHub
* Make sure `.gitignore` includes `.env`

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 🧠 How It Works

### ✔ Model Routing Logic

```python
def smart_route(prompt):
    prompt = prompt.lower()

    if "code" in prompt or "python" in prompt:
        return get_groq()
    else:
        return get_gemini()
```

---

## 📸 UI Overview

* Sidebar for settings ⚙️
* Chat interface similar to ChatGPT 💬
* Compare mode with split screen 📊

---

## 🔒 Deployment Tip

If your app fails after deployment:

* Ensure API keys are added in platform environment variables (e.g., Streamlit Cloud, Render)
* Do NOT rely on `.env` in production

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **LLMs:** Groq (LLaMA 3), Google Gemini
* **Framework:** LangChain
* **Language:** Python

---

## 📌 Future Improvements

* Add more models (OpenAI, Claude, Mistral)
* Streaming responses instead of simulated typing
* Chat history database (MongoDB / SQLite)
* User authentication

---


⭐ If you like this project, don't forget to star the repo!
