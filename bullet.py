import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, cannon):
        """creating bullet in a top of gun"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.image_bullet = pygame.image.load('img/bullet.png')
        self.image_bullet = pygame.transform.scale(self.image_bullet, (1160, 90))
        self.rect = self.image_bullet.get_rect()

        self.speed = 6
        self.rect.centerx = cannon.rect.centerx
        self.rect.top = cannon.rect.top
        self.y = float(self.rect.y)


    def update(self):
        """moving up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """drawing a bullet"""
        """pygame.draw.rect(self.screen, self.rect)"""
        self.screen.blit(self.image_bullet, self.rect)
