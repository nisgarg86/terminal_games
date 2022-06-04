from tic_tac_toe.classes import Game, Player, Board


if __name__ == '__main__':
    game_board = Board()
    player1 = Player('1', 'X', 'RED')
    player2 = Player('2', 'O', 'BLUE')
    game_board.add_player(player1)
    game_board.add_player(player2)
    game = Game(game_board)
    game.launch_game()
