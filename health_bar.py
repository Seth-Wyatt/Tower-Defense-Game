import pygame
from player_list import Player

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour, max_health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.max_health = max_health
        self.health_ratio = 1.0

    def update(self, current_health):
        self.health_ratio = current_health / self.max_health

    def draw(self, surface):
        current_health_width = int(self.width * self.health_ratio)
        health_bar_rect = pygame.Rect(self.x, self.y, current_health_width, self.height)
        pygame.draw.rect(surface, self.colour, health_bar_rect)
