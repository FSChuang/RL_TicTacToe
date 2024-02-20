import torch
import random
import numpy as np
from collections import deque
from game_AI import TicTacToe_AI, Player, movement
from model import Linear, QTrainer
import time

MAX_MEMORY = 5000
BATCH_SIZE = 500
LR = 0.001 #learning rate

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 1
        self.gamma = 0.9
        self.memory = deque(maxlen = MAX_MEMORY)
        self.model = Linear(9, 256, 9)
        self.trainer = QTrainer(self.model, lr = LR, gamma = self.gamma)

    def get_state(self, game):
        board = [[game.board[row][column].value for column in range(3)] for row in range(3)]
        return np.array(torch.tensor(board).view(-1, 9).squeeze(0), dtype = int)
        
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        final_move = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if random.randint(0, 9) < self.epsilon:
            final_move[random.randint(0, 8)] = 1
        else:
            state0 = torch.tensor(state, dtype = torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
            
        return final_move
        
def train():
        agent = Agent()
        game = TicTacToe_AI()
        sleep_time = 0
        origin = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        while True:
            #get current state
            state_old = agent.get_state(game)

            #get movement
            final_move = agent.get_action(state_old)

            #do movement and get new state
            reward, done = game._game_play(final_move)
            if done:
                time.sleep(sleep_time)
                game._reset()
                agent.train_long_memory()
                agent.n_games += 1
                print("Game", agent.n_games)
                game._game_play(origin)

            time.sleep(sleep_time)
            state_new = agent.get_state(game)

            #train short memory()
            agent.train_short_memory(state_old, final_move, reward, state_new, done)
            # remember
            agent.remember(state_old, final_move, reward, state_new, done)

            game._opponent_move()
            
            time.sleep(sleep_time)

            if game._game_is_over(Player.P2)[0]:
                print(game._game_is_over(Player.P2))
                game._reset()
                agent.train_long_memory()
                agent.n_games += 1

            if agent.n_games > 10000:
                sleep_time = 1

                

if __name__ == '__main__':
    train()