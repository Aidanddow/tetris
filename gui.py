from shapes import *
from block import Block
import pygame,time

pygame.init()
screen = pygame.display.set_mode((600,945))
screen.fill((0,0,0))

def draw_grid():
    for i in range(40,480,40):
        pygame.draw.line(screen,(200,200,200),(i,40),(i,840))
    for i in range(40,850,40):
        pygame.draw.line(screen,(200,200,200),(40,i),(440,i))
    pygame.display.update()


def draw_box(x,y,num):

    colours = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(255,165,0),(255,255,0),(128,0,128),(100,210,255)]
    colour = colours[num]

    start = (40,40)
    pygame.draw.rect(screen, colour, [start[0]*(x+1), start[1]*(y+1), 40, 40])


def update_grid(board):
    screen.fill((0,0,0))
    for y in range(20):
        for x in range(10):
            if board[y][x] != 0:
                draw_box(x,y,board[y][x])
    draw_grid()
    pygame.display.update()
    







    
    

