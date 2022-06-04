"""
main file for launching game
"""

from snakes_and_ladder.classes import Board, Player, Game

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
    game = Game(board)
    game.launch_game()
