import { getRandomPG13Prompt } from "./generated-data/Prompts.pg13";
import { getRandomPicturePrompt } from "./generated-data/Prompts.pics";

const POINTS_PER_VOTE = 100;
const promptsForRoom = {};

// Keep track of how many answers are submitted.  Wait until all answers are in before starting game.
const numberOfAnswersForRoom = {};
// Keep track of prompts that haven't been displayed and voted on yet.
const unusedPromptsForRoom = {};
// Keep track of winning answers for the score screen
const winningAnswersForRoom = {};

export function deleteSavedPromptsForRoom(roomCode) {
  delete numberOfAnswersForRoom[roomCode];
  delete promptsForRoom[roomCode];
  delete unusedPromptsForRoom[roomCode];
  delete winningAnswersForRoom[roomCode];
}

export function getNumberOfAnswersForRoom(roomCode) {
  return numberOfAnswersForRoom[roomCode];
}

export function hasMorePromptsForRoom(roomCode) {
  return unusedPromptsForRoom[roomCode].length > 0;
}

export function storeAnswerForPrompt({ prompt, playerName, answer, roomCode }) {
  numberOfAnswersForRoom[roomCode]++;
  if (promptsForRoom[roomCode] && promptsForRoom[roomCode][prompt]) {
    let realAnswer = answer;
    // Check for duplicate answer and add ditto to it
    if (promptsForRoom[roomCode][prompt][answer]) {
      realAnswer = answer + " ditto";
    }
    promptsForRoom[roomCode][prompt][realAnswer] = {};
    promptsForRoom[roomCode][prompt][realAnswer].submitter = playerName;
  }
}

export function storeVoteForPrompt({ prompt, playerName, roomCode, answerVotedFor }) {
  if (!promptsForRoom[roomCode][prompt][answerVotedFor].votes) {
    promptsForRoom[roomCode][prompt][answerVotedFor].votes = [];
  }
  promptsForRoom[roomCode][prompt][answerVotedFor].votes.push(playerName);
}
