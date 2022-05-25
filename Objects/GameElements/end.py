import string
import pygame
from Objects.GameElements.game_element import GameElement

class End(GameElement):

    def __init__(self, pos: tuple, img_name: str, *groups):
        super().__init__(pos, img_name, *groups)