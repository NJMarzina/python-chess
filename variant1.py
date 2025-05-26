import chess
import chess.engine

class MyChessVariant1(chess.Board):
    """Example chess variant - no pawns, pieces start on back ranks"""
    
    def __init__(self):
        super().__init__(fen=None)
        
        # White pieces--back rank
        self.set_piece_at(chess.A1, chess.Piece(chess.ROOK, chess.WHITE))
        self.set_piece_at(chess.B1, chess.Piece(chess.KNIGHT, chess.WHITE))
        self.set_piece_at(chess.C1, chess.Piece(chess.BISHOP, chess.WHITE))
        self.set_piece_at(chess.D1, chess.Piece(chess.QUEEN, chess.WHITE))
        self.set_piece_at(chess.E1, chess.Piece(chess.KING, chess.WHITE))
        self.set_piece_at(chess.F1, chess.Piece(chess.BISHOP, chess.WHITE))
        self.set_piece_at(chess.G1, chess.Piece(chess.KNIGHT, chess.WHITE))
        self.set_piece_at(chess.H1, chess.Piece(chess.ROOK, chess.WHITE))

        # additional white pieces
        self.set_piece_at(chess.A2, chess.Piece(chess.ROOK, chess.WHITE))
        self.set_piece_at(chess.H2, chess.Piece(chess.ROOK, chess.WHITE))
        
        # Black pieces--back rank
        self.set_piece_at(chess.A8, chess.Piece(chess.ROOK, chess.BLACK))
        self.set_piece_at(chess.B8, chess.Piece(chess.KNIGHT, chess.BLACK))
        self.set_piece_at(chess.C8, chess.Piece(chess.BISHOP, chess.BLACK))
        self.set_piece_at(chess.D8, chess.Piece(chess.QUEEN, chess.BLACK))
        self.set_piece_at(chess.E8, chess.Piece(chess.KING, chess.BLACK))
        self.set_piece_at(chess.F8, chess.Piece(chess.BISHOP, chess.BLACK))
        self.set_piece_at(chess.G8, chess.Piece(chess.KNIGHT, chess.BLACK))
        self.set_piece_at(chess.H8, chess.Piece(chess.ROOK, chess.BLACK))

        # additional black pieces
        self.set_piece_at(chess.A7, chess.Piece(chess.ROOK, chess.BLACK))
        self.set_piece_at(chess.H7, chess.Piece(chess.ROOK, chess.BLACK))