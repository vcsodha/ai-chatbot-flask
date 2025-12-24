console.log("🔥 chat.js loaded");

const chatContainer = document.getElementById("chat");
const input = document.getElementById("message");
const sendBtn = document.getElementById("send");
const sessionList = document.getElementById("session-list");
const newChatBtn = document.getElementById("new-chat");

/* ---------- Session ---------- */
let sessionId = localStorage.getItem("session_id");
if (!sessionId) {
  sessionId = crypto.randomUUID();
  localStorage.setItem("session_id", sessionId);
}

/* ---------- Helpers ---------- */
function clearChat() {
  chatContainer.innerHTML = "";
}

function addMessage(role, text) {
  const msg = document.createElement("div");
  msg.className = `message ${role}`;

  const bubble = document.createElement("span");
  bubble.textContent = text;

  msg.appendChild(bubble);
  chatContainer.appendChild(msg);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

/* ---------- Typing Indicator ---------- */
function showTyping() {
  const div = document.createElement("div");
  div.id = "typing";
  div.className = "typing";
  div.textContent = "Bot is typing...";
  chatContainer.appendChild(div);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

function hideTyping() {
  const t = document.getElementById("typing");
  if (t) t.remove();
}

/* ---------- Sidebar ---------- */
async function loadSessions() {
  const res = await fetch("/v1/sessions");
  const data = await res.json();

  sessionList.innerHTML = "";

  data.sessions.forEach(s => {
    const li = document.createElement("li");
    li.className = "session-item";
    li.dataset.id = s.id;

    if (s.id === sessionId) li.classList.add("active");

    const title = document.createElement("span");
    title.className = "session-title";
    title.textContent = s.title || "New chat";
    title.onclick = () => loadSession(s.id);

    const del = document.createElement("button");
    del.className = "delete-btn";
    del.textContent = "🗑️";
    del.onclick = async (e) => {
      e.stopPropagation();
      await deleteSession(s.id);
    };

    li.appendChild(title);
    li.appendChild(del);
    sessionList.appendChild(li);
  });
}

async function loadSession(id) {
  sessionId = id;
  localStorage.setItem("session_id", id);

  const res = await fetch(`/v1/sessions/${id}`);
  if (!res.ok) return;

  const data = await res.json();

  clearChat();
  data.messages.forEach(m => addMessage(m.role, m.content));

  document.querySelectorAll(".session-item").forEach(li => {
    li.classList.toggle("active", li.dataset.id === id);
  });
}

async function deleteSession(id) {
  await fetch(`/v1/sessions/${id}`, { method: "DELETE" });

  if (id === sessionId) {
    sessionId = crypto.randomUUID();
    localStorage.setItem("session_id", sessionId);
    clearChat();
  }

  loadSessions();
}

/* ---------- Restore history on reload ---------- */
async function restoreLastSession() {
  const saved = localStorage.getItem("session_id");
  if (!saved) return;

  try {
    const res = await fetch(`/v1/sessions/${saved}`);
    if (!res.ok) return;

    const data = await res.json();
    clearChat();
    data.messages.forEach(m => addMessage(m.role, m.content));
  } catch {
    console.warn("No previous session to restore");
  }
}

/* ---------- Bot typing animation ---------- */
function typeBotMessage(text) {
  const msg = document.createElement("div");
  msg.className = "message bot";

  const bubble = document.createElement("span");
  msg.appendChild(bubble);
  chatContainer.appendChild(msg);

  let i = 0;
  function type() {
    if (i < text.length) {
      bubble.textContent += text.charAt(i++);
      chatContainer.scrollTop = chatContainer.scrollHeight;
      setTimeout(type, 20);
    } else {
      input.disabled = false;
      sendBtn.disabled = false;
      input.focus();
    }
  }
  type();
}

/* ---------- Send message ---------- */
async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  addMessage("user", text);
  input.value = "";
  input.disabled = true;
  sendBtn.disabled = true;

  showTyping();

  try {
    const res = await fetch("/v1/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: sessionId, message: text })
    });

    const data = await res.json();
    hideTyping();
    typeBotMessage(data.assistant_message);
    loadSessions();
  } catch {
    hideTyping();
    addMessage("bot", "⚠️ Error contacting server.");
    input.disabled = false;
    sendBtn.disabled = false;
  }
}

/* ---------- New chat ---------- */
newChatBtn.onclick = () => {
  sessionId = crypto.randomUUID();
  localStorage.setItem("session_id", sessionId);
  clearChat();
  loadSessions();
};

/* ---------- Events ---------- */
sendBtn.onclick = sendMessage;
input.addEventListener("keydown", e => {
  if (e.key === "Enter") sendMessage();
});

/* ---------- Init ---------- */
loadSessions();
restoreLastSession();