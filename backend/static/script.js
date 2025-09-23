const form = document.getElementById('chat-form');
const chatBox = document.getElementById('chat-box');
const promptInput = document.getElementById('prompt');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const prompt = promptInput.value.trim();
    if (!prompt) return;

    // Display user's message
    const userMsg = document.createElement('div');
    userMsg.className = 'message user';
    userMsg.innerHTML = `<strong>You:</strong> ${prompt}`;
    chatBox.appendChild(userMsg);

    // Clear input
    promptInput.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send request to backend
    const formData = new FormData();
    formData.append('prompt', prompt);

    const response = await fetch('/generate', {
        method: 'POST',
        body: formData
    });

    const html = await response.text();

    // Parse returned HTML and extract bot message
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const botMsgText = doc.querySelector('.message.bot')?.innerHTML;

    if (botMsgText) {
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot';
        botMsg.innerHTML = botMsgText;
        chatBox.appendChild(botMsg);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
