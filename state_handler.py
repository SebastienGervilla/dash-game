import pygame

from GameStates.game_state import GameState
from GameStates.play_state import PlayState
from GameStates.menu_state import MenuState

class StateHandler():

    def __init__(self):
        self.is_running = True
        self.curr_state_str = "menustate"
        self.curr_state = MenuState()
        self.curr_state.onEnter()

    def changeGameState(self, game_state: str):
        if game_state == self.curr_state_str:
            return
        
        self.curr_state.onExit()
        del self.curr_state

        self.curr_state_str = game_state
        self.curr_state = self.getCurrentState()

        self.curr_state.onEnter()
        print("State changed...")

    def getCurrentState(self):
        if self.curr_state_str == "playstate":
            curr_state = PlayState()
        elif self.curr_state_str == "menustate":
            curr_state = MenuState()
        else: 
            curr_state = MenuState()
        return curr_state

    def handleInputs(self):
        self.curr_state.handleInputs()

    def update(self):
        self.is_running = self.curr_state.getIsRunning()
        if self.curr_state.getNextState() != None:
            self.changeGameState(self.curr_state.getNextState())
        self.curr_state.update()

    def draw(self, screen: pygame.Surface):
        self.curr_state.draw(screen)

    def getIsRunning(self):
        return self.is_running