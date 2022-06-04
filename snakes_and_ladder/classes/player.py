"""
player class
"""

from colorama import Fore


class Player:

    def __init__(self, name: str, symbol: str, color: str):
        self.name = name
        self.symbol = symbol
        self.symbol_color = color
        self.value = 1

    def get_value(self) -> int:
        return self.value

    def set_value(self, value: int) -> None:
        if self.value + value <= 100:
            self.value += value

    def get_symbol(self) -> str:
        return self.symbol

    def get_symbol_color(self) -> str:
        return eval(f"Fore.{self.symbol_color}")

    def get_name(self) -> str:
        return self.name
