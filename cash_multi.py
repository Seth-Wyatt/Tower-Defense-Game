from cash_upgrades import CashUpgrades
import pygame

GREEN = (0, 255, 0)

class CashMulti(CashUpgrades):
    def __init__(self, x, y, width, height, colour, border_colour, border_size, id, text, font_size):
        super().__init__(x, y, width, height, colour, border_colour, border_size, id, text, font_size)

        self.colour_2 = GREEN
        cash_multi_boost = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        pygame.draw.rect(screen, self.border_colour, self.rect, self.border_size)
        screen.blit(self.label, self.label_rect)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if upgrade_ready == True:
                    cash_multi_boost += 1

    def upgrade_ready(self, colour):
        if upgrade_ready == True:
            pygame.draw.rect(screen, self.colour_2, self.rect)
