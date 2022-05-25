import os
import pygame
from Objects.UI.game_button import GameButton

class GameMenu():

    def __init__(self, game_size: tuple, state_objs: dict, bg_name: str):
        self.game_size = game_size
        self.state_objs = state_objs
        self.setMenu()
        self.setBgImage(bg_name)

    def setMenu(self):
        self.state_objs["buttons"] = []

    def checkIsPressed(self, mouse_pos: tuple):
        for object in self.state_objs["buttons"]:
            object: GameButton
            object.checkIsPressed(mouse_pos)

    def checkForClick(self, mouse_pos: tuple):
        for object in self.state_objs["buttons"]:
            object: GameButton
            if object.getCollision(mouse_pos) and object.is_pressed:
                return object.name
        return None

    def setBgImage(self, bg_name: str):
        self.bg_img = pygame.image.load(os.path.join("assets\\images\\Backgrounds", bg_name))

    def update(self):
        pass