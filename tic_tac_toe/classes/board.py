"""
board for tic tac toe
"""
from colorama import Style

from tic_tac_toe.classes.game_status import GameStatus
from tic_tac_toe.classes.player import Player


class Board:

    def __init__(self):

        self.default_char = ' '
        self.print_width = 3
        self.m = 3
        self.n = 3
        self.grid = [[self.default_char for _ in range(self.n)] for _ in range(self.m)]
        self.filled_count = 0
        self.total_count = 9
        self.player_list = []

    def add_player(self, player: Player) -> None:
        self.player_list.append(player)

    def fill_grid(self, index: int, symbol: str):

        index -= 1
        row = index // 3
        col = index % 3

        if self.is_position_filled(row, col):
            print('Position already filled, please try another position')
            return GameStatus.INVALID_MOVE
        else:
            self.grid[row][col] = symbol
            self.filled_count += 1
            self.print_board()

    def is_position_filled(self, row: int, col: int) -> bool:
        return self.grid[row][col] != self.default_char

    def print_board(self) -> None:
        row_separator = '|'+'-'*((2*self.print_width+1)*3+2)+'|'
        print(row_separator)
        for i in range(len(self.grid)):
            row = self.print_row(i)
            print(row)
            print(row_separator)

    def print_row(self, row: int) -> str:
        row_string = '|'
        col_list = list(range(len(self.grid[0])))
        for j in col_list:
            if self.grid[row][col_list[j]] != self.default_char:
                for player in self.player_list:
                    if self.grid[row][col_list[j]] == player.get_player_symbol():
                        val = f'{player.get_player_color()}{self.grid[row][col_list[j]]}'
                        break
            else:
                val = self.default_char
            row_string += ' '*self.print_width + f'{val}{Style.RESET_ALL}' + ' '*self.print_width + '|'
        return row_string

    def is_game_over(self, index: int) -> bool:

        index -= 1
        row = index // 3
        col = index % 3

        # checking values in that row
        values = set()
        for j in range(self.n):
            values.add(self.grid[row][j])
        if validate_set(values):
            return True

        # checking values in that col
        values = set()
        for i in range(self.m):
            values.add(self.grid[i][col])
        if validate_set(values):
            return True

        # checking first diagonal values
        diagonal_points_list = [(0, 0), (1, 1), (2, 2)]
        if (row, col) in diagonal_points_list:
            values = set()
            for val in diagonal_points_list:
                values.add(self.grid[val[0]][val[1]])
            if validate_set(values):
                return True

        # checking second diagonal
        diagonal_points_list = [(0, 2), (1, 1), (2, 0)]
        if (row, col) in diagonal_points_list:
            values = set()
            for val in diagonal_points_list:
                values.add(self.grid[val[0]][val[1]])
            if validate_set(values):
                return True

        return False

    def is_game_draw(self) -> bool:
        if self.filled_count == self.total_count:  # draw
            return True
        return False


def validate_set(set_object):
    if len(set_object) == 1 and '*' not in set_object:
        return True
    return False


if __name__ == '__main__':
    board = Board()
    print(board.fill_grid(1, 'X'))
    print(board.fill_grid(5, 'X'))
    print(board.fill_grid(9, 'X'))
