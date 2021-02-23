  
const room = {};

const MAX_NUMBER_OF_PLAYERS = 8;

export function addHostToRoom(roomCode, hostSocketId) {
  room[roomCode].hostSocketId = hostSocketId;
}

export function addPlayerToRoom(roomCode, player) {
  if (room[roomCode]) {
    if (room[roomCode].started) {
      console.warn("Could not add player as game has already started: ", roomCode);
      return false;
    }
    room[roomCode].players.push(player);
    return true;
  }
  console.warn("Could not add player as room was not found: ", roomCode);
  return false;
}

export function addPoints(roomCode, allVotes) {
  for (let vote of allVotes) {
    if (!room[roomCode].points[vote.submitter]) {
      room[roomCode].points[vote.submitter] = 0;
    }
    room[roomCode].points[vote.submitter] += vote.points;
  }
}

export function createRoom(roomOptions) {
  let roomCode;
  do {
    roomCode = "";
    for (var i = 0; i < 4; i++) {
      roomCode += (Math.floor(Math.random()*10))*(i*10);
    }
  } while (room[roomCode]);
  room[roomCode] = { players: [], points: {}, roomOptions };
  return roomCode;
}

export function deleteRoom(roomCode) {
  delete room[roomCode];
}

export function doesPlayerNameAlreadyExist(roomCode, playerName) {
  if (room[roomCode]) {
    return room[roomCode].players.find((player) => player.name === playerName);
  }
  return false;
}

export function getHostSocketIdForRoom(roomCode) {
  // handle case where stale client tries to connect to a past room
  try {
    return room[roomCode].hostSocketId;
  } catch (e) {
    return false;
  }
}

export function getPointsSortedHighestFirst(roomCode) {
  return Object.entries(room[roomCode].points).sort((a, b) => (a[1] > b[1] ? -1 : 1));
}

export function getPlayersOfRoom(roomCode) {
  if (room[roomCode]) {
    return room[roomCode].players;
  }
  return [];
}

export function getRoomOptions(roomCode) {
  return room[roomCode].roomOptions;
}

export function storeStartGame(roomCode) {
  room[roomCode].started = true;
}