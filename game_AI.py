import pygame
import random
from enum import Enum
import sys
import numpy as np

pygame.init()

# Color 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

movement = {0: (0, 0), 1: (0, 1), 2: (0, 2),
            3: (1, 0), 4: (1, 1), 5: (1, 2),
            6: (2, 0), 7: (2, 1), 8: (2, 2)}

# Board constants
Width, Height = 600, 600
BG_Color = BLACK
Line_Color = WHITE
Line_Width = 30
Cell_Size = 600 // 3
Cricle_Radius = Cell_Size // 3
Circle_Color = BLUE
Circle_Width = 30
Cross_Space = Cell_Size // 4
Cross_Color = RED
Cross_Width = 30

# AI side
class Player(Enum):
    P1 = 'X'
    P2 = 'O'

# game
class TicTacToe_AI:

    def __init__(self, w=Width, h=Height):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Tic Tac Toe")

        self.board = [[" " for row in range(3)] for col in range(3)]
        self.player = Player.P1
    
    def _game_is_over(self, player):
        for row in range(3):
            if all([self.board[row][col] == player for col in range(3)]):
                return True, player
        
            if all([self.board[col][row] == player for col in range(3)]):
                return True, player
            
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2-i] == player for i in range(3)]):
            return True, player
        
        if all([cell != " " for row in self.board for cell in row]):
            return True, 'Tie'
        
        return False, None

    def _move(self, action):
        
        self.board[movement[np.argmax(action)][0]][movement[np.argmax(action)][1]] = self.player

    def _draw_grid(self):
        for row in range(1, 3):
            pygame.draw.line(self.display, WHITE, (Cell_Size*row, 0), (Cell_Size*row, Width), Line_Width)
            pygame.draw.line(self.display, WHITE, (0, Cell_Size*row), (Height, Cell_Size*row), Line_Width)

    def _draw_flags(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == Player.P1:
                    pygame.draw.line(self.display, RED, (Cell_Size*row + Cross_Space, Cell_Size*col + Cross_Space),
                                     (Cell_Size*row + Cell_Size - Cross_Space, Cell_Size*col + Cell_Size - Cross_Space), Cross_Width)
                    pygame.draw.line(self.display, RED, (Cell_Size*row + Cross_Space, Cell_Size*col + Cell_Size - Cross_Space), 
                                     (Cell_Size*row + Cell_Size - Cross_Space, Cell_Size*col + Cross_Space), Cross_Width)
                    
                elif self.board[row][col] == Player.P2:
                    pygame.draw.circle(self.display, color = Circle_Color, center = (Cell_Size*row + Cell_Size//2, Cell_Size*col + Cell_Size//2), radius = Cricle_Radius, width = Circle_Width)

    def _update_ui(self):
        self.display.fill(BLACK)
        self._draw_grid()
        self._draw_flags()
        pygame.display.flip()

    def _game_play(self, action):
        print(self.board)
        reward = 0 
        game_over = False
        # 1. Collect User input
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2.move / if ai choose the occupied place, end the game and return a negative reward
        if self.board[movement[np.argmax(action)][0]][movement[np.argmax(action)][1]] != " ":
            reward = -10
            game_over = True
            return game_over, reward
        self._move(action)

        # 3. Check if the game is over
        reward = 0 
        game_over = False
        if self._game_is_over(self.player)[0] == True:
            game_over = True
            if self._game_is_over()[1] == self.player:
                reward = 10
            elif self._game_is_over()[1] == 'tie':
                reward = 8
            else:
                reward = -10
            return game_over, reward
        
        
        # 4.update ui
        self._update_ui()

        
