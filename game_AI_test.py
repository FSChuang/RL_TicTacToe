from game_AI import TicTacToe_AI, Player, movement
import pygame
import sys
import os

movement = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1]]
idx = [0, 0]
if __name__ == '__main__':
    game = TicTacToe_AI()
    i = 0
    p1 = Player.P1
    print(p1.value)
    '''while(i < 4):
        idx = game._game_play(movement[i])
        game._opponent_move()
        print(game.board)
        if i < 4:
            try:
                print("Reward: ", idx[1])
            except:
                print("error")
        i+=1
        os.system("pause")'''
    idx = game._game_play([0, 0, 0, 1, 0, 0, 0, 0, 0])
    print(idx)


        


