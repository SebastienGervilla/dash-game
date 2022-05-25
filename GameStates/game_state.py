from __future__ import annotations
import pygame
from Objects.GameElements.game_element import GameElement
from constants import SCREEN_SIZE

class GameState():

    def __init__(self):
        self.next_state = None
        self.is_running = True
        self.screen_size = SCREEN_SIZE
        self.state_objs = {}

    def onEnter(self):
        print("Entered a new state...")

    def onExit(self):
        print("Leaving current state...")

    def handleInputs(self):
        self.events = pygame.event.get()
        for event in self.events:
            if (event.type == pygame.QUIT):
                self.is_running = False

    def update(self):
        pass

    def draw(self, screen: pygame.Surface):
        for objects in self.state_objs.values():
            objects: list[GameElement]
            for object in objects: 
                object.draw(screen)
                # pygame.draw.rect(screen, (255, 0, 0), object.hitbox)

    def setNextState(self, next_state: GameState):
        self.next_state = next_state

    def getNextState(self):
        return self.next_state

    def getIsRunning(self):
        return self.is_running