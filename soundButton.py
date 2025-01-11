import pygame

class SoundButton():

    def __init__(self, screen):
        self.screen = screen
        self.initial_size = (30, 30)
        self.sound_on_img = pygame.image.load("img/music_on.png")
        self.sound_off_img = pygame.image.load("img/music_off.png")
        self.sound_on_img = pygame.transform.scale(self.sound_on_img, self.initial_size)
        self.sound_off_img = pygame.transform.scale(self.sound_off_img, self.initial_size)
        self.current_img = self.sound_on_img
        self.rect = self.current_img.get_rect()
        self.rect.topleft = (10, 10)  # Position of the sound button
        self.music_paused = True  # Initial state of the music

    def toggle_sound(self):
        if self.music_paused:
            pygame.mixer.music.pause()
            self.current_img = self.sound_off_img  # Обновляем текущее изображение кнопки
        else:
            pygame.mixer.music.unpause()
            self.current_img = self.sound_on_img  # Обновляем текущее изображение кнопки

        self.music_paused = not self.music_paused
        self.screen.blit(self.current_img, self.rect)
        pygame.display.flip()


    def draw(self):
        self.screen.blit(self.current_img, self.rect)
        pygame.display.flip()
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos): # here error why it blinking
                self.toggle_sound()


