📌 AI Chatbot with Local LLM (Ollama)

A full-stack AI chatbot built with Flask, SQLite, Docker, and Ollama, featuring persistent chat sessions, auto-generated titles, and a modern sidebar UI.

This project runs entirely locally using a free LLM (no paid APIs required), with optional OpenAI support for future use.

✨ Features

🤖 AI chatbot powered by Ollama (LLaMA 3)

💾 Persistent chat history using SQLite

🗂️ Sidebar with chat sessions

🏷️ Auto-generated chat titles

🗑️ Delete individual chats

🔄 Restore last session on refresh

⚡ Typing animation & smooth UI

🐳 Fully Dockerized

🔌 Pluggable LLM backend (Ollama now, OpenAI later)

🛠 Tech Stack

Frontend

HTML, CSS, Vanilla JavaScript

Backend

Python (Flask)

SQLite

AI / LLM

Ollama (LLaMA 3)

DevOps

Docker & Docker Compose

🚀 Getting Started (Local)
1️⃣ Install Ollama
brew install ollama
ollama run llama3

2️⃣ Clone the repo
git clone https://github.com/your-username/ai-chatbot-flask.git
cd ai-chatbot-flask

3️⃣ Run with Docker
docker compose up --build

4️⃣ Open in browser
http://localhost:8000/ui

📂 Project Structure
ai-chatbot-flask/
├── app/
│   ├── routes/
│   ├── storage/
│   ├── openai_client.py
│   └── __init__.py
├── static/
│   ├── chat.js
│   └── style.css
├── templates/
│   └── index.html
├── docker-compose.yml
├── Dockerfile
├── .env
└── README.md

🔮 Roadmap (Upcoming Features)

🌗 Light / Dark themes

🖼️ Image upload support

📡 Streaming responses

🔐 Authentication

☁️ Cloud deployment

🤝 OpenAI model toggle

📸 Screenshots

See screenshots below 👇

🧑‍💻 Author

Vidisha Sodha
Built as a full-stack + AI learning project.