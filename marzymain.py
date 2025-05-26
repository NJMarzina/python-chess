import chess
import chess.engine

import variant1

def display_board_with_coordinates(board):
    """Display the board with file/rank coordinates"""
    print("  a b c d e f g h")
    lines = str(board).split('\n')
    for i, line in enumerate(lines):
        print(f"{8-i} {line} {8-i}")
    print("  a b c d e f g h")

def get_legal_moves_list(board):
    """Get a formatted list of legal moves"""
    moves = list(board.legal_moves)
    return [move.uci() for move in moves]

def play_interactive_game(board_class=chess.Board, variant_name="Standard Chess"):
    """Play an interactive chess game"""
    print(f"=== {variant_name.upper()} - INTERACTIVE GAME ===")
    print("Enter moves in UCI format (e.g., 'e2e4', 'g8f6')")
    print("Special commands:")
    print("  'quit' or 'q' - Exit game")
    print("  'moves' or 'm' - Show all legal moves")
    print("  'help' or 'h' - Show this help")
    print("  'undo' or 'u' - Undo last move")
    print("-" * 50)
    
    # Create the board
    if board_class == chess.Board:
        board = chess.Board()
    else:
        board = board_class()
    
    move_history = []
    
    while True:
        # Display current position
        print(f"\nMove {len(move_history) + 1} - {'White' if board.turn else 'Black'} to move")
        display_board_with_coordinates(board)
        
        # Check for game end conditions
        if board.is_checkmate():
            winner = "Black" if board.turn else "White"
            print(f"\nCheckmate! {winner} wins!")
            break
        elif board.is_stalemate():
            print("\nStalemate! It's a draw!")
            break
        elif board.is_insufficient_material():
            print("\nDraw by insufficient material!")
            break
        elif board.is_seventyfive_moves():
            print("\nDraw by 75-move rule!")
            break
        elif board.is_fivefold_repetition():
            print("\nDraw by fivefold repetition!")
            break
        
        # Show check status
        if board.is_check():
            print("CHECK!")
        
        print(f"Legal moves available: {len(list(board.legal_moves))}")
        
        # Get user input
        user_input = input(f"Enter move for {'White' if board.turn else 'Black'}: ").strip().lower()
        
        # Handle special commands
        if user_input in ['quit', 'q']:
            print("Thanks for playing!")
            break
        elif user_input in ['help', 'h']:
            print("\nMove format examples:")
            print("  e2e4    - Pawn from e2 to e4")
            print("  g1f3    - Knight from g1 to f3")
            print("  e1g1    - Castling (king side)")
            print("  e7e8q   - Pawn promotion to queen")
            continue
        elif user_input in ['moves', 'm']:
            legal_moves = get_legal_moves_list(board)
            print(f"\nAll legal moves ({len(legal_moves)}):")
            # Display moves in rows of 8
            for i in range(0, len(legal_moves), 8):
                print("  " + "  ".join(legal_moves[i:i+8]))
            continue
        elif user_input in ['undo', 'u']:
            if move_history:
                board.pop()
                last_move = move_history.pop()
                print(f"Undid move: {last_move}")
            else:
                print("No moves to undo!")
            continue
        
        # Try to parse and make the move
        try:
            move = chess.Move.from_uci(user_input)
            if board.is_legal(move):
                board.push(move)
                move_history.append(user_input)
                print(f"Move played: {user_input}")
                
                # Show what piece was moved
                piece = board.piece_at(move.to_square)
                if piece:
                    piece_name = chess.piece_name(piece.piece_type).title()
                    color = "White" if piece.color else "Black"
                    print(f"  ({color} {piece_name})")
            else:
                print("Illegal move! Try again.")
                # Show a few legal moves as hints
                legal_moves = get_legal_moves_list(board)
                print(f"Hint - some legal moves: {', '.join(legal_moves[:5])}")
                if len(legal_moves) > 5:
                    print(f"  (and {len(legal_moves) - 5} more - type 'moves' to see all)")
        except ValueError:
            print("Invalid move format! Use format like 'e2e4' or type 'help' for examples.")


def main_menu():
    """Display main menu and handle game selection"""
    while True:
        print("\n" + "="*50)
        print("CHESS GAME SELECTOR")
        print("="*50)
        print("1. Play Standard Chess")
        print("2. Variant 1 - No-Pawns 4 Rooks")
        print("3. Quit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            play_interactive_game(variant1.chess.Board, "Standard Chess")
        elif choice == '2':
            play_interactive_game(variant1.MyChessVariant1, "Variant 1 - No-Pawns 4 Rooks")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()