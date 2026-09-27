# 🎮 Tic-Tac-Toe AI

A console-based Tic-Tac-Toe game where a human player competes against an AI agent powered by the Minimax algorithm.

## 📌 CodSoft Artificial Intelligence Internship

**Task:** Task 2 - Tic-Tac-Toe AI

The objective of this project is to implement an AI agent that can play Tic-Tac-Toe against a human player using the Minimax algorithm.

## 🚀 Features

- Human vs AI gameplay
- AI powered by the Minimax algorithm
- Automatic winner detection
- Draw detection
- Input validation
- Invalid move handling
- Replay option
- Position guide for players
- Unbeatable AI for standard Tic-Tac-Toe

## 🧠 Algorithm

The project uses the **Minimax algorithm**, a recursive decision-making algorithm commonly used in two-player games.

The algorithm evaluates possible future game states:

- AI win → `+1`
- Draw → `0`
- Human win → `-1`

The AI evaluates possible moves and selects the move with the highest score.

## 🎮 How to Play

The player uses:

`X`

The AI uses:

`O`

Choose a position from `1` to `9`.

Example:

```text
     |     |
  1  |  2  |  3
_____|_____|_____
     |     |
  4  |  5  |  6
_____|_____|_____
     |     |
  7  |  8  |  9
     |     |