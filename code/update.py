import pygame
from pygame.locals import *
white=255,255,255
blue=0,0,255
pygame.init()
screen=pygame.display.set_mode((600,500))
myfont=pygame.font.Font(None,60)
textImage1=myfont.render("1",True,white)
textImage2=myfont.render("2",True,white)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage1,(380,150))
    screen.blit(textImage2,(200,150))
    pygame.display.update()
