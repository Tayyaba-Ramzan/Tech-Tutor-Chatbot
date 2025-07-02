# 🧠 Tech Tutor Chatbot 🤖
> _“Your personal AI-powered technical instructor – built for developers, by a developer.”_


![Chainlit](https://img.shields.io/badge/Chainlit-Framework-6A5ACD?logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/API-Gemini-blue)
![Python](https://img.shields.io/badge/Built%20With-Python%203.11-yellow)
![Chainlit](https://img.shields.io/badge/UI%20Framework-Chainlit-orange)
![Status](https://img.shields.io/badge/Status-Ready%20for%20Deployment-brightgreen)


---

## 🚀 Project Overview

**Tech Tutor Chatbot** is a W3Schools-style AI instructor built using **Chainlit** and **Google's Gemini API**. It helps users learn and ask questions about all core technical topics like:

- ✅ Python, JavaScript, HTML, CSS, SQL, C++, Java, Bash, Git
- ✅ Loops, variables, data types, DOM, APIs, regex, JSON
- ❌ No off-topic responses (e.g., love, politics, religion)

💡 The chatbot **remembers previous questions**, avoids off-topic queries, and explains with **clean, structured code examples**.

---

## 🏗️ Tech Stack

| Layer        | Tools / Tech                          |
|--------------|----------------------------------------|
| 🧠 AI Model  | Gemini 2.0 Flash (via Google API)      |
| 💬 Frontend  | Chainlit (`@cl.on_message`, streaming) |
| 🐍 Backend   | Python 3.11                            |
| 🔐 Secrets   | `python-dotenv` for API Key Management |

---

👋 Hello! I'm your technical tutor. Ask me anything related to tech (like Python, HTML, SQL, etc).

You: What is a Python list?
Bot: A list in Python is a mutable, ordered collection. Example:

my_list = [1, 2, 3]
print(my_list[0])  # Output: 1


---

## 🛠️ Setup Instructions

> Make sure you have Python 3.11+ installed and your `GEMINI_API_KEY`.

### 1. Clone the Repo

```bash
git clone https://github.com/Tayyaba-Ramzan/Tech-Tutor-Chatbot.git

2. Create & Activate Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Add .env File
Create a .env file in root with:
GEMINI_API_KEY=your_actual_api_key_here

5. Run the Chatbot 🚀
chainlit run main.py
Then open the browser link (usually http://localhost:8000)

💡 Features
✅ Handles a wide variety of programming topics

✅ Stateless UI with cl.user_session memory

✅ API-secured with .env for safety

✅ Non-technical queries are rejected politely

✅ Fast response via Runner.run() 

❌ What This Bot Won’t Do
❌ Answer personal, emotional, or religious questions

❌ Discuss politics, gossip, celebrities

❌ Get distracted – it's only a tech tutor 😎

📁 File Structure

tech-tutor-chatbot/
│
├── main.py               # Chatbot logic with Chainlit
├── .env                  # API key stored here
├── requirements.txt      # Python dependencies
└── README.md             # You’re here!

🙌 Acknowledgements
Chainlit – Conversational UI for Python agents

Gemini API – LLM from Google

W3Schools – Inspiration for topic coverage

🏁 Final Words
Built with 💻, ❤️, and ☕ by a developer who believes tech education should be accessible, clean, and AI-powered.

If this project helped you or inspired you — ⭐ star it, fork it, or use it in your next bootcamp or classroom.


