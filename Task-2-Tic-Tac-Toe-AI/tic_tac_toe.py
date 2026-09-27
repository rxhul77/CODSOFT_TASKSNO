# ============================================================
# CODSOFT - AI INTERNSHIP
# Task 2: Tic-Tac-Toe AI
# AI Agent: Minimax with Alpha-Beta Pruning
# ============================================================

import math


# ------------------------------------------------------------
# Game Configuration
# ------------------------------------------------------------

HUMAN = "X"
AI = "O"

board = [" " for _ in range(9)]


# ------------------------------------------------------------
# Winning Combinations
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# Display Board
# ------------------------------------------------------------

def print_board():
    print()
    print("     |     |     ")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("     |     |     ")
    print()


# ------------------------------------------------------------
# Position Guide
# ------------------------------------------------------------

def print_position_guide():
    print("\nPosition Guide:")
    print()
    print("     |     |     ")
    print("  1  |  2  |  3  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  4  |  5  |  6  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  7  |  8  |  9  ")
    print("     |     |     ")
    print()


# ------------------------------------------------------------
# Check Winner
# ------------------------------------------------------------

def check_winner():

    for a, b, c in winning_combinations:

        if (
            board[a] == board[b]
            and board[b] == board[c]
            and board[a] != " "
        ):
            return board[a]

    if " " not in board:
        return "draw"

    return None


# ------------------------------------------------------------
# Get Available Moves
# ------------------------------------------------------------

def get_available_moves():

    return [
        index
        for index in range(9)
        if board[index] == " "
    ]


# ------------------------------------------------------------
# Human Move
# ------------------------------------------------------------

def human_move():

    while True:

        try:

            position = int(
                input("Enter your move (1-9): ")
            ) - 1

            if position < 0 or position > 8:

                print(
                    "Please enter a number between 1 and 9."
                )

                continue

            if board[position] != " ":

                print(
                    "That position is already occupied."
                )

                continue

            board[position] = HUMAN

            break

        except ValueError:

            print(
                "Invalid input. Please enter a number between 1 and 9."
            )


# ------------------------------------------------------------
# Minimax with Alpha-Beta Pruning
# ------------------------------------------------------------

def minimax(is_maximizing, alpha, beta):

    result = check_winner()

    # AI wins
    if result == AI:
        return 1

    # Human wins
    if result == HUMAN:
        return -1

    # Draw
    if result == "draw":
        return 0

    # --------------------------------------------------------
    # Maximizing Player - AI
    # --------------------------------------------------------

    if is_maximizing:

        best_score = -math.inf

        for move in get_available_moves():

            board[move] = AI

            score = minimax(
                False,
                alpha,
                beta
            )

            board[move] = " "

            best_score = max(
                best_score,
                score
            )

            alpha = max(
                alpha,
                best_score
            )

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best_score

    # --------------------------------------------------------
    # Minimizing Player - Human
    # --------------------------------------------------------

    else:

        best_score = math.inf

        for move in get_available_moves():

            board[move] = HUMAN

            score = minimax(
                True,
                alpha,
                beta
            )

            board[move] = " "

            best_score = min(
                best_score,
                score
            )

            beta = min(
                beta,
                best_score
            )

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best_score


# ------------------------------------------------------------
# Find Best Move for AI
# ------------------------------------------------------------

def get_best_move():

    best_score = -math.inf
    best_move = None

    for move in get_available_moves():

        board[move] = AI

        score = minimax(
            False,
            -math.inf,
            math.inf
        )

        board[move] = " "

        if score > best_score:

            best_score = score
            best_move = move

    return best_move


# ------------------------------------------------------------
# AI Move
# ------------------------------------------------------------

def ai_move():

    print("🤖 AI is thinking...")

    move = get_best_move()

    if move is not None:

        board[move] = AI

        print(
            f"🤖 AI selected position {move + 1}."
        )


# ------------------------------------------------------------
# Instructions
# ------------------------------------------------------------

def print_instructions():

    print("\n" + "=" * 55)
    print("             TIC-TAC-TOE AI")
    print("=" * 55)

    print("\nYou are: X")
    print("AI is:   O")

    print(
        "\nThe AI uses Minimax with Alpha-Beta Pruning."
    )

    print(
        "Try to defeat the AI!"
    )

    print_position_guide()


# ------------------------------------------------------------
# Play Game
# ------------------------------------------------------------

def play_game():

    global board

    board = [" " for _ in range(9)]

    print_instructions()

    while True:

        # ----------------------------------------------------
        # Human Turn
        # ----------------------------------------------------

        print("Your turn.")

        print_board()

        human_move()

        print_board()

        result = check_winner()

        if result == HUMAN:

            print("🎉 Congratulations! You won!")

            break

        if result == "draw":

            print("🤝 It's a draw!")

            break

        # ----------------------------------------------------
        # AI Turn
        # ----------------------------------------------------

        ai_move()

        print_board()

        result = check_winner()

        if result == AI:

            print(
                "🤖 AI wins! Better luck next time."
            )

            break

        if result == "draw":

            print("🤝 It's a draw!")

            break


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

def main():

    while True:

        play_game()

        print("\n" + "=" * 55)

        choice = input(
            "Do you want to play again? (y/n): "
        ).strip().lower()

        if choice != "y":

            print(
                "\nThank you for playing Tic-Tac-Toe AI!"
            )

            print(
                "Good luck with your CodSoft internship!"
            )

            break


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------

if __name__ == "__main__":
    main()