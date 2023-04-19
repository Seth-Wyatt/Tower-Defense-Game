import pygame
import math

class Bullet():
    def __init__(self, x, y, speed, enemies, bullets):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = (0, 0)
        self.enemies = list(enemies)
        self.closest_enemy = None
        self.bullets = bullets
        self.hit_enemy = False
        self.target = None

    def update(self):
        if not self.enemies:
            return

        if self.hit_enemy:
            if self.target.health > 0:
                self.target.health -= 1
            self.bullets.remove(self)
            return

        self.closest_enemy = min(self.enemies, key=lambda e: math.sqrt((self.x - e.rect.centerx) ** 2 + (self.y - e.rect.centery) ** 2))
        dx = self.closest_enemy.rect.centerx - self.x
        dy = self.closest_enemy.rect.centery - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        self.direction = (dx / dist, dy / dist)

        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

        for enemy in self.enemies:
            if enemy.rect.colliderect(pygame.Rect(self.x, self.y, 5, 5)):
                self.hit_enemy = True
                self.target = enemy


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 5)
