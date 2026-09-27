# ============================================================
# CODSOFT - AI INTERNSHIP
# Task 2: Tic-Tac-Toe AI
# Algorithm: Minimax
# ============================================================
import math
# ------------------------------------------------------------
# Game Board
# ------------------------------------------------------------
board = [" " for _ in range(9)]
HUMAN = "X"
AI = "O"
# ------------------------------------------------------------
# Display Board
# ------------------------------------------------------------
def print_board():
    print("\n")
    print("     |     |     ")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("     |     |     ")
    print("\n")

# ------------------------------------------------------------
# Display Position Guide
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
# Winning Combinations
# ------------------------------------------------------------
winning_combinations = [
    (0, 1, 2),  # Top row
    (3, 4, 5),  # Middle row
    (6, 7, 8),  # Bottom row

    (0, 3, 6),  # Left column
    (1, 4, 7),  # Middle column
    (2, 5, 8),  # Right column

    (0, 4, 8),  # Main diagonal
    (2, 4, 6)   # Other diagonal
]
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

    # If there are no empty spaces, it is a draw
    if " " not in board:
        return "draw"

    return None

# ------------------------------------------------------------
# Get Available Moves
# ------------------------------------------------------------
def get_available_moves():
    return [
        i for i in range(9)
        if board[i] == " "
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

            # Check valid range
            if position < 0 or position > 8:
                print("Please enter a number between 1 and 9.")
                continue

            # Check whether position is already occupied
            if board[position] != " ":
                print("That position is already occupied.")
                continue

            # Place human move
            board[position] = HUMAN

            break

        except ValueError:
            print("Invalid input.")
            print("Please enter a number between 1 and 9.")
# ------------------------------------------------------------
# Minimax Algorithm
# ------------------------------------------------------------
def minimax(is_maximizing):

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

            # Make AI move
            board[move] = AI

            # Recursively evaluate position
            score = minimax(False)

            # Undo move
            board[move] = " "

            best_score = max(
                best_score,
                score
            )

        return best_score

    # --------------------------------------------------------
    # Minimizing Player - Human
    # --------------------------------------------------------

    else:

        best_score = math.inf

        for move in get_available_moves():

            # Make human move
            board[move] = HUMAN

            # Recursively evaluate position
            score = minimax(True)

            # Undo move
            board[move] = " "

            best_score = min(
                best_score,
                score
            )

        return best_score
    
# ------------------------------------------------------------
# Find Best AI Move
# ------------------------------------------------------------
def get_best_move():

    best_score = -math.inf
    best_move = None

    for move in get_available_moves():

        # Try AI move
        board[move] = AI

        # Calculate score
        score = minimax(False)

        # Undo move
        board[move] = " "

        # Keep best move
        if score > best_score:

            best_score = score
            best_move = move

    return best_move

# ------------------------------------------------------------
# AI Move
# ------------------------------------------------------------
def ai_move():

    print("AI is thinking...")

    move = get_best_move()

    if move is not None:
        board[move] = AI

    print(f"AI selected position {move + 1}.")

# ------------------------------------------------------------
# Game Instructions
# ------------------------------------------------------------
def print_instructions():

    print("\n" + "=" * 50)
    print("       TIC-TAC-TOE AI")
    print("=" * 50)

    print("\nYou are X.")
    print("AI is O.")

    print("\nThe AI uses the Minimax algorithm.")
    print("Try to defeat the AI!")

    print_position_guide()

# ------------------------------------------------------------
# Play One Game
# ------------------------------------------------------------

def play_game():

    global board

    # Reset board
    board = [" " for _ in range(9)]

    print_instructions()

    # Randomly, AI could start, but for simplicity
    # the human starts first.

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
            print("🤖 AI wins! Better luck next time.")
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

        print("\n" + "=" * 50)

        choice = input(
            "Do you want to play again? (y/n): "
        ).strip().lower()

        if choice != "y":
            print("\nThank you for playing Tic-Tac-Toe AI!")
            print("Good luck with your CodSoft internship!")
            break

# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()