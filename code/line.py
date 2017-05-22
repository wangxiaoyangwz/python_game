import pygame
import sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Draw lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit(0)

    screen.fill((0,80,0))

    #draw lines
    color=100,255,200
    width=8
    pygame.draw.line(screen,color,(100,100),(500,400),width)

    pygame.display.update()
    
