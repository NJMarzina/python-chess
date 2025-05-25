# This script uses the `chess` library to create a standard chess board,
# display it, and count the number of legal moves available.

import chess

# Create a standard chess board
board = chess.Board()

# Show the board
print("Chess board:")
print(board)

# Show how many moves are possible
print(f"Number of legal moves: {len(list(board.legal_moves))}")