import pygame
from objects.gameElements import GameElement
from math import ceil, floor

class Spike(GameElement):

    def __init__(self, image: pygame.Surface, pos: tuple, *groups):
        self.rect = image.get_rect(topleft=pos)
        self.hitbox = self.getHitbox()
        super().__init__(image, pos, *groups)

    def updateHitbox(self):
        self.hitbox = self.getHitbox()

    def getHitbox(self):
        hitbox_x = self.rect.x + ceil(self.rect.w / 3)
        hitbox_y = self.rect.y + floor(6 * self.rect.h / 15)
        hitbox_w = floor(self.rect.w / 3)
        hitbox_h = floor(9 * self.rect.h / 15)
        return pygame.Rect(hitbox_x, hitbox_y, hitbox_w, hitbox_h)