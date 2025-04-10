from pylatex import Command, Document, Section, Subsection, Package
from pylatex.utils import NoEscape, italic
from commands import ShogiBoard, TsumeBoard
from shogi import BoardPiece, Piece, Side, BoardState, CapturedPiece

def fill_document(doc: Document):
    board = BoardState(
        [
            BoardPiece(Piece.Lance, Side.Sente, (1, 1)),
            BoardPiece(Piece.King, Side.Sente, (2, 2)),
            BoardPiece(Piece.Pawn, Side.Sente, (4, 2)),
            BoardPiece(Piece.Pawn, Side.Sente, (1, 3)),
            BoardPiece(Piece.Bishop, Side.Gote, (2, 3)),
        ],
        [
            CapturedPiece(Piece.Silver, Side.Gote),
            CapturedPiece(Piece.Gold, Side.Gote, 2),

            CapturedPiece(Piece.Pawn, Side.Sente, 2),
            CapturedPiece(Piece.Rook, Side.Sente)
        ]
    )

    #doc.append(TsumeBoard(board, [1, 4], [1, 5]))
    doc.append(ShogiBoard(board))

if __name__ == "__main__":
    # Basic document
    doc = Document("basic")

    doc.preamble.append(Package("tikz"))
    doc.preamble.append(Package("graphicx"))
    doc.preamble.append(Package("listings"))
    doc.preamble.append(Package("bxcjkjatype", "whole"))
    doc.preamble.append(Package("amsmath"))
    doc.preamble.append(Package("RyuOhTeX"))

    fill_document(doc)

    doc.generate_tex()
    doc.generate_pdf(clean_tex=False)
    
