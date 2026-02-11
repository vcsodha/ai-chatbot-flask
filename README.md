## 📌 AI Chatbot with Pluggable LLMs (Ollama, Mock, OpenAI-ready)

A full-stack AI chatbot built with Flask, SQLite, Docker, and local LLM inference (Ollama).

It features persistent chat sessions, auto-generated titles, and a modern sidebar UI designed for real-world conversational workflows.

### The application supports multiple LLM providers:

 - Ollama (LLaMA-3) → Local, free AI inference

 - Mock LLM → Offline development, testing, and cloud demos

 - OpenAI (future-ready) → Optional integration prepared but disabled by default

This project explores LLM integration, stateful chat UX, and production-style backend architecture while avoiding mandatory paid API dependencies.


### 🔗 Live Demo (UI)


👉 https://ai-chatbot-flask-5p5h.onrender.com/ui

#### Note: The demo is hosted on a free cloud tier and may take ~30 seconds to spin up on first access.

### ⚠️ Demo Scope:

The hosted demo primarily showcases:

- UI functionality
- Session persistence
- Chat history management
- Title generation and deletion
- Overall application workflow

For actual AI responses:

- Ollama provider → run locally
- Mock provider → works anywhere (demo default)
- This design keeps the project accessible without requiring paid AI services.


### ✨ Features


🤖 AI chatbot with pluggable LLM backends


🧠 Ollama (LLaMA 3) for free, local AI


🧪 Mock LLM provider for testing & offline use


💾 Persistent chat history using SQLite


🗂️ Sidebar with chat sessions


🏷️ Auto-generated chat titles


🗑️ Delete individual chats


🔄 Restore last session on refresh


 ⚡ Typing animation & smooth UX


🐳 Fully Dockerized


🔌 Environment-based LLM switching


### 🧠 Architecture Highlights


- Clean separation of UI, storage, and LLM providers


- Environment-controlled LLM selection (OLLAMA, MOCK, OPENAI)


- Designed to be extensible, testable, and production-ready


- No hard dependency on paid APIs


### 📂 Project Structure

app/
 |--- routes/                    
  API routes (chat, sessions, health)
 
 |--- storage/                 
 SQLite + memory backends
 
 |--- templates/               
  HTML UI
 
 |--- static/                   
  CSS & JavaScript
 
 |--- openai_client.py        
  LLM abstraction layer
 


### 🛠 Tech Stack

#### Frontend

- HTML


- CSS


- Vanilla JavaScript


#### Backend


- Python (Flask)


- SQLite


#### AI / LLM


- Ollama (LLaMA 3)


- Mock LLM (development/testing)


- OpenAI (future-ready)


#### DevOps

- Docker


- Docker Compose


### 🎯 Project Motivation


This project was built to:


- Learn how to integrate LLMs into real applications


- Design stateful chat UX with persistent sessions


- Work with local LLMs instead of paid APIs


- Practice clean backend architecture


- Build something deployable and extensible


### ⚙️ LLM Providers


The active LLM provider is controlled via environment variables.


#### 🧪 Mock LLM (default-safe)


Best for:


- UI development


- Testing


- Cloud demos


- LLM_PROVIDER=mock


#### 🤖 Ollama (local, free)


- Requires Ollama running on your machine.


- LLM_PROVIDER=ollama


#### ☁️ OpenAI (planned)


- Included but intentionally disabled by default.


- LLM_PROVIDER=openai


### 🚀 Getting Started (Local)

1️⃣ Install Ollama (optional)

brew install ollama

ollama run llama3


2️⃣ Clone the repository

git clone https://github.com/vcsodha/ai-chatbot-flask.git

cd ai-chatbot-flask


3️⃣ Run with Docker

docker compose up --build


4️⃣ Open in browser

http://localhost:8000/ui


### 🔮 Roadmap


🌗 Light / Dark themes


🖼️ Image upload support


📡 Streaming responses


🔐 Authentication


☁️ Cloud-hosted LLM support


🤝 OpenAI model toggle


### 📸 Screenshot

- Chat UI with persistent sessions (using Ollama LLM in local mode) 

<img width="500" alt="Screenshot 2026-02-11 at 16 06 45" src="https://github.com/user-attachments/assets/bba42b9f-a5f5-4821-a8d8-e8150b10ae44" />

-----

- Chat UI with persistent sessions (using Mock LLM in demo mode) 

<img width="500" alt="image" src="https://github.com/user-attachments/assets/502e6ef5-be8d-48cf-8116-3f220cae1924" />



### 🧑‍💻 Author


Vidisha Sodha

Software Engineer • AI Engineer

Built as a hands-on project exploring AI integration, backend architecture, and production-ready conversational systems.
