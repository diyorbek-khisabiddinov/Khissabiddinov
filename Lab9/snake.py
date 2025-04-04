import pygame
import sys
import random
import time

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
class Food:
    def __init__(self):
        # Randomly generate food properties
        self.size = random.randint(1, 3)  # Size of the food
        self.value = self.size  # Value of the food (score increment)
        self.x = random.randrange(0, WIDTH, CELL_SIZE)
        self.y = random.randrange(0, HEIGHT, CELL_SIZE)
        self.timestamp = time.time()  # Time when the food was generated
        self.lifespan = random.randint(5, 10)  # Food disappears in 5 to 10 seconds
    
    def is_expired(self):
        # Check if the food has expired (time-based)
        return time.time() - self.timestamp > self.lifespan

# Create the initial food object
food = Food()

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
    if snake_pos == [food.x, food.y]:  # If snake eats the food
        score += food.value
        food = Food()  # Generate new food
        # Level up every 3 points
        if score % 3 == 0:
            level += 1
            speed += 2  # Increase speed
    else:
        snake_body.pop()

    # Check if food is expired and regenerate if necessary
    if food.is_expired():
        food = Food()

    # Draw everything
    screen.fill(BLACK)

    # Draw food (food size can vary)
    pygame.draw.rect(screen, RED, pygame.Rect(food.x, food.y, food.size * CELL_SIZE, food.size * CELL_SIZE))
    
    # Draw snake
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
