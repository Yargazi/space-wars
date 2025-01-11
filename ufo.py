import pygame, random

class Ufo(pygame.sprite.Sprite):
    """class of one ufo"""

    def __init__(self, screen):
        """initialization and start point"""
        super(Ufo, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/enemy.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.last_call_time = 0
        self.direction = ""

    def draw(self):
        """showing ufo on screen"""
        self.screen.blit(self.image, self.rect)


    def moving_randomly(self):


        if self.direction == "Right":
            self.x += 80
            self.rect.x = self.x
            self.direction = "Left"

        else:
            self.x -= 80
            self.rect.x = self.x
            self.direction = "Right"


    def update(self):
        """moving down army def = 0.5"""
        self.y += 2
        self.rect.y = self.y


        call_interval = 2000 #random.randint(3000, 5000)
        current_time = pygame.time.get_ticks()


        # Проверка, прошло ли достаточно времени для вызова функции
        if current_time - self.last_call_time > call_interval:
            self.moving_randomly()
            self.last_call_time = current_time




