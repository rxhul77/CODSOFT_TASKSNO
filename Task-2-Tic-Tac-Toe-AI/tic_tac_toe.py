import tkinter as tk
from tkinter import messagebox


class TicTacToeAI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI")
        self.window.resizable(False, False)

        self.board = [""] * 9
        self.human = "X"
        self.ai = "O"
        self.game_over = False

        self.create_interface()

    def create_interface(self):
        title = tk.Label(
            self.window,
            text="TIC-TAC-TOE AI",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=(15, 5))

        self.status_label = tk.Label(
            self.window,
            text="Your Turn - You are X",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=5)

        board_frame = tk.Frame(self.window)
        board_frame.pack(padx=15, pady=10)

        self.buttons = []

        for i in range(9):
            button = tk.Button(
                board_frame,
                text="",
                font=("Arial", 24, "bold"),
                width=4,
                height=2,
                command=lambda index=i: self.human_move(index)
            )
            button.grid(
                row=i // 3,
                column=i % 3,
                padx=2,
                pady=2
            )
            self.buttons.append(button)

        reset_button = tk.Button(
            self.window,
            text="New Game",
            font=("Arial", 12, "bold"),
            command=self.reset_game
        )
        reset_button.pack(pady=(5, 15))

    def human_move(self, position):
        if self.game_over or self.board[position] != "":
            return

        self.board[position] = self.human
        self.buttons[position].config(text=self.human)

        if self.check_winner(self.board, self.human):
            self.end_game("You Win!")
            return

        if self.is_board_full(self.board):
            self.end_game("It's a Draw!")
            return

        self.status_label.config(text="AI is thinking...")
        self.window.after(300, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return

        best_score = float("-inf")
        best_move = None

        for position in range(9):
            if self.board[position] == "":
                self.board[position] = self.ai

                score = self.minimax(
                    self.board,
                    0,
                    False,
                    float("-inf"),
                    float("inf")
                )

                self.board[position] = ""

                if score > best_score:
                    best_score = score
                    best_move = position

        if best_move is not None:
            self.board[best_move] = self.ai
            self.buttons[best_move].config(text=self.ai)

        if self.check_winner(self.board, self.ai):
            self.end_game("AI Wins!")
            return

        if self.is_board_full(self.board):
            self.end_game("It's a Draw!")
            return

        self.status_label.config(text="Your Turn - You are X")

    def minimax(self, board, depth, maximizing, alpha, beta):
        if self.check_winner(board, self.ai):
            return 10 - depth

        if self.check_winner(board, self.human):
            return depth - 10

        if self.is_board_full(board):
            return 0

        if maximizing:
            best_score = float("-inf")

            for position in range(9):
                if board[position] == "":
                    board[position] = self.ai

                    score = self.minimax(
                        board,
                        depth + 1,
                        False,
                        alpha,
                        beta
                    )

                    board[position] = ""

                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)

                    if beta <= alpha:
                        break

            return best_score

        else:
            best_score = float("inf")

            for position in range(9):
                if board[position] == "":
                    board[position] = self.human

                    score = self.minimax(
                        board,
                        depth + 1,
                        True,
                        alpha,
                        beta
                    )

                    board[position] = ""

                    best_score = min(best_score, score)
                    beta = min(beta, best_score)

                    if beta <= alpha:
                        break

            return best_score

    def check_winner(self, board, player):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_combinations:
            if board[a] == player and board[b] == player and board[c] == player:
                return True

        return False

    def is_board_full(self, board):
        return all(cell != "" for cell in board)

    def end_game(self, message):
        self.game_over = True
        self.status_label.config(text=message)
        messagebox.showinfo("Game Over", message)

    def reset_game(self):
        self.board = [""] * 9
        self.game_over = False

        for button in self.buttons:
            button.config(text="")

        self.status_label.config(text="Your Turn - You are X")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToeAI()
    game.run()