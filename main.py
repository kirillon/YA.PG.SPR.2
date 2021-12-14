import os
import sys
from copy import deepcopy
from random import randint

import pygame
from pygame import mouse

TILE = 20
FPS = 120
RES = WIDTH, HEIGHT = 1600, 900
W, H = WIDTH // TILE, HEIGHT // TILE
f = 0
pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode(RES)

clock = pygame.time.Clock()
mouse.set_visible(False)
mous = pygame.sprite.Sprite(all_sprites)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


mouse_img = load_image("arrow.png")
while True:

    screen.fill(pygame.color.Color("black"))
    if mouse.get_focused():
        mous.image = mouse_img
        mous.rect = mous.image.get_rect()
        mous.rect.x = mouse.get_pos()[0]
        mous.rect.y = mouse.get_pos()[1]
        all_sprites.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(FPS)
