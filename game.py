import pygame
from state_handler import StateHandler

class Game():

    def __init__(self, screen_size: tuple, game_size: tuple):
        self.setScreen(screen_size)
        self.state_handler = StateHandler()

        self.game_size = game_size
        self.is_running = True

    def setScreen(self, screen_size: tuple):
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Dash Game')

    def handleInputs(self):
        self.state_handler.handleInputs()

    def update(self):
        self.is_running = self.state_handler.getIsRunning()
        self.state_handler.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.state_handler.draw(self.screen)
        pygame.display.flip()

    def getIsRunning(self):
        return self.is_running