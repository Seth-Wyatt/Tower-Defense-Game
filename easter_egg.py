from home_screen import *
import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class EasterEgg(HomeScreen):
    def __init__(self, x, y, width, height, colour, border_colour, border_size, id, text, font_size):

        self.rect = pygame.Rect(x, y, width, height)
        self.colour = colour
        self.border_colour = border_colour
        self.border_size = border_size
        self.id = id
        self.font_size = font_size
        self.font = pygame.font.SysFont('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*', font_size)
        self.text = text
        self.label = self.font.render(text, True, (BLACK))
        self.label_rect = self.label.get_rect(center=self.rect.center)
        self.last_compliment = None
        compliments = [
        "You have a heart of gold",
        "You light up the room",
        "You're a natural leader",
        "You're so creative and imaginative",
        "You're incredibly talented",
        "You have a great sense of humor",
        "You're an amazing listener",
        "You're inspiring",
        "You're a great friend",
        "You have a contagious smile",
        "You're intelligent and witty",
        "You have a captivating personality",
        "You're one of a kind",
        "You're brave and courageous",
        "You're so generous and giving",
        "You have a beautiful soul",
        "You have a sharp mind",
        "You're a fantastic problem solver",
        "You're always there for me",
        "You make the world a better place",
        "You have an infectious energy",
        "You're so graceful and elegant",
        "You have a keen eye for detail",
        "You have a great work ethic",
        "You're wise beyond your years",
        "You have a great sense of style",
        "You have a warm and caring nature",
        "You have a wonderful sense of adventure",
        "You have a unique perspective on life",
        "You're so full of positivity and optimism",
        "You have a brilliant mind",
        "You're so thoughtful and considerate",
        "You're so selfless and compassionate",
        "You have a powerful presence",
        "You have a fantastic sense of humor",
        "You're an incredible problem solver",
        "You have a great taste in music",
        "You're a true inspiration to others",
        "You have a magnetic personality",
        "You're so humble and down-to-earth",
        "You have an infectious laugh",
        "You have an incredible work ethic",
        "You have a fantastic sense of humor",
        "You're always willing to help others",
        "You're so talented and skilled",
        "You have a beautiful singing voice",
        "You're so easy to talk to",
        "You're so kind and generous",
        "You have a great sense of humor",
        "You make everyone around you feel special",
        ]
        self.compliments = compliments

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        pygame.draw.rect(screen, self.border_colour, self.rect, self.border_size)
        screen.blit(self.label, self.label_rect)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self
        return None

    def compliment(self):
        random_compliment = random.choice(self.compliments)
        while random_compliment == self.last_compliment:
            random_compliment = random.choice(self.compliments)

        self.last_compliment = random_compliment

        self.text = random_compliment
        self.label = self.font.render(random_compliment, True, WHITE)
        self.label_rect = self.label.get_rect(center=self.rect.center)