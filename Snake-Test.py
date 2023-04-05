import pygame
import random

pygame.init()

# Define the window size
window_width = 600
window_height = 400

# Create a window
screen = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Snake Game")

snake_block = 10

# Define the initial position of the snake
x1 = window_width / 2
y1 = window_height / 2

x1_change = 0       
y1_change = 0

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        # Move the snake using arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
                
    # Move the snake
    x1 += x1_change
    y1 += y1_change
    
    # Fill the background color
    screen.fill((255, 255, 255))
    
    # Draw the snake
    pygame.draw.rect(screen, (0, 0, 0), [x1, y1, snake_block, snake_block])
    
    # Update the screen
    pygame.display.update()
    
    # Set the FPS of the game
    clock = pygame.time.Clock()
    clock.tick(30)

# Quit Pygame
pygame.quit()
