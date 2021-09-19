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
    ima = Piece(piece)
    
    #Blue figures
    if ima.blue:
        #Round blue figures
        if ima.round:
            #Tall round blue figures
            if ima.tall:
                #Pinched tall round blue figure
                if ima.pinched:
                    print('Pinched tall round blue figure')
                #Unpinched tall round blue figure figure
                else:
                    print('Unpinched tall round blue figure figure')
            #Short figures
            else:
                #Pinched short round blue figure
                if ima.pinched:
                    print('Pinched short round blue figure')
                #Unpinched short round blue figure
                else:
                    print('Unpinched short round blue figure')
        #Square blue figures
        else:
            #Tall square blue figures
            if ima.tall:
                #Pinched tall square blue figure
                if ima.pinched:
                    print('Pinched tall square blue figure')
                #Unpinched tall square blue figure
                else:
                    print('Unpinched tall square blue figure')
            #Short square blue figures
            else:
                #Pinched short square blue figure
                if ima.pinched:
                    print('Pinched short square blue figure')
                #Unpinched short square blue figure
                else:
                    print('Unpinched short square blue figure')
    #Red figures
    else:
        #Round red figures
        if ima.round:
            #Tall round red figures
            if ima.tall:
                #Pinched tall round red figure
                if ima.pinched:
                    pass
                #Unpinched tall round red figure
                else:
                    pass
            #Short round red figures
            else:
                #Pinched short round red figure
                if ima.pinched:
                    pass
                #Unpinched short round red figure
                else:
                    pass
        #Square red figures
        else:
            #Tall square red figures
            if ima.tall:
                #Pinched tall square red figure
                if ima.pinched:
                    pass
                #Unpinched tall square red figure
                else:
                    pass
            #Short square red figures
            else:
                #Pinched square red figure
                if ima.pinched:
                    pass
                #Unpinched square red figure
                else:
                    pass


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
