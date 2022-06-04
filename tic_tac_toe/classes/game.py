from tic_tac_toe.classes.board import Board
from tic_tac_toe.classes.game_status import GameStatus


class Game:

    def __init__(self,
                 board: Board):

        self.board = board

    def launch_game(self):

        game_complete = False

        self.board.print_board()
        input('Press any key to begin...')

        while not game_complete:
            for player in self.board.player_list:
                # run till player not enters correct value
                response = GameStatus.INVALID_MOVE
                while response == GameStatus.INVALID_MOVE:
                    index = player.make_move()
                    response = self.board.fill_grid(index, player.get_player_symbol())
                if self.board.is_game_over(index):
                    print(f'{player.get_player_name()} won!!!')
                    exit(0)
                elif self.board.is_game_draw():
                    print(f'Its a draw')
                    exit(0)
