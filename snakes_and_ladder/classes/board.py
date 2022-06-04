"""
board for tic tac toe
"""
import os

from colorama import Style

from snakes_and_ladder.classes.player import Player


class Board:

    def __init__(self):

        self.default_char = ' '
        self.print_width = 5
        self.m = 10
        self.n = 10
        self.grid = [[0 for j in range(self.n)] for i in range(self.m)]
        self.fill_grid()
        self.player_list = []

    def add_player(self, player: Player) -> None:
        self.player_list.append(player)

    def fill_grid(self) -> None:
        counter = 1
        reverse = False
        for i in range(self.m):
            temp = list(range(counter, counter+10))
            if reverse:
                temp = temp[::-1]
            reverse = not reverse
            self.grid[self.m - 1 - i] = temp
            counter += 10

    def is_game_over(self) -> bool:
        for player in self.player_list:
            if player.get_value() == 100:
                return True
            return False

    def print_board(self) -> None:
        print("\033c")
        cell_sep = '-'*(2*self.print_width+1)
        row_separator = '|' + '|'.join([cell_sep]*self.n) + '|'
        print(row_separator)
        for i in range(self.m):
            row = self.print_row(i)
            print(row)
            print(row_separator)
        print('\n\n')

    def print_row(self, row: int) -> str:
        row_string = '|'
        col_list = list(range(self.n))
        for j in col_list:
            curr_cell_val = self.grid[row][col_list[j]]
            curr_cell_val_len = len(str(curr_cell_val))
            player_val_list = [' ' if self.player_list[i].get_value() != curr_cell_val
                               else f"{self.player_list[i].get_symbol_color()}{self.player_list[i].get_symbol()}"
                               for i in range(len(self.player_list))]
            row_string += ''.join(player_val_list) + f'{Style.RESET_ALL}'
            row_string += ' '*(2*self.print_width + 1 - curr_cell_val_len - len(self.player_list)) +\
                          f'{self.grid[row][col_list[j]]}' + '|'
        return row_string


if __name__ == '__main__':
    board = Board()
    player_1 = Player('Nishant', '1', 'RED')
    player_2 = Player('Shilpi', '2', 'BLUE')
    player_3 = Player('Nishu', '3', 'YELLOW')
    player_4 = Player('Shinu', '4', 'GREEN')
    board.add_player(player_1)
    board.add_player(player_2)
    board.add_player(player_3)
    board.add_player(player_4)
    player_4.value = 36
    player_3.value = 99
    board.print_board()
