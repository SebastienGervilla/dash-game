from re import S
import pygame
import os

class GameButton():

    def __init__(self, pos: tuple, size: tuple, image_name: str, button_name: str):
        self.pos = list(pos)
        self.size = size
        self.setImage(image_name)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect
        self.name = button_name
        
        self.is_pressed = False

    def setImage(self, image_name):
        img_path = os.path.join("assets\\images\\UI", image_name)
        self.image = pygame.image.load(img_path)
        self.resizeImage()

    def resizeImage(self):
        self.image = pygame.transform.smoothscale(self.image, self.size)
    
    def checkIsPressed(self, mouse_pos: tuple):
        self.is_pressed = True if self.getCollision(mouse_pos) else False

    def getCollision(self, mouse_pos: tuple):
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

    def update(self):
        pass

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.pos)
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox)

    def getPos(self):
        return self.pos

    def getSize(self):
        return self.size