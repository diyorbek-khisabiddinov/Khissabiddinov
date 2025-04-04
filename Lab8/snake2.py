import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 10
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game with Levels')

# Snake setup
snake_pos = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]
direction = 'RIGHT'
change_to = direction

# Food setup
def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if [x, y] not in snake_body:
            return [x, y]

food_pos = spawn_food()

# Game variables
score = 0
level = 1
speed = 10
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
    direction = change_to

    # Move snake
    if direction == 'UP':
        snake_pos[1] -= CELL_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += CELL_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= CELL_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += CELL_SIZE

    # Check for wall collision
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        running = False  # Game over

    # Check for self collision
    if snake_pos in snake_body[1:]:
        running = False  # Game over

    # Update snake body
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_pos = spawn_food()
        # Level up every 3 points
        if score % 3 == 0:
            level += 1
            speed += 2  # Increase speed
    else:
        snake_body.pop()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))
    
    # Display score and level
    font = pygame.font.SysFont('Arial', 20)
    score_text = font.render(f'Score: {score}  Level: {level}', True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()