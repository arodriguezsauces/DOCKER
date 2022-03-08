import os
import pygame
import time
X = 100
Y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
pygame.init()
win_screen = pygame.display.set_mode((500,500))
time.sleep(2)