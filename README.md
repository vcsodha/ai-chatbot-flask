## 📌 AI Chatbot with Pluggable LLMs (Ollama, Mock, OpenAI-ready)


A full-stack AI chatbot built with Flask, SQLite, Docker, and Ollama, featuring persistent chat sessions, auto-generated titles, and a modern sidebar UI.


#### The application supports multiple LLM providers:


Ollama (local, free LLaMA-3)


Mock LLM (for offline development & testing)


OpenAI (planned / optional)


Designed as a hands-on project to explore LLM integration, stateful chat UX, and production-style backend architecture.


### 🔗 Live Demo (UI)


👉 https://ai-chatbot-flask-5p5h.onrender.com/ui


### ⚠️ Important:


The deployed demo showcases UI, sessions, titles, deletion, and persistence AI responses require a running LLM provider


Ollama → local only


Mock provider → works anywhere


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


Clean separation of UI, storage, and LLM providers


Environment-controlled LLM selection (OLLAMA, MOCK, OPENAI)


Designed to be extensible, testable, and production-ready


No hard dependency on paid APIs


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

HTML


CSS


Vanilla JavaScript


#### Backend


Python (Flask)


SQLite


#### AI / LLM


Ollama (LLaMA 3)


Mock LLM (development/testing)


OpenAI (future-ready)


#### DevOps

Docker


Docker Compose


### 🎯 Project Motivation


I built this project to:


Learn how to integrate LLMs into real applications


Design stateful chat UX with persistent sessions


Work with local LLMs instead of paid APIs


Practice clean backend architecture


Build something deployable and extensible


### ⚙️ LLM Providers


The active LLM provider is controlled via environment variables.


#### 🧪 Mock LLM (default-safe)


Best for:


UI development


Testing


Cloud demos


LLM_PROVIDER=mock


#### 🤖 Ollama (local, free)


Requires Ollama running on your machine.


LLM_PROVIDER=ollama


#### ☁️ OpenAI (planned)


Included but intentionally disabled by default.


LLM_PROVIDER=openai


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


Chat UI with persistent sessions ( when using mock LLM) 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/502e6ef5-be8d-48cf-8116-3f220cae1924" />



### 🧑‍💻 Author


Vidisha Sodha


Built as a full-stack + AI learning project.
