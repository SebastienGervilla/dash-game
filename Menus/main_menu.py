from Menus.game_menu import GameMenu
from Objects.UI.game_button import GameButton

from constants import DEFAULT_SIZE

from math import floor

class MainMenu(GameMenu):

    def __init__(self, game_size: tuple, state_objs: dict, bg_name: str):
        super().__init__(game_size, state_objs, bg_name)

    def setMenu(self):
        super().setMenu()
        center = (floor(self.game_size[0] / 2), floor(self.game_size[1] / 2))
        button_size = (DEFAULT_SIZE[0] * 2, DEFAULT_SIZE[1] * 2)
        self.state_objs["buttons"].append(GameButton((center[0] / 2 - button_size[0] / 2, 
        floor(self.game_size[1] * 2 / 3)), button_size, "playbutton.png", "play"))
        self.state_objs["buttons"].append(GameButton((center[0] - button_size[0] / 2, 
        floor(self.game_size[1] * 2 / 3)), button_size, "levelbutton.png", "level"))
        self.state_objs["buttons"].append(GameButton((center[0] * 3 / 2 - button_size[0] / 2, 
        floor(self.game_size[1] * 2 / 3)), button_size, "quitbutton.png", "quit"))