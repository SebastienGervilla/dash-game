import pygame

class GameElement(pygame.sprite.Sprite):

    def __init__(self, image: pygame.Surface, pos: tuple, *groups):
        super().__init__(*groups)
        self.image = image

    def updateHitbox():
        pass