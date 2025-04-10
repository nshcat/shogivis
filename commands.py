from typing import List, Tuple
from pylatex.base_classes import Arguments, CommandBase
from shogi import BoardState, BoardPiece, Piece, Side, CapturedPiece

class ShogiBoard(CommandBase):
    _latex_name = "shogiban"
    _default_escape = False

    def __init__(self, board: BoardState):
        super().__init__(arguments=ShogiBoard._build_arguments(board))


    @staticmethod
    def _build_arguments(board: BoardState) -> List[str]:
        boardContents = "".join([_boardpiece_to_latex(boardPiece) for boardPiece in board.pieces])
        capturedContents = "".join([_captured_piece_to_latex(capturedPiece) for capturedPiece in board.captured])
        return boardContents + capturedContents
    

class TsumeBoard(CommandBase):
    _latex_name = "tsumeshogi"
    _default_escape = False

    def __init__(self, board: BoardState, xrange: Tuple[int, int], yrange: Tuple[int, int]):
        super().__init__(arguments=TsumeBoard._build_arguments(board, xrange, yrange))


    @staticmethod
    def _build_arguments(board: BoardState, xrange: Tuple[int, int], yrange: Tuple[int, int]) -> List[str]:
        boardContents = "".join([_boardpiece_to_latex(boardPiece) for boardPiece in board.pieces])
        capturedContents = "".join([_captured_piece_to_latex(capturedPiece) for capturedPiece in board.captured])
        return [str(xrange[0]), str(xrange[1]), str(yrange[0]), str(yrange[1]), boardContents + capturedContents]
    

def _captured_piece_to_latex(capturedPiece: CapturedPiece) -> str:
    return "\\mochigoma[%d]\\%s" % (capturedPiece.amount, _piece_to_latex(capturedPiece.piece, capturedPiece.side))


def _boardpiece_to_latex(boardPiece: BoardPiece) -> str:
    pieceLatex = _piece_to_latex(boardPiece.piece, boardPiece.side)
    return "\\koma%d%d\\%s" % (boardPiece.position[0], boardPiece.position[1], pieceLatex)


def _piece_to_latex(piece: Piece, side: Side) -> str:
    if piece == Piece.King:
        return "GY" if side == Side.Gote else "Ou"

    pieceMap = {
        Piece.Pawn: "Fu",
        Piece.Tokin: "To",
        Piece.Lance: "Ky",
        Piece.Knight: "Ke",
        Piece.Silver: "Gi",
        Piece.Gold: "Ki",
        Piece.Rook: "Hi",
        Piece.Bishop: "Ka",
        Piece.PromotedLance: "Ny",
        Piece.PromotedKnight: "Nk",
        Piece.PromotedSilver: "Ng",
        Piece.PromotedRook: "Ry",
        Piece.PromotedBishop: "Um"
    }

    pieceStr = pieceMap[piece]

    if side == Side.Gote:
        return pieceStr.upper()
    else:
        return pieceStr