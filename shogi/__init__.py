from enum import Enum
from typing import Tuple, List


class Piece(Enum):
    Pawn = 0
    Tokin = 1
    King = 2
    Silver = 3
    Gold = 4
    Lance = 5
    Knight = 6
    Bishop = 7
    Rook = 8
    PromotedBishop = 9
    PromotedRook = 10
    PromotedLance = 11
    PromotedKnight = 12
    PromotedSilver = 13


class Side(Enum):
    Gote = 0
    Sente = 1


class BoardPiece(object):
    _piece: Piece
    _position: Tuple[int, int]
    _side: Side


    def __init__(self, piece: Piece, side: Side, position: Tuple[int, int]):
        self._piece = piece
        self._side = side
        self._position = position


    @property
    def piece(self) -> Piece:
        return self._piece


    @property
    def side(self) -> Side:
        return self._side
    

    @property
    def position(self) -> Tuple[int, int]:
        return self._position
    

class CapturedPiece(object):
    _piece: Piece
    _amount: int
    _side: Side

    def __init__(self, piece: Piece, side: Side, amount: int = 1):
        self._piece = piece
        self._side = side
        self._amount = amount


    @property
    def piece(self) -> Piece:
        return self._piece


    @property
    def side(self) -> Side:
        return self._side
    

    @property
    def amount(self) -> int:
        return self._amount
    
    

class BoardState(object):
    _boardPieces: List[BoardPiece]
    _capturedPieces: List[CapturedPiece]

    def __init__(self, boardPieces: List[BoardPiece], capturedPieces: List[CapturedPiece]):
        self._boardPieces = boardPieces
        self._capturedPieces = capturedPieces


    @property
    def pieces(self) -> List[BoardPiece]:
        return self._boardPieces
    
    @property
    def captured(self) -> List[CapturedPiece]:
        return self._capturedPieces