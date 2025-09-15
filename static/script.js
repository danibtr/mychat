const socket = io();

function sendMessage() {
    const msgInput = document.getElementById('msg');
    const message = msgInput.value;
    socket.emit('send_message', { user: 'User', message });
    msgInput.value = '';
}

socket.on('receive_message', data => {
    const box = document.getElementById('chat-box');
    const div = document.createElement('div');
    div.innerText = `${data.user}: ${data.message}`;
    box.appendChild(div);
});
