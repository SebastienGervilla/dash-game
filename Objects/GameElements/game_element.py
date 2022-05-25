import pygame
import os

from constants import DEFAULT_SIZE

class GameElement(pygame.sprite.Sprite):

    def __init__(self, pos: tuple, image_name: str, *groups):
        super().__init__(*groups)
        self.pos = list(pos)
        self.size = list(DEFAULT_SIZE)
        self.setImage(image_name)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect

    def setImage(self, image_name):
        img_path = os.path.join("assets\\images\\GameElements", image_name)
        self.image = pygame.image.load(img_path)
        self.resizeImage()

    def resizeImage(self):
        self.image = pygame.transform.smoothscale(self.image, self.size)

    def update(self, vel_x: int):
        self.pos[0] -= vel_x
        self.rect.x = self.pos[0]
        self.updateHitbox()

    def updateHitbox(self):
        self.hitbox = self.rect

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.pos)
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox)

    def getPos(self):
        return self.pos

    def getSize(self):
        return self.size