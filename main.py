import pygame, sys
import numpy as np
from pieces import *
from constants import *


player = 1
game_on = True
current = 0
used = []
nham = False
pygame.init()



#initalize colored titled screen 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(COLORS['background'])
pygame.display.set_caption('O quarto')


#Draw grid
for i in range(1, GRID):
    pygame.draw.line(screen, COLORS['line'],  (WIDTH*i/GRID, 0), (WIDTH*i/GRID, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, COLORS['line'],  (0, HEIGHT*i/GRID), (WIDTH, HEIGHT*i/GRID), LINE_WIDTH)

#create logic board
board = np.zeros((GRID, GRID))


#
def place_piece(row, column, piece):
    board[row][column] = piece
    draw_figure(row, column, piece)
    check_win(board)


def draw_figure(row, column, piece):
    pygame.draw.circle(screen, COLORS['blue'], (int(WIDTH/GRID * (column + 1/2)), int((HEIGHT/GRID * (row + 1/2)))), int(CIRCLE_RADIUS), int(FIGURE_WIDTH))
    pygame.display.update()



def check_win(board):
    pass

def is_available(row, column):
    return board[row][column] == 0

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and game_on:
            
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            cellX = int(mouseX // (WIDTH/GRID))
            cellY = int(mouseY // (HEIGHT/GRID))

            if is_available(cellY, cellX):
                if nham:
                    place_piece(cellY, cellX, current)
                else:
                    nham = True
                print(board)
                current = int(input('Escolha a próxima peça (0-15): '))
                while current in used or current > 15 or current < 0:
                    current = int(input('Peça já usada ou valor inválido, escolha outra: '))
                    
                used.append(current)
                if player == 1:
                    player = 2
                if player == 2:
                    player = 1


    pygame.display.update()
