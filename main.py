import pygame as pg
import sys
from random import randrange
from menu import show_menu  # Make sure this import correctly references your menu file

# Initialize Pygame and create the main window
pg.init()
WINDOW = 1000
screen = pg.display.set_mode((WINDOW, WINDOW))
clock = pg.time.Clock()
font = pg.font.Font(None, 36)  # Adjust the font size or specify a font file if needed

# Display the menu
show_menu(screen, font)

# Game initialization
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)  # Initial direction set to no movement
last_snake_dir = (0, 0)  # Store the last direction
time, time_step = 0, 110  # Time controls for the game
food = snake.copy()
food.center = get_random_position()
dirs = {
    pg.K_w: (0, -TILE_SIZE),
    pg.K_UP: (0, -TILE_SIZE),
    pg.K_s: (0, TILE_SIZE),
    pg.K_DOWN: (0, TILE_SIZE),
    pg.K_a: (-TILE_SIZE, 0),
    pg.K_LEFT: (-TILE_SIZE, 0),
    pg.K_d: (TILE_SIZE, 0),
    pg.K_RIGHT: (TILE_SIZE, 0),
}

# Main game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            new_dir = dirs.get(event.key, None)
            # Prevent reversing direction
            if new_dir and (new_dir[0] != -last_snake_dir[0] or new_dir[1] != -last_snake_dir[1]):
                snake_dir = new_dir
                last_snake_dir = snake_dir  # Update last direction after confirming it's valid

    screen.fill('white')
    # Check border and self-eating
    self_eating = snake.collidelist(segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir, last_snake_dir = 1, (0, 0), (0, 0)
        segments = [snake.copy()]

    # Check food
    if snake.colliderect(food):
        food.center = get_random_position()
        length += 1

    # Draw food
    pg.draw.rect(screen, 'green', food)
    # Draw snake
    for segment in segments:
        pg.draw.rect(screen, 'red', segment)

    # Time-based action
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        # Move snake if direction is set
        if snake_dir:
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]

    pg.display.flip()
    clock.tick(60)
