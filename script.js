document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') sendMessage();
});

async function sendMessage() {
    const inputField = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const message = inputField.value.trim();

    if (!message) return;

    // Append User Message
    appendMessage('User', message);
    inputField.value = '';

    try {
        // Replace with your deployed URL if not running locally
        const response = await fetch('/chatbot', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: message })
        });

        const botResponse = await response.text();
        appendMessage('Bot', botResponse);
    } catch (error) {
        appendMessage('Error', 'Could not connect to the server.');
        console.error(error);
    }
}

function appendMessage(sender, text) {
    const chatBox = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message');
    msgDiv.classList.add(sender.toLowerCase());
    msgDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
