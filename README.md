# 📌 AI Chatbot with Local LLM (Ollama)

A full-stack AI chatbot built with **Flask**, **SQLite**, **Docker**, and **Ollama**, featuring persistent chat sessions, auto-generated titles, and a modern sidebar UI.

This project runs **entirely locally** using a **free LLM** (no paid APIs required), with optional **OpenAI support** for future use.

Designed as a hands-on project to explore **LLM integration**, **stateful chat UX**, and **production-style architecture**.


## ✨ Features

- 🤖 AI chatbot powered by **Ollama (LLaMA 3)**
- 💾 Persistent chat history using **SQLite**
- 🗂️ Sidebar with chat sessions
- 🏷️ Auto-generated chat titles
- 🗑️ Delete individual chats
- 🔄 Restore last session on refresh
- ⚡ Typing animation & smooth UI
- 🐳 Fully Dockerized
- 🔌 Pluggable LLM backend (Ollama now, OpenAI later)


## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- Vanilla JavaScript

### Backend
- Python (Flask)
- SQLite

### AI / LLM
- Ollama (LLaMA 3)

### DevOps
- Docker
- Docker Compose


## 🚀 Getting Started (Local)

## 1️⃣ Install Ollama
```bash
brew install ollama
ollama run llama3

2️⃣ Clone the repo
git clone https://github.com/vcsodha/ai-chatbot-flask.git
cd ai-chatbot-flask
3️⃣ Run with Docker
bash
Copy code
docker compose up --build
4️⃣ Open in browser
bash
Copy code
http://localhost:8000/ui

🔮 Roadmap (Upcoming Features)
🌗 Light / Dark themes

🖼️ Image upload support

📡 Streaming responses

🔐 Authentication

☁️ Cloud deployment

🤝 OpenAI model toggle

📸 Screenshot
Chat Window & Side Bar with stored history


<img width="754" height="356" alt="Screenshot 2025-12-24 at 14 27 38" src="https://github.com/user-attachments/assets/feb1c3d3-c4e0-46b9-bbb9-919f5a3c4e13" />


🧑‍💻 Author
Vidisha Sodha
Built as a full-stack + AI learning project.
