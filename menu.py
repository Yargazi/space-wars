import pygame
import sys
from soundButton import SoundButton

class Menu:
    def __init__(self, screen):
        """Initialization of menu"""
        self.screen = screen
        self.font_path = "fonts/Usually-font.otf"
        self.font = pygame.font.Font(self.font_path, 35)
        self.screen_rect = screen.get_rect()
        self.btn_center_x = self.screen_rect.centerx
        self.btn_center_y = self.screen_rect.centery
        self.top_btn_color = 'grey'
        self.main_menu = True
        self.button_rects = []  # Initialize button_rects attribute
        # Создание экземпляра SoundButton
        self.sound_button = SoundButton(screen)
        self.start_clicked = False
        self.game_status = ""

    def draw_bg_img(self):
        # Load background image
        bg = pygame.image.load("img/space-bg-1.jpg")
        self.screen.blit(bg, (0, 0))

        # Display the game title
        title_font_path = "fonts/Usually-font-Bold.otf"
        title_font = pygame.font.Font(title_font_path, 65)
        title_text = title_font.render("Space Invaders", True, "white")
        self.screen.blit(title_text, (185, 230))

    def draw_btn_menu(self, button_texts, game_status):
        pygame.display.set_caption("Menu")
        self.button_rects = []  # Clear previous button rectangles
        self.game_status = game_status


        # Calculate the width of each button as a percentage of the screen width
        screen_width = pygame.display.get_surface().get_width()
        button_width_percentage = 0.3  # 30% of the screen width for button width
        button_width = int(screen_width * button_width_percentage)

        # Calculate the vertical spacing between buttons
        button_height = self.font.get_height() + 30  # Get the height of the font
        spacing = int(button_height * 0.3)  # 30% of the button height for spacing

        # Calculate the total height required for all buttons and spacing
        total_height = (button_height + spacing) * len(button_texts) - spacing

        # Calculate the top position for the first button
        top_y = self.btn_center_y - total_height // 2

        for idx, text in enumerate(button_texts):
            # Check if it's the first button and the game is paused
            if idx == 0 and game_status == "pause":
                text = "Continue"  # Change text for the first button when game is paused

            # Render text surface
            text_surf = self.font.render(text, True, 'black')
            text_rect = text_surf.get_rect(center=(self.btn_center_x, top_y + button_height // 2))

            # Create button rectangle with border and rounded corners
            button_rect = pygame.Rect(self.btn_center_x - button_width // 2, top_y, button_width, button_height)
            pygame.draw.rect(self.screen, '#FFFFFF', button_rect, border_radius=10)
            pygame.draw.rect(self.screen, self.top_btn_color, button_rect, width=2, border_radius=10)

            # Blit text surface
            self.screen.blit(text_surf, text_rect)

            # Update top position for the next button
            top_y += button_height + spacing

            # Add the button rectangle to the list
            self.button_rects.append(button_rect)
            pygame.display.flip()

        return self.button_rects

    def start_game(self):
        """Display the menu"""

        self.sound_button.draw()
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(self.button_rects):
                        if rect.collidepoint(mouse_pos):
                            if i == 0:
                                # Действия при нажатии на кнопку "Start"
                                self.start_clicked = True
                                self.main_menu = False
                                running = False
                                pygame.display.set_caption("Space wars")
                                pygame.display.flip()
                            elif i == 1:
                                print("Settings button clicked")

                            elif i == 2:
                                # Действия при нажатии на кнопку "Exit"
                                sys.exit()
                                print("Exit button clicked")

                    self.sound_button.handle_event(event)

                    # Отрисовка экрана
                    self.draw_bg_img()
                    if self.game_status != "start":
                        button_texts = ["Continue", "Settings", "Exit"]
                    else:
                        button_texts = ["Start", "Settings", "Exit"]

                    # Условие для текста на кнопке "Start" или "Continue"
                    button_texts[0] = "Start" if not self.start_clicked else "Continue"
                    self.draw_btn_menu(button_texts, button_texts[0])


                    # Отрисовка всех объектов, включая кнопку звука
                    self.sound_button.draw()  # Отрисовка кнопки звука

                    # Отображение всех изменений на экране
                    pygame.display.flip()