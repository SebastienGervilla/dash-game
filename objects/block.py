import pygame
from objects.gameElements import GameElement

class Block(GameElement):

    def __init__(self, image: pygame.Surface, pos: tuple, *groups):
        self.rect = image.get_rect(topleft=pos)
        self.hitbox = self.rect
        super().__init__(image, pos, *groups)

    def updateHitbox(self):
        self.hitbox = self.rect