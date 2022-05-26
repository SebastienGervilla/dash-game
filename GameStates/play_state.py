from Objects.GameElements.game_element import GameElement
from Objects.UI.game_button import GameButton
from GameStates.game_state import GameState
from Menus.pause_menu import PauseMenu
from level import Level
import pygame

from constants import DEFAULT_VEL
from math import floor

class PlayState(GameState):

    def __init__(self):
        super().__init__()
        self.game_size = self.screen_size

    def onEnter(self):
        super().onEnter()
        self.level = Level(self.screen_size, self.game_size, self.state_objs)
        self.menu = None

    def handleInputs(self):
        super().handleInputs()

        self.level.handleInputs(self.events)

        if (self.level.getButtonClicked() != None): 
            self.triggerButton(self.level.getButtonClicked())
            self.level.button_clicked = None

    def triggerButton(self, button_name: str):
        print(button_name)
        if button_name == "pause" and self.menu == None:
            self.level.player.setVel((0, self.level.player.getVel()[1]))
            self.menu = PauseMenu(self.game_size, self.state_objs, "pausemenubg.png")
        elif button_name == "play" or (button_name == "pause" and self.menu != None):
            self.level.player.setVel((DEFAULT_VEL[0], self.level.player.getVel()[1]))
            self.menu = None
        elif button_name == "menu":
            self.setNextState("menustate")
        elif button_name == "restart":
            self.menu = None
            self.restartLevel()

    def togglePauseMenu(self):
        return

    def restartLevel(self):
        del self.level
        self.level = Level(self.screen_size, self.game_size, self.state_objs)

    def update(self):
        self.level.update()

        if self.level.player.getOutcome()[0]:
            print("-------------------\nYou Won\n-------------------")
            quit()
        if self.level.player.getOutcome()[1]:
            self.restartLevel()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.level.bg_img, (0, 0))

        for objects in self.state_objs.values():
            objects: list[GameElement]
            if type(objects[0]) == GameButton and self.menu != None:
                self.menu.draw(screen)
            for object in objects: 
                object.draw(screen)
                # pygame.draw.rect(screen, (255, 0, 0), object.hitbox)