import pygame
import sys
from constants import *
from tictactoe import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
chip_font = pygame.font.Font(None, 400)
game_over_font = pygame.font.Font(None, 40)

# draw horizontal and vertical lines
def draw_lines():
    # horizontal
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, 200*i), (600, 200*i), LINE_WIDTH)
    # vertical
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (200*i, 0), (200*i, 600), LINE_WIDTH)

def draw_chips():
    # draw chips based on the board state
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == "x":
                chip_x_surf = chip_font.render("x", 1, CROSS_COLOR)
                chip_x_rect = chip_x_surf.get_rect(center=(100 + SQUARE_SIZE * j, 100 + SQUARE_SIZE * i))
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[i][j] == "o":
                chip_o_surf = chip_font.render("o", 1, CIRCLE_COLOR)
                chip_o_rect = chip_o_surf.get_rect(center=(100 + SQUARE_SIZE * j, 100 + SQUARE_SIZE * i))
                screen.blit(chip_o_surf, chip_o_rect)


def draw_game_over():
    screen.fill(BG_COLOR)
    if winner != 0:
        game_over_surf = game_over_font.render(f"Player {winner} wins the game!", 1, LINE_COLOR)
    else:
        game_over_surf = game_over_font.render("No one wins this game!", 1, LINE_COLOR)

    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
    screen.blit(game_over_surf, game_over_rect)


    restart_surf = game_over_font.render("Press space to restart game...", 1, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)

# initialize the pygame state
screen.fill(BG_COLOR)
draw_lines()

#initialize the board state
board = initialize_board()
player = 1
game_over = False
winner = 0

# event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            clicked_col = event.pos[0] // SQUARE_SIZE
            clicked_row = event.pos[1] // SQUARE_SIZE
            if is_available(board, clicked_row, clicked_col):
                mark_square(board, clicked_row, clicked_col, player)
                chip = "x" if player ==1 else "o"
                if check_if_winner(board, chip):
                    game_over = True
                    winner = 1 if player == 1 else 2
                else:
                    if board_is_full(board):
                        game_over = True
                        winner = 0

                #alternate between player 1 and 2
                player = 2 if player == 1 else 1
                draw_chips()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                board = initialize_board()
                player = 1
                game_over = False
                winner = 0
                screen.fill(BG_COLOR)
                draw_lines()

    if game_over:
        pygame.display.update()
        pygame.time.delay(500)
        draw_game_over()

    pygame.display.update()
