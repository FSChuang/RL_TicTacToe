from game_AI import TicTacToe_AI, Player

movement = [1, 0, 0, 0, 0, 0, 0, 0, 0]
if __name__ == '__main__':
    game = TicTacToe_AI()
    i = 0
    while(i < 3):
        game._game_play(movement)
        i+=1
        