import pygame, sys
from cannon import Cannon
from pygame.sprite import Group

class Scores():
    """Show game info and UI elements."""
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.font_path = "fonts/Invasion.ttf"
        self.font = pygame.font.Font(self.font_path, 40)
        self.bigfont = pygame.font.Font(self.font_path, 60)
        self.text_color = (34, 66, 131)
        self.image_score()
        self.image_high_score()
        self.image_lives_cannon()
        self.restart_btn_img(False)

    def image_score(self):
        """Create image from score counter."""
        self.score_img = self.font.render(
            f"Current: {self.stats.score}", True, self.text_color, (0, 0, 0)
        )
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """Transform high score into an image."""
        self.high_score_image = self.font.render(
            f"Top score: {self.stats.high_score}", True, self.text_color, (0, 0, 0)
        )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 22

    def image_lives_cannon(self):
        """Display cannon lives as icons."""
        self.cannons = Group()
        for cannon_num in range(self.stats.cannons_left):
            cannon_life = Cannon(self.screen, initial_size=(50, 50))
            cannon_life.rect.x = 15 + cannon_num * cannon_life.rect.width
            cannon_life.rect.y = 20
            self.cannons.add(cannon_life)

    def show_score(self):
        """Show score on screen."""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.cannons.draw(self.screen)

    def game_over_img(self, infinite_mode=False):
        """Display appropriate message and result based on the mode."""
        y_offset = int(self.screen_rect.height * 0.1)

        if infinite_mode:
            # Endless mode messages
            messages = [
                "Welcome to Endless Mode!",
                "Survive as long as you can!",
                f"Your result: {self.stats.score}"
            ]

            for message in messages:
                line = self.bigfont.render(message, True, (255, 255, 255), (34, 66, 131))
                line_rect = line.get_rect()
                line_rect.centerx = self.screen_rect.centerx
                line_rect.y = y_offset
                self.screen.blit(line, line_rect)
                y_offset += line.get_height() + 10  # Add spacing between lines

        else:
            # Game over message
            self.result_img = self.bigfont.render(
                f"Game over! Your result: {self.stats.score}",
                True, (255, 255, 255), (34, 66, 131)
            )
            self.result_rect = self.result_img.get_rect()
            self.result_rect.centerx = self.screen_rect.centerx
            self.result_rect.y = y_offset
            self.screen.blit(self.result_img, self.result_rect)

    def create_buttons(self, button_info):
        """Create buttons based on provided info."""
        buttons = []
        for text, position, action in button_info:
            button_text = self.font.render(text, True, (225, 225, 225))
            button_text_rect = button_text.get_rect(center=position)
            button_width = button_text_rect.width + 20
            button_height = button_text_rect.height + 20
            button_rect = pygame.Rect(0, 0, button_width, button_height)
            button_rect.center = position
            buttons.append((button_text, button_text_rect, button_rect, action))
        return buttons

    def restart_btn_img(self, infinite_mode):
        """Create buttons with actions."""
        if infinite_mode:
            # Adjust button positions for infinite mode
            button_start_y = self.screen_rect.centery   # Adjust starting position
            button_spacing = 90  # Spacing between buttons

            button_info = [
                ("Infinity", (self.screen_rect.centerx, button_start_y - button_spacing), "endless"),
                ("Restart", (self.screen_rect.centerx, button_start_y), "restart"),
                ("Main menu", (self.screen_rect.centerx, button_start_y + button_spacing), "main_m"),
                ("Exit", (self.screen_rect.centerx, button_start_y + 2 * button_spacing), "exit")
            ]
        else:
            # Adjust button positions for game over (non-infinite mode)
            button_start_y = self.screen_rect.top + 240   # Adjust starting position
            button_spacing = 90  # Spacing between buttons

            button_info = [
                ("Restart", (self.screen_rect.centerx, button_start_y), "restart"),
                ("Main menu", (self.screen_rect.centerx, button_start_y + button_spacing), "main_m"),
                ("Exit", (self.screen_rect.centerx, button_start_y + 2 * button_spacing), "exit")
            ]

        self.buttons = self.create_buttons(button_info)

    def show_game_o_pic(self, infinite_mode=False):
        """Show game over screen with buttons."""
        self.restart_btn_img(infinite_mode)

        # Draw buttons
        for button_text, button_text_rect, button_rect, _ in self.buttons:
            pygame.draw.rect(self.screen, (34, 66, 131), button_rect, 0, 15)
            pygame.draw.rect(self.screen, (255, 255, 255), button_rect, 2, 15)
            self.screen.blit(button_text, button_text_rect)

    def wrap_text(self, text, max_width):
        """Wrap text to fit within a specified width."""
        words = text.split(" ")
        wrapped_lines = []
        current_line = ""

        for word in words:
            # Check if adding the next word exceeds the width
            test_line = current_line + " " + word if current_line else word
            rendered_line = self.font.render(test_line, True, (255, 255, 255))
            if rendered_line.get_width() > max_width:
                # Commit the current line and start a new one
                wrapped_lines.append(current_line)
                current_line = word
            else:
                current_line = test_line

        # Add the last line
        if current_line:
            wrapped_lines.append(current_line)

        return wrapped_lines
