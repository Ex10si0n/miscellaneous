import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size, 0, 32)

font = pygame.font.SysFont("arial", 17)
font_height = font.get_linesize()
event_text = []

while 1:
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[(-screen_size[1]//font_height):]
    # 这个切片操作保证了event_text里面只保留一个屏幕的文字

    if event.type == QUIT:
        exit()
    screen.fill((0, 0, 0))
    # screen.blit()
    y = screen_size[1]-font_height
    # 找一个合适的起笔位置，最下面开始但是要留一行空

    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))
        y -= font_height

    pygame.display.update()
