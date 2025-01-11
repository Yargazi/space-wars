import pygame, sys
from bullet import Bullet
from ufo import Ufo
import time

def events(screen, cannon, bullets, menu, button_texts):
    """Event listener"""
    shot = pygame.mixer.Sound("music/8bit_bomb_explosion.wav")
    shot.set_volume(0.2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, cannon)
                shot.play()
                bullets.add(new_bullet)
            elif event.key == pygame.K_ESCAPE:
                game_status = "pause"
                menu.draw_bg_img()
                menu.draw_btn_menu(button_texts, game_status)
                menu.start_game()
            elif event.key == pygame.K_LEFT:
                cannon.mleft = True
            elif event.key == pygame.K_RIGHT:
                cannon.mright = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                cannon.mright = False
            elif event.key == pygame.K_LEFT:
                cannon.mleft = False

def update(bg_img_path, screen, stats, sc, cannon, ufos, bullets):
    """Screen updating"""
    screen.blit(bg_img_path, (0, 0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    cannon.output()
    ufos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, ufos, bullets, cannon, menu):
    """Updating bullet position"""
    explosion = pygame.mixer.Sound("music/tir.mp3")
    explosion.set_volume(0.2)

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)
    if collisions:
        explosion.play()
        for ufos_hit in collisions.values():
            stats.score += 10 * len(ufos_hit)
            sc.image_score()
            check_high_score(stats, sc)
            sc.image_lives_cannon()

    if len(ufos) == 0:
        bullets.empty()
        if stats.level == -1:  # Endless mode
            """pygame.time.wait(350)  # Wait 0,35 seconds before respawning enemies"""
            create_infinite_army(screen, ufos)
        else:
            stats.level += 1
            create_army(screen, ufos, stats, menu, sc, cannon, bullets)


def restart(stats, screen, sc, cannon, ufos, bullets, menu):
    """Restarting the game"""
    ufos.empty()
    bullets.empty()
    stats.reset_stats()
    stats.menu_displayed = False  # Reset the menu flag
    sc.image_score()
    sc.image_lives_cannon()
    create_army(screen, ufos, stats, menu, sc, cannon, bullets)
    cannon.create_cannon()
    stats.run_game = True
    cannon.mleft = False
    cannon.mright = False
    pygame.display.flip()

def cannon_destroy(stats, screen, sc, cannon, ufos, bullets, menu, infinite_mode=False):
    """Destroying the cannon"""
    ship_explosion = pygame.mixer.Sound("music/ship_explosion.wav")
    ship_explosion.set_volume(0.5)
    ship_explosion.play()

    if not infinite_mode and stats.cannons_left > 1:
        stats.cannons_left -= 1
        sc.image_lives_cannon()
        ufos.empty()
        bullets.empty()
        create_army(screen, ufos, stats, menu, sc, cannon, bullets)
        cannon.create_cannon()
        time.sleep(1)
    else:
        stats.run_game = False
        display_game_over_popup(screen, sc, infinite_mode)
        handle_game_over_menu(stats, screen, sc, cannon, ufos, bullets, menu, infinite_mode)

def display_game_over_popup(screen, sc, infinite_mode):
    size = (1200, 1000)
    GREEN = (34, 0, 68, 50)
    green_image = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.rect(green_image, GREEN, green_image.get_rect())
    screen.blit(green_image, (0, 0))
    sc.game_over_img(infinite_mode)
    sc.show_game_o_pic(infinite_mode)
    pygame.display.update()

def handle_game_over_menu(stats, screen, sc, cannon, ufos, bullets, menu, infinite_mode):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button_text, button_text_rect, button_rect, action in sc.buttons:
                    if button_rect.collidepoint(mouse_pos):
                        if action == "restart":
                            running = False
                            restart(stats, screen, sc, cannon, ufos, bullets, menu)
                        elif action == "main_m":
                            running = False
                            stats.running = False
                            restart(stats, screen, sc, cannon, ufos, bullets, menu)
                            menu.draw_bg_img()
                            menu.draw_btn_menu(["Start", "Settings", "Exit"], "start")
                            menu.start_game()
                            pygame.display.flip()
                        elif action == "endless" and infinite_mode:
                            stats.level = -1
                            stats.run_game = True
                            create_infinite_army(screen, ufos)
                            running = False
                        elif action == "exit":
                            pygame.quit()
                            sys.exit()

def update_ufos(stats, screen, sc, cannon, ufos, bullets, menu):
    ufos.update()
    if pygame.sprite.spritecollideany(cannon, ufos):
        cannon_destroy(stats, screen, sc, cannon, ufos, bullets, menu)
    ufos_check_win(stats, screen, sc, cannon, ufos, bullets, menu)

def ufos_check_win(stats, screen, sc, cannon, ufos, bullets, menu):
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            cannon_destroy(stats, screen, sc, cannon, ufos, bullets, menu)
            break

def create_army(screen, ufos, stats, menu, sc, cannon, bullets):
    screen_width = screen.get_rect().width
    screen_height = screen.get_rect().height
    ufo = Ufo(screen)
    ufo_width = ufo.rect.width
    ufo_height = ufo.rect.height
    num_ufo_x = int(((screen_width - 2 * ufo_width) / ufo_width) / 2)
    num_ufo_y = int(((screen_height - 100 - 2 * ufo_height) / ufo_height) / 2)

    if stats.level == 1:
        create_army_pattern(num_ufo_y - 3, num_ufo_x - 5, screen, 300, 180, 40, 300, 200, ufos)
    elif stats.level > 1 and not stats.menu_displayed:
        stats.menu_displayed = True
        display_game_over_popup(screen, sc, infinite_mode=True)
    else:
        cannon_destroy(stats, screen, sc, cannon, ufos, bullets, menu, infinite_mode=True)

def create_army_pattern(rows, cols, screen, ufo_width, ufo_height, gap, startx, starty, ufos):
    for row in range(rows):
        for col in range(cols):
            ufo = Ufo(screen)
            ufo.x = ufo_width + startx + (ufo_width + gap) * col
            ufo.y = ufo_height + (ufo_height * row) - starty
            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.y
            ufos.add(ufo)

def create_infinite_army(screen, ufos):
    """Creates an infinite enemy army pattern"""
    screen_rect = screen.get_rect()
    for row in range(6):
        for col in range(12):
            ufo = Ufo(screen)
            # Spawn UFOs outside the visible screen
            ufo.x = col * (ufo.rect.width + 20)
            ufo.y = -row * (ufo.rect.height + 20) - ufo.rect.height
            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.y
            ufos.add(ufo)


def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
