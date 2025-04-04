import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame
pygame.init()

# Set the frames per second
FPS = 60
clock = pygame.time.Clock()

# Define color constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
W, H = 400, 600

# Initial speed, score, and coins
SPEED = 5
SCORE = 0
COINS = 0

# Load fonts for game text
font = pygame.font.Font(r"/Users/khissabiddinovdiyorbek/Desktop/PP2/Lab8/font_user (1).ttf", 60)
font_small = pygame.font.Font(r"/Users/khissabiddinovdiyorbek/Desktop/PP2/Lab8/font_user (1).ttf", 20)

# Render the "Game Over" message
game_over = font.render("Game Over", True, BLACK)

# Load and scale the coin icon for display
coin_icon = pygame.image.load(r"/Users/khissabiddinovdiyorbek/Desktop/PP2/Lab8/coin.jpg")
coin_icon = pygame.transform.scale(coin_icon, (coin_icon.get_width()//20, coin_icon.get_height()//20))

# Load background image
bg = pygame.image.load(r"/Users/khissabiddinovdiyorbek/Desktop/PP2/Lab8/way.jpg")

# Set up the display window
SC = pygame.display.set_mode((W, H))
SC.fill(WHITE)
pygame.display.set_caption("My game")

# Enemy class — moves vertically downward and resets when off-screen
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"/Users/khissabiddinovdiyorbek/Desktop/PP2/Lab8/enemy.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1  # Increase score when enemy passes player
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)

# Player class — moves left and right with arrow keys
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"/Users/khissabiddinovdiyorbek/Desktop/PP2/Lab8/car.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 1:
            if pressed_key[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Coin class — falls down and resets position after going off-screen
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"/Users/khissabiddinovdiyorbek/Desktop/PP2/Lab8/coin.jpg")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//12, self.image.get_height()//12))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)

# Create game entities
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins_group = pygame.sprite.Group()
coins_group.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Set up a custom event to increase speed every 4 seconds
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 4000)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1  # Increase difficulty over time

        if event.type == QUIT:
            pygame.quit()
            exit()

    # Draw background and coin icon
    SC.blit(bg, (0, 0))
    SC.blit(coin_icon, (10, 35))

    # Display collected coins
    coins_v = font_small.render(f"X{str(COINS)}", True, BLACK)
    SC.blit(coins_v, (50, 50))

    # Draw and update all sprites
    for entity in all_sprites:
        SC.blit(entity.image, entity.rect)
        entity.move()

    # Check collision between player and enemy — Game Over
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"/Users/khissabiddinovdiyorbek/Desktop/PP2/Lab8/crash.wav").play()
        time.sleep(0.5)

        # Show Game Over screen
        SC.fill(RED)
        SC.blit(game_over, (30, 250))
        result = font_small.render(f"Your result: {COINS}", True, BLACK)
        SC.blit(result, (120, 350))
        pygame.display.update()

        # Remove all sprites and end game
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check if player collects a coin
    if pygame.sprite.spritecollideany(P1, coins_group):
        COINS += 1  # Increase coin count
        for i in coins_group:
            # Reset coin position after collection
            i.rect.top = 0
            i.rect.center = (random.randint(40, W-40), 0)

    # Refresh screen and control frame rate
    pygame.display.update()
    clock.tick(FPS)