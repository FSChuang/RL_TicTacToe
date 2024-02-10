import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_WIDTH = 15
CELL_SIZE = WIDTH // 3
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
CROSS_SPACE = CELL_SIZE // 4
CROSS_COLOR = (66, 66, 66)
CIRCLE_COLOR = (239, 231, 200)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Draw the grid
def draw_grid():
    for row in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE * row), (WIDTH, CELL_SIZE * row), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE * row, 0), (CELL_SIZE * row, HEIGHT), LINE_WIDTH)

# Draw the markers
def draw_markers():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + CROSS_SPACE, row * CELL_SIZE + CELL_SIZE - CROSS_SPACE),
                                 (col * CELL_SIZE + CELL_SIZE - CROSS_SPACE, row * CELL_SIZE + CROSS_SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + CROSS_SPACE, row * CELL_SIZE + CROSS_SPACE),
                                 (col * CELL_SIZE + CELL_SIZE - CROSS_SPACE, row * CELL_SIZE + CELL_SIZE - CROSS_SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Check for a win
def check_win(player):
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Main game loop
turn = 'X'
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x coordinate
            mouseY = event.pos[1]  # y coordinate

            clicked_row = int(mouseY // CELL_SIZE)
            clicked_col = int(mouseX // CELL_SIZE)

            if board[clicked_row][clicked_col] == ' ':
                board[clicked_row][clicked_col] = turn

                if check_win(turn):
                    game_over = True
                elif all([cell != ' ' for row in board for cell in row]):
                    game_over = True
                else:
                    turn = 'O' if turn == 'X' else 'X'

    screen.fill(BG_COLOR)
    draw_grid()
    draw_markers()

    if game_over:
        font = pygame.font.Font(None, 100)
        text_surface = font.render("Game Over", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)

    pygame.display.update()

    pygame.time.delay(100)

pygame.quit()
sys.exit()