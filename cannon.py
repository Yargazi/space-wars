import pygame
from pygame.sprite import Sprite

class Cannon(Sprite):

    def __init__(self, screen, initial_size=(100, 100)):
        """initialization of cannon"""
        super(Cannon, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/star_ship.png')
        self.image = pygame.transform.scale(self.image, initial_size)
        self.current_img = self.image
        self.rect = self.current_img.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False



    def output(self):
        """showing a cannon"""
        self.screen.blit(self.current_img, self.rect)

    def update_cannon(self):
        """checking position of cannon and borderSCR"""
        self.rect.centerx = self.center
        
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 10

        if self.mleft and self.rect.left > 0:
            self.center -= 10

    def create_cannon(self):
        """creation a new cannon"""
        self.center = self.screen_rect.centerx

