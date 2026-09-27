# 🎮 Tic-Tac-Toe AI

An AI-powered console-based Tic-Tac-Toe game where a human player competes against an intelligent AI agent.

The AI agent uses the **Minimax algorithm with Alpha-Beta Pruning** to evaluate possible game states and select the optimal move.

## 📌 CodSoft Artificial Intelligence Internship

**Task:** Task 2 — Tic-Tac-Toe AI

The objective of this project is to implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player.

## 🚀 Features

* Human vs AI gameplay
* AI agent using Minimax
* Alpha-Beta Pruning optimization
* Automatic winner detection
* Draw detection
* Input validation
* Invalid move handling
* Replay option
* Position guide
* Optimal AI decision-making

## 🧠 AI Algorithm

### Minimax

Minimax is a recursive decision-making algorithm used in two-player, zero-sum games.

The algorithm explores possible future game states and evaluates them from the perspective of both players.

The scoring system used in this project is:

```text
AI wins      → +1
Draw         →  0
Human wins   → -1
```

The AI attempts to maximize its score, while the human player's simulated moves attempt to minimize it.

### Alpha-Beta Pruning

Alpha-Beta Pruning improves the Minimax algorithm by eliminating branches of the game tree that cannot affect the final decision.

This reduces unnecessary calculations while preserving the same optimal result.

The algorithm maintains two values:

```text
Alpha → Best value found for the maximizing player

Beta  → Best value found for the minimizing player
```

When:

```text
Beta <= Alpha
```

the remaining branch can be skipped.

## 🎮 How to Play

You play as:

```text
X
```

The AI plays as:

```text
O
```

Choose a position from `1` to `9`.

### Position Guide

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
```

For example, entering:

```text
5
```

places your `X` in the center.

## 🛠️ Technologies Used

* Python
* Minimax Algorithm
* Alpha-Beta Pruning
* Recursion
* Game Theory

## ▶️ How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project:

```bash
cd Task-2-Tic-Tac-Toe-AI
```

Run the application:

```bash
python tic_tac_toe.py
```

## 📂 Project Structure

```text
Task-2-Tic-Tac-Toe-AI/
│
├── tic_tac_toe.py
├── README.md
├── requirements.txt
│
└── screenshots/
    ├── game-start.png
    ├── gameplay.png
    └── game-result.png
```

## 🎯 Learning Outcomes

Through this project, I learned:

* How to implement an AI agent for a game
* How the Minimax algorithm works
* How Alpha-Beta Pruning optimizes game-tree search
* How recursive algorithms can be used for decision-making
* How game states can be evaluated
* How AI agents select optimal actions
* How to handle user input and game states
* How to structure and document an AI project

## 📸 Demo

The project includes screenshots demonstrating:

* Game initialization
* Human vs AI gameplay
* Game completion

A video demonstration will also be provided as part of the CodSoft internship submission.

## 👨‍💻 Author

**Rahul**

Built as part of the **CodSoft Artificial Intelligence Internship**.
