import pygame
from GameStates.game_state import GameState
from level import Level

class PlayState(GameState):

    def __init__(self):
        super().__init__()
        self.game_size = self.screen_size

    def onEnter(self):
        super().onEnter()
        self.level = Level(self.screen_size, self.game_size, self.state_objs)

    def handleInputs(self):
        super().handleInputs()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]):
            self.level.player.jump()

    def update(self):
        self.level.update()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.level.bg_img, (0, 0))
        super().draw(screen)