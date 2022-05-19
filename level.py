import csv
import pygame
from objects.gameElements import GameElement
from player import Player
from objects.block import Block
from objects.spike import Spike
from objects.end import End

class Level():

    def __init__(self, screen_size: tuple, game_size: tuple, image_set: dict, player: Player):
        self.screen_size = screen_size
        self.game_size = game_size
        self.image_set = image_set
        self.objects = pygame.sprite.Group()
        self.player = player
        self.generateMap()
        self.setLevel()
        
    def setLevel(self):
        x = 0
        y = self.game_size[1]
        for row in reversed(self.lvl):
            for col in row:
                if col == "0":
                    Block(self.image_set["block"], (x , y) , self.objects)
                elif col == "1":
                    Spike(self.image_set["spike"], (x , y) , self.objects)
                elif col == "2":
                    End(self.image_set["end"], (x , y) , self.objects)
                x += 32
            y -= 32
            x = 0


    def generateMap(self):
        self.lvl = []
        with open("levels/Level1.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                self.lvl.append(row)
        return self.lvl

    def update(self):
        self.player.update(self.objects)
        if self.player.getOutcome()[0]:
            print("-------------------\nYou Won\n-------------------")
            quit()
        if self.player.getOutcome()[1]:
            print("-------------------\nYou lost\n-------------------")
            quit()
        self.moveMap()

    def moveMap(self):
        for object in self.objects:
            object: GameElement
            object.rect.x -= self.player.getVel()[0]
            object.updateHitbox()

    def getObjects(self):
        return self.objects