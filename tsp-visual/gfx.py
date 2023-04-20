import pygame
import sys
from util import *
from pygame.locals import *


def check_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            pygame.quit()
            sys.exit()

def draw_text_center(surface, text, font, x, y):
    text_obj = font.render(text, 1, RED)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def draw_text_top_left(surface, text, color, font, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def draw_dividers(surface, DIVIDERS):
    for x1, y1, x2, y2 in DIVIDERS:
        pygame.draw.aaline(surface, WHITE, (x1, y1), (x2, y2))

def draw_path(surface, cities, order):
    if len(order) != len(cities):
        return
    r = CITY_SIZE//len(cities)
    r = int(max(MIN_CITY_SIZE, r))
    r = int(min(MAX_CITY_SIZE, r))
    order = order[order.index(0):] + order[:order.index(0)]
    for i in range(len(order)):
        pass