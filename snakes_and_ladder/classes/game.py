"""
game class
"""

from random import randint
import time

from snakes_and_ladder.classes.board import Board
from snakes_and_ladder.classes.player import Player


class Game:
    def __init__(self, board: Board):
        self.board = board

    def launch_game(self) -> None:

        # printing initial board
        self.board.print_board()

        input("Press any key to start game...")

        while True:
            for player in self.board.player_list:
                dice_val = self.throw_dice()
                player.set_value(dice_val)
                self.board.print_board()
                if self.board.is_game_over():
                    print(f"{player.get_symbol_color()}Game Finished!!! {player.get_name()} won!!")
                    exit(0)
                input("Press any key to continue...")

    @staticmethod
    def throw_dice() -> int:
        return randint(1, 6)

