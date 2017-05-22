import sys,pygame
from pygame.locals import *
pygame.init()
black=0,0,0
screen=pygame.display.set_mode((600,500))
pygame.draw.circle(screen,black,(100,100),30,0)
screen.fill((0,0,100))
pygame.display.update()
