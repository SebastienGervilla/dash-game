import pygame
from GameStates.game_state import GameState
from GameStates.play_state import PlayState
from Menus.main_menu import MainMenu

class MenuState(GameState): #Clear objects

    def __init__(self):
        super().__init__()
        self.game_size = self.screen_size

    def onEnter(self):
        super().onEnter()
        self.menu = MainMenu(self.game_size, self.state_objs, "mainmenubg.png")

    def handleInputs(self):
        super().handleInputs()
        
        for event in self.events:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.menu.checkIsPressed(pygame.mouse.get_pos())
            elif (event.type == pygame.MOUSEBUTTONUP):
                button_clicked = self.menu.checkForClick(pygame.mouse.get_pos())
                if button_clicked != None: 
                    self.setNextState(button_clicked)

    def setNextState(self, button_name: str):
        if button_name == "play":
            super().setNextState(PlayState())
        elif button_name == "level":
            print("----- Working In Progress -----")
        elif button_name == "quit":
            self.is_running = False

    def update(self):
        pass

    def draw(self, screen: pygame.Surface):
        screen.blit(self.menu.bg_img, (0, 0))
        super().draw(screen)