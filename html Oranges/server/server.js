// import { initializeBenevOranges } from "./server/benev-oranges";
// import { createRoom } from "../server/room";

const io = require('socket.io')(8080);

io.on('connection', socket =>{
  socket.on('send-chat-message', message => {
    socket.broadcast.emit('chat-message', 'hello world');
  })
})







// const http = require('http');
// const express = require('express');

// const app = express();
// app.use(express.static(`${__dirname}/../client`))
// ;
// const server = http.createServer(app);

server.on('error', (err) => {
  console.error(err);
});

// server.listen(3000, () => {
//   console.log('server is ready');
// })




/*

const io = require("socket.io")(server);

const PORT = process.env.PORT || 3001;
const path = require("path");

app.use(express.static(path.join(__dirname, "..", "build")));
app.use(express.json());
app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "..", "build", "index.html"));
});
app.get("/create", function (req, res) {
  res.sendFile(path.join(__dirname, "..", "build", "index.html"));
});
app.get("/game/*", function (req, res) {
  res.sendFile(path.join(__dirname, "..", "build", "index.html"));
});

app.post("/create-new-game", function (req, res, next) {
  const roomCode = createRoom(req.body);
  res.send(roomCode);
});

initializeBenevOranges(io);

// start the app
server.listen(PORT, (error) => {
  if (error) {
    return console.log("something bad happened", error);
  }
  console.log("listening on " + PORT + "...");
});

*/

