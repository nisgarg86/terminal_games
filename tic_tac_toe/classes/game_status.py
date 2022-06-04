from enum import Enum


class GameStatus(Enum):
    GAME_FINISH = 1
    GAME_DRAW = 2
    VALID_MOVE = 3
    INVALID_MOVE = 4