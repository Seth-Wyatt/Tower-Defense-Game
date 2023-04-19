import pygame

BLACK = (0, 0, 0)

class UpgradesBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour, border_colour, border_size, id, text, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.colour = colour
        self.border_colour = border_colour
        self.border_size = border_size
        self.id = id
        self.font_size = font_size
        self.font = pygame.font.SysFont('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*', font_size)
        self.text = text
        self.label = self.font.render(text, True, (255, 255, 255))
        self.label_rect = self.label.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        pygame.draw.rect(screen, self.border_colour, self.rect, self.border_size)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self
        return None