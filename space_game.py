import pygame, controls
from cannon import Cannon
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from menu import Menu

window_size = width, height = 1200, 1000

def run():
    pygame.init()
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Space wars")

    # Load resources
    bg_img_path = pygame.image.load("img/bg-earth-2.jpg")
    icon = pygame.image.load("img/enemy.png")
    pygame.display.set_icon(icon)

    pygame.mixer.music.load("music/8_Bit_Retro_Funk.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Initialize game components
    timer = pygame.time.Clock()
    fps = 144
    cannon = Cannon(screen)
    bullets = Group()
    ufos = Group()
    stats = Stats()
    sc = Scores(screen, stats)
    menu = Menu(screen)
    button_texts = ["Start", "Settings", "Exit"]

    # Initialize game state
    controls.create_army(screen, ufos, stats, menu, sc, cannon, bullets)
    menu.draw_bg_img()
    menu.draw_btn_menu(button_texts, "start")
    menu.start_game()

    if not menu.main_menu:
        stats.run_game = True
        pygame.display.set_caption("Space wars")

        # Main game loop
        while True:
            timer.tick(fps)
            controls.events(screen, cannon, bullets, menu, button_texts)

            if stats.run_game:
                cannon.update_cannon()
                controls.update(bg_img_path, screen, stats, sc, cannon, ufos, bullets)
                controls.update_bullets(screen, stats, sc, ufos, bullets, cannon, menu)
                controls.update_ufos(stats, screen, sc, cannon, ufos, bullets, menu)
            else:
                # Handle game over popup and reset
                controls.handle_game_over_menu(stats, screen, sc, cannon, ufos, bullets, menu, infinite_mode=True)
    else:
        print("Something went wrong...")


if __name__ == "__main__":
    run()
