from Objects.GameElements.game_element import GameElement
from Objects.GameElements.block import Block
from Objects.GameElements.spike import Spike
from Objects.GameElements.orb import Orb
from Objects.GameElements.end import End

import pygame
from constants import GRAVITY

class Player(GameElement):

    def __init__(self, velocity: tuple, pos: tuple, img_name: str):
        super().__init__(pos, img_name)
        self.base_img = self.image
        self.resizeImage()

        self.angle = 0
        self.jump_height = 13
        self.velocity = list(velocity)
        self.rotated_img = self.image
        self.rotated_rect = self.rect

        self.on_ground = False
        self.is_jumping = False
        self.is_dead = False
        self.has_won = False

    def jump(self):
        self.is_jumping = True

    def move(self):
        self.velocity[1] -= self.jump_height

    def update(self, platforms: list[GameElement]):
        if self.is_jumping:
            if self.on_ground:
                self.move()
                self.on_ground = False

        if not self.on_ground:
            pass
        
        self.velocity[1] += GRAVITY

        if self.velocity[1] > 50:
            self.velocity[1] = 50

        self.collide(0, platforms)

        self.rect.y += self.velocity[1]

        self.on_ground = False

        self.collide(self.velocity[1], platforms)

        self.rotatePlayer()
        self.pos = [self.rect.x, self.rect.y]

    def collide(self, vel: int, platforms: list[GameElement]):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, Orb):
                    self.move() #add orbs
                if isinstance(p, Block):
                    if vel > 0:
                        self.rect.bottom = p.rect.top
                        self.velocity[1] = 0
                        self.on_ground = True
                        self.is_jumping = False
                    elif vel < 0:
                        self.velocity[0] = 0
                        self.rect.top = p.rect.bottom
                        self.is_dead = True
                    else:
                        self.velocity[0] = 0
                        self.rect.right = p.rect.left
                        self.is_dead = True
                if isinstance(p, Spike):
                    if self.rect.colliderect(p.hitbox):
                        self.is_dead = True
                if isinstance(p, End):
                    self.has_won = True

    def calculateAngle(self):
        if not self.on_ground:
            if self.angle < -360: self.angle += 360
            self.angle = round(self.angle - 7.2, 1)
        else:
            multiplier = 1
            closest_angle = round(self.angle / 90) * 90
            if closest_angle - self.angle <= 0: multiplier = -1
            if (self.angle + 7.2 * multiplier) * multiplier > (closest_angle) * multiplier:
                self.angle += closest_angle - self.angle
            else:
                self.angle += 7.2 * multiplier

    def rotatePlayer(self):
        self.calculateAngle()
        self.rotated_img = pygame.transform.rotate(self.base_img, self.angle)
        self.rotated_rect = self.rotated_img.get_rect(center = self.image.get_rect(topleft=self.pos).center)

    def setVel(self, vel: tuple):
        self.velocity = list(vel)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.rotated_img, self.rotated_rect)

    def getPos(self):
        return self.pos
    
    def getRect(self):
        return self.rect

    def getVel(self):
        return self.velocity

    def getOutcome(self):
        return (self.has_won, self.is_dead)