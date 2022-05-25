import pygame
from Objects.GameElements.game_element import GameElement
from math import ceil, floor

class Spike(GameElement):

    def __init__(self, pos: tuple, img_name: str, *groups):
        super().__init__(pos, img_name, *groups)

    def updateHitbox(self):
        hitbox_x = self.rect.x + ceil(self.rect.w / 3)
        hitbox_y = self.rect.y + floor(6 * self.rect.h / 15)
        hitbox_w = floor(self.rect.w / 3)
        hitbox_h = floor(9 * self.rect.h / 15)
        self.hitbox = (hitbox_x, hitbox_y, hitbox_w, hitbox_h)