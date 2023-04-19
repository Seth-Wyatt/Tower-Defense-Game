import pygame
import math

WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour, max_health):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.colour = colour

        self.center_x = self.rect.x + x/2
        self.center_y = self.rect.y + y/2

        self.max_health = 10
        self.health = self.max_health
        self.fire_rate = 10
        self.dmg = 1
        self.regen = 0
        self.block_chance = 0
        self.block_percent = 0
        self.crit_chance = 0
        self.crit_dmg = 0

        # Create a surface for the player
        self.image = pygame.Surface([width, height])
        self.image.fill(self.colour)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
