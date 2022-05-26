import pygame
from Menus.game_menu import GameMenu
from Objects.UI.game_button import GameButton

from constants import DEFAULT_SIZE

from math import floor

class PauseMenu(GameMenu):

    def __init__(self, game_size: tuple, state_objs: dict, bg_name: str):
        super().__init__(game_size, state_objs, bg_name)

    def setMenu(self):
        super().setMenu()
        center = (floor(self.game_size[0] / 2), floor(self.game_size[1] / 2))
        button_size = (DEFAULT_SIZE[0] * 2, DEFAULT_SIZE[1] * 2)
        self.state_objs["buttons"].append(GameButton((center[0] - button_size[0] * 2, 
        center[1]), button_size, "playbutton.png", "play"))
        self.state_objs["buttons"].append(GameButton((center[0] - button_size[0] / 2, 
        center[1]), button_size, "menubutton.png", "menu"))
        self.state_objs["buttons"].append(GameButton((center[0] + button_size[0],
        center[1]), button_size, "restartbutton.png", "restart"))

    def draw(self, screen: pygame.Surface):
        center = (floor(self.game_size[0] / 2 - self.bg_img.get_width() / 2), 
        floor(self.game_size[1] / 2 - self.bg_img.get_height() / 2))
        screen.blit(self.bg_img, center)

    def __del__(self):
        deleted = 0
        while(deleted < 3):
            del self.state_objs["buttons"][-1]
            deleted += 1
        self.state_objs["buttons"].append(GameButton((20, 20), DEFAULT_SIZE, "pausebutton.png", "pause"))