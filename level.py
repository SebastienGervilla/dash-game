from constants import DEFAULT_SIZE, DEFAULT_VEL
import csv
import os
import pygame
from Objects.GameElements.game_element import GameElement
from Objects.GameElements.player import Player
from Objects.GameElements.block import Block
from Objects.GameElements.spike import Spike
from Objects.GameElements.end import End
from Objects.UI.game_button import GameButton

class Level():

    def __init__(self, screen_size: tuple, game_size: tuple, state_objs: dict):
        self.screen_size = screen_size
        self.game_size = game_size
        self.state_objs = state_objs
        self.curr_lvl = 1
        self.button_clicked = None

        self.generateMap()
        self.setLevel()
        self.setPlayer()
        self.setBgImage()

    def generateMap(self):
        self.lvl = []
        level_path = "levels/Level" + str(self.curr_lvl) + ".csv"
        with open(level_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                self.lvl.append(row)
        return self.lvl
        
    def setLevel(self):
        x = 0
        y = self.game_size[1]
        self.state_objs["platforms"] = []
        for row in reversed(self.lvl):
            for col in row:
                if col == "0":
                    self.state_objs["platforms"].append(Block((x , y), "block.png"))
                elif col == "1":
                    self.state_objs["platforms"].append(Spike((x , y), "spike.png"))
                elif col == "2":
                    self.state_objs["platforms"].append(End((x , y), "endblock.png"))
                x += 32
            y -= 32
            x = 0

        self.state_objs["buttons"] = []
        self.state_objs["buttons"].append(GameButton((20, 20), DEFAULT_SIZE, "pausebutton.png", "pause"))

    def setPlayer(self):
        self.state_objs["player"] = []
        start_pos = (self.game_size[0] / 2 - DEFAULT_SIZE[0] / 2, self.game_size[1] - DEFAULT_SIZE[1])
        self.player = Player(DEFAULT_VEL, start_pos, "avatar.png")
        self.state_objs["player"].append(self.player)

    def setBgImage(self):
        background_name = "level" + str(self.curr_lvl) + ".png"
        self.bg_img = pygame.image.load(os.path.join("assets\\images\\Backgrounds", background_name))

    def handleInputs(self, events: list[pygame.event.Event]):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]):
            self.player.jump()
        
        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.checkIsPressed(pygame.mouse.get_pos())
            elif (event.type == pygame.MOUSEBUTTONUP):
                button_clicked = self.checkForClick(pygame.mouse.get_pos())
                if button_clicked != None: 
                    self.button_clicked = button_clicked
            elif (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                self.button_clicked = "pause"

    def update(self):
        for object in self.state_objs["platforms"]:
            object: GameElement
            object.update(self.player.getVel()[0])

        self.player.update(self.state_objs["platforms"])

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

    def getButtonClicked(self):
        return self.button_clicked

    def clear(self):
        self.state_objs.clear()

    def __del__(self):
        self.clear()