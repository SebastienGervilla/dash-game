import pygame

from GameStates.game_state import GameState
from GameStates.play_state import PlayState
from GameStates.menu_state import MenuState

class StateHandler():

    def __init__(self):
        self.is_running = True
        self.curr_state = MenuState()
        self.curr_state.onEnter()

    def changeGameState(self, game_state: GameState):
        if isinstance(game_state, type(self.curr_state)):
            return
        
        self.curr_state.onExit()
        del self.curr_state

        self.curr_state = game_state
        self.curr_state.onEnter()
        print("State changed...")

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