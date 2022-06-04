"""
Player class
"""

from colorama import Fore


class Player:

    def __init__(self, name: str, symbol: str, color: str):
        self.player_name = name
        self.player_symbol = symbol
        self.color = color

    def make_move(self) -> int:
        print(f"{self.player_name}'s turn")
        num = 0
        while num > 9 or num < 1:
            num = int(input('Enter number between 1-9:'))
        return num

    def get_player_symbol(self) -> str:
        return self.player_symbol

    def get_player_name(self) -> str:
        return self.player_name

    def get_player_color(self) -> str:
        return eval(f"Fore.{self.color}")


if __name__ == '__main__':
    player = Player('Nishant', 'X', 'RED')
    player.make_move()
