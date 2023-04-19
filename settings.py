from upgrades_bar import *
import pygame

class Settings(UpgradesBar):
    def __init__(self, x, y, width, height, colour, border_colour, border_size, id, text, font_size):
        super().__init__(x, y, width, height, colour, border_colour, border_size, id, text, font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        pygame.draw.rect(screen, self.border_colour, self.rect, self.border_size)
        screen.blit(self.label, self.label_rect)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self
        return None