console.log("🔥 chat.js loaded");

const chatContainer = document.getElementById("chat");
const input = document.getElementById("message");
const sendBtn = document.getElementById("send");
const sessionList = document.getElementById("session-list");
const newChatBtn = document.getElementById("new-chat");

let sessionId = localStorage.getItem("session_id");

if (!sessionId) {
  sessionId = crypto.randomUUID();
  localStorage.setItem("session_id", sessionId);
}

function clearChat() {
  chatContainer.innerHTML = "";
}

function scrollDown() {
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

function setSending(isSending) {
  input.disabled = isSending;
  sendBtn.disabled = isSending;
}

function addMessage(role, text) {
  const msg = document.createElement("div");
  msg.className = `message ${role}`;

  const bubble = document.createElement("span");
  bubble.textContent = text;

  msg.appendChild(bubble);
  chatContainer.appendChild(msg);
  scrollDown();
}

function showTyping() {
  if (document.getElementById("typing")) return;

  const msg = document.createElement("div");
  msg.id = "typing";
  msg.className = "message bot";

  const bubble = document.createElement("span");
  bubble.className = "typing";

bubble.className = 'typing-status-message'; 
bubble.innerHTML = `
  <div class="typing-flex-container">
    <span class="typing-text">Assistant is typing</span>
    <div class="mini-dots">
      <span></span><span></span><span></span>
    </div>
  </div>
`;

  msg.appendChild(bubble);
  chatContainer.appendChild(msg);
  scrollDown();
}

function hideTyping() {
  const t = document.getElementById("typing");
  if (t) t.remove();
}

async function loadSessions() {
  try {
    const res = await fetch("/v1/sessions");
    if (!res.ok) return;

    const data = await res.json();
    sessionList.innerHTML = "";

    data.sessions.forEach((s) => {
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
  } catch (err) {
    console.log("loadSessions error:", err);
  }
}

async function loadSession(id) {
  sessionId = id;
  localStorage.setItem("session_id", id);

  try {
    const res = await fetch(`/v1/sessions/${id}`);
    if (!res.ok) return;

    const data = await res.json();

    clearChat();
    data.messages.forEach((m) => addMessage(m.role, m.content));

    document.querySelectorAll(".session-item").forEach((li) => {
      li.classList.toggle("active", li.dataset.id === id);
    });

    scrollDown();
  } catch (err) {
    console.log("loadSession error:", err);
  }
}

async function deleteSession(id) {
  try {
    await fetch(`/v1/sessions/${id}`, { method: "DELETE" });

    if (id === sessionId) {
      sessionId = crypto.randomUUID();
      localStorage.setItem("session_id", sessionId);
      clearChat();
    }

    loadSessions();
  } catch (err) {
    console.log("deleteSession error:", err);
  }
}

async function restoreLastSession() {
  const saved = localStorage.getItem("session_id");
  if (!saved) return;

  try {
    const res = await fetch(`/v1/sessions/${saved}`);
    if (!res.ok) return;

    const data = await res.json();
    clearChat();
    data.messages.forEach((m) => addMessage(m.role, m.content));
    scrollDown();
  } catch (err) {
    console.log("restoreLastSession error:", err);
  }
}

function typeBotMessage(text) {
  const msg = document.createElement("div");
  msg.className = "message bot";

  const bubble = document.createElement("span");
  msg.appendChild(bubble);
  chatContainer.appendChild(msg);

  let i = 0;

  function typeNext() {
    if (i < text.length) {
      bubble.textContent += text.charAt(i);
      i++;
      scrollDown();
      setTimeout(typeNext, 18);
    } else {
      setSending(false);
      input.focus();
    }
  }

  typeNext();
}

async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  addMessage("user", text);
  input.value = "";
  setSending(true);
  showTyping();

  try {
    const res = await fetch("/v1/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: sessionId, message: text }),
    });

    if (!res.ok) {
      throw new Error("Bad response: " + res.status);
    }

    const data = await res.json();

    hideTyping();

    const reply = data.assistant_message || data.reply || data.message || "";
    typeBotMessage(reply || "No response.");

    loadSessions();
  } catch (err) {
    console.log("sendMessage error:", err);
    hideTyping();
    addMessage("bot", "⚠️ Error contacting server.");
    setSending(false);
    input.focus();
  }
}


newChatBtn.onclick = () => {
  sessionId = crypto.randomUUID();
  localStorage.setItem("session_id", sessionId);
  clearChat();
  loadSessions();
};

sendBtn.onclick = sendMessage;

input.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

loadSessions();
restoreLastSession();
