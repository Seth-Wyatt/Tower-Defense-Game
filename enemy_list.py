import pygame
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour, health, speed, damage, target):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.colour = colour

        self.damage = damage

        self.center_x = self.x + width/2
        self.center_y = self.y + height/2

        self.image = pygame.Surface([width, height])
        self.image.fill(self.colour)

        self.health = 1
        self.speed = speed
        self.direction = (0, 0)
        self.target = list(target)
        self.closest_target = None


    def update(self):
        self.closest_target = min(self.target, key=lambda p: math.sqrt((self.x - p.rect.centerx) ** 2 + (self.y - p.rect.centery) ** 2))
        dx = self.closest_target.rect.centerx - self.center_x
        dy = self.closest_target.rect.centery - self.center_y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        self.direction = (dx / dist, dy / dist)

        # Move the enemy in the calculated direction
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.health <= 0:
            self.kill()
    def draw(self, screen):
        screen.blit(self.image, self.rect)