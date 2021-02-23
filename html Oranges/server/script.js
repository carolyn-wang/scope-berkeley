messageForm.addEventListener('submit', e=>{
    e.preventDefault();
    const message = messageInput.nodeValue;
    socket.emit('send-chat-message', message);
})

const socket = io.connect('client/game.html');
const messageForm = document.getElementById('send-container');
const messageInput = document.getElementById('message-input');
socket.on('chat-message', data =>{
    console.log(data)
})

// const socket = io.connect('client/join-game.html');
// const messageForm = document.getElementById('send-container');
// const messageInput = document.getElementById('message-input');
// socket.on('chat-message', data =>{
//     console.log(data)
// })