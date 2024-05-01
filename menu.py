import pygame as pg
import sys

def show_menu(screen, font):
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False

        screen.fill((0, 0, 0))  # Black background
        # Title text
        title_text = font.render('Snake for Python', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 4))
        screen.blit(title_text, title_rect)

        # Start game instruction
        start_text = font.render('Press Enter to Start', True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(start_text, start_rect)

        # Movement instruction
        move_text = font.render('WASD and Arrow Keys to move', True, (255, 255, 255))
        move_rect = move_text.get_rect(center=(screen.get_width() / 2, screen.get_height() * 3 / 4))
        screen.blit(move_text, move_rect)

        # Credit text
        credit_text = font.render('Coded by Trei Feske', True, (255, 255, 255))
        credit_rect = credit_text.get_rect(center=(screen.get_width() / 2, screen.get_height() * 7 / 8))
        screen.blit(credit_text, credit_rect)

        pg.display.flip()
        pg.time.Clock().tick(60)
