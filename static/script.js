document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("prompt-form");
  const input = document.getElementById("prompt-input");
  const chatWindow = document.getElementById("chat-window");

  // Load conversation history
  fetch("/history")
    .then(res => res.json())
    .then(data => {
      data.forEach(msg => {
        addMessage("user", msg.user),
        addMessage("bot", msg.bot)
      });
    });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const prompt = input.value.trim();
    if (!prompt) return;

    addMessage("user", prompt);

    const formData = new FormData();
    formData.append("prompt", prompt);

    const res = await fetch("/prompt", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    addMessage("bot", data["Extracted prompt"]);

    // ✅ Display generated image
    if (data.image_data) {
      const img = document.createElement("img");
      img.src = data.image_data;
      img.style.maxWidth = "300px";
      img.style.marginTop = "10px";
      chatWindow.appendChild(img);

      // ✅ Optional: Add download button
      const a = document.createElement("a");
      a.href = data.image_data;
      a.download = "generated.png";
      a.textContent = "Download Image";
      a.style.display = "block";
      a.style.marginBottom = "20px";
      chatWindow.appendChild(a);
    }

    input.value = "";
  });

  function addMessage(sender, text) {
    const div = document.createElement("div");
    div.className = `chat-message ${sender}`;
    div.innerText = text;
    chatWindow.appendChild(div);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
});
