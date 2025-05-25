import chess

def test_basic_functionality():
    """Test basic chess functionality"""
    print("=== STANDARD CHESS TEST ===")
    
    # Create standard board
    board = chess.Board()
    print("Initial board:")
    print(board)
    print(f"Number of legal moves: {len(list(board.legal_moves))}")
    print(f"Whose turn: {'White' if board.turn else 'Black'}")
    
    # Make a move
    move = chess.Move.from_uci("e2e4")
    if board.is_legal(move):
        board.push(move)
        print("\nAfter e2-e4:")
        print(board)
        print(f"Number of legal moves: {len(list(board.legal_moves))}")
        print(f"Whose turn: {'White' if board.turn else 'Black'}")
    
    print("\n" + "="*50 + "\n")

def test_custom_starting_position():
    """Test custom starting position"""
    print("=== CUSTOM STARTING POSITION ===")
    
    # Create empty board
    board = chess.Board(fen=None)
    
    # Place only kings and queens
    board.set_piece_at(chess.E1, chess.Piece(chess.KING, chess.WHITE))
    board.set_piece_at(chess.D1, chess.Piece(chess.QUEEN, chess.WHITE))
    board.set_piece_at(chess.E8, chess.Piece(chess.KING, chess.BLACK))
    board.set_piece_at(chess.D8, chess.Piece(chess.QUEEN, chess.BLACK))
    
    print("Custom board (Kings and Queens only):")
    print(board)
    print(f"Number of legal moves: {len(list(board.legal_moves))}")
    
    print("\n" + "="*50 + "\n")

class MyChessVariant(chess.Board):
    """Example chess variant - modify starting position"""
    
    def __init__(self):
        # Start with empty board
        super().__init__(fen=None)
        
        # Custom starting position - put all pieces on back ranks
        # White pieces
        self.set_piece_at(chess.A1, chess.Piece(chess.ROOK, chess.WHITE))
        self.set_piece_at(chess.B1, chess.Piece(chess.KNIGHT, chess.WHITE))
        self.set_piece_at(chess.C1, chess.Piece(chess.BISHOP, chess.WHITE))
        self.set_piece_at(chess.D1, chess.Piece(chess.QUEEN, chess.WHITE))
        self.set_piece_at(chess.E1, chess.Piece(chess.KING, chess.WHITE))
        self.set_piece_at(chess.F1, chess.Piece(chess.BISHOP, chess.WHITE))
        self.set_piece_at(chess.G1, chess.Piece(chess.KNIGHT, chess.WHITE))
        self.set_piece_at(chess.H1, chess.Piece(chess.ROOK, chess.WHITE))
        
        # No pawns! Start with just back rank pieces
        
        # Black pieces
        self.set_piece_at(chess.A8, chess.Piece(chess.ROOK, chess.BLACK))
        self.set_piece_at(chess.B8, chess.Piece(chess.KNIGHT, chess.BLACK))
        self.set_piece_at(chess.C8, chess.Piece(chess.BISHOP, chess.BLACK))
        self.set_piece_at(chess.D8, chess.Piece(chess.QUEEN, chess.BLACK))
        self.set_piece_at(chess.E8, chess.Piece(chess.KING, chess.BLACK))
        self.set_piece_at(chess.F8, chess.Piece(chess.BISHOP, chess.BLACK))
        self.set_piece_at(chess.G8, chess.Piece(chess.KNIGHT, chess.BLACK))
        self.set_piece_at(chess.H8, chess.Piece(chess.ROOK, chess.BLACK))

def test_my_variant():
    """Test our custom variant"""
    print("=== MY CHESS VARIANT (NO PAWNS) ===")
    
    variant_board = MyChessVariant()
    print("Variant board (no pawns):")
    print(variant_board)
    print(f"Number of legal moves: {len(list(variant_board.legal_moves))}")
    
    # Make a move
    move = chess.Move.from_uci("e1e2")  # King forward
    if variant_board.is_legal(move):
        variant_board.push(move)
        print("\nAfter King e1-e2:")
        print(variant_board)

if __name__ == "__main__":
    test_basic_functionality()
    test_custom_starting_position()
    test_my_variant()