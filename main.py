import pygame
from game import Game

from constants import SCREEN_SIZE

def main():

    pygame.init()

    game = Game(SCREEN_SIZE, SCREEN_SIZE)
    game_clock = pygame.time.Clock()
    
    while(game.getIsRunning()):
        
        game.handleInputs()
        game.update()
        game.draw()

        game_clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()