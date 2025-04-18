import pygame
import sys
import random
import time
import sqlite3

# -------------------- Database Setup --------------------
def init_db():
    conn = sqlite3.connect("snake_game.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        score INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        FOREIGN KEY (user_id) REFERENCES user (id)
    )""")
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect("snake_game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM user WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute("INSERT INTO user (username) VALUES (?)", (username,))
        conn.commit()
        user_id = cursor.lastrowid
        cursor.execute("INSERT INTO user_score (user_id) VALUES (?)", (user_id,))
        conn.commit()
        level = 1
    else:
        user_id = user[0]
        cursor.execute("SELECT level FROM user_score WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        level = result[0] if result else 1
    conn.close()
    return user_id, level

def save_game(user_id, score, level):
    conn = sqlite3.connect("snake_game.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE user_score SET score = ?, level = ? WHERE user_id = ?", (score, level, user_id))
    conn.commit()
    conn.close()

# -------------------- Game Setup --------------------
pygame.init()
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 10
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game with Levels')

font = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()

# Start screen
def start_screen():
    while True:
        screen.fill(BLACK)
        title = font.render("Press ENTER to Start", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - title.get_height()//2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

start_screen()

# Get user
init_db()
username = input("Enter your username: ")
user_id, level = get_user(username)
print(f"Welcome {username}, starting from Level {level}")

# Level configuration
LEVELS = {
    1: {"speed": 10, "walls": []},
    2: {"speed": 15, "walls": [(100, 100, 200, 10)]},
    3: {"speed": 20, "walls": [(100, 100, 200, 10), (300, 200, 10, 150)]},
}

snake_pos = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]
direction = 'RIGHT'
change_to = direction

class Food:
    def __init__(self):
        self.size = random.randint(1, 3)
        self.value = self.size
        self.x = random.randrange(0, WIDTH - CELL_SIZE * self.size, CELL_SIZE)
        self.y = random.randrange(0, HEIGHT - CELL_SIZE * self.size, CELL_SIZE)
        self.timestamp = time.time()
        self.lifespan = random.randint(5, 10)
        self.rect = pygame.Rect(self.x, self.y, self.size * CELL_SIZE, self.size * CELL_SIZE)

    def is_expired(self):
        return time.time() - self.timestamp > self.lifespan

food = Food()
score = 0
speed = LEVELS.get(level, LEVELS[1])["speed"]
paused = False

# -------------------- Main Loop --------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(user_id, score, level)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_game(user_id, score, level)
            elif not paused:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

    if paused:
        pygame.time.delay(100)
        continue

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= CELL_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += CELL_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= CELL_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += CELL_SIZE

    snake_rect = pygame.Rect(snake_pos[0], snake_pos[1], CELL_SIZE, CELL_SIZE)

    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        save_game(user_id, score, level)
        break
    if snake_pos in snake_body[1:]:
        save_game(user_id, score, level)
        break

    for wall in LEVELS.get(level, {}).get("walls", []):
        wall_rect = pygame.Rect(*wall)
        if snake_rect.colliderect(wall_rect):
            save_game(user_id, score, level)
            running = False
            break

    snake_body.insert(0, list(snake_pos))
    if snake_rect.colliderect(food.rect):
        score += food.value
        food = Food()
        if score % 3 == 0:
            level = min(level + 1, max(LEVELS.keys()))
            speed = LEVELS[level]["speed"]
    else:
        snake_body.pop()

    if food.is_expired():
        food = Food()

    screen.fill(BLACK)

    for wall in LEVELS.get(level, {}).get("walls", []):
        pygame.draw.rect(screen, WHITE, pygame.Rect(*wall))

    pygame.draw.rect(screen, RED, food.rect)

    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

    score_text = font.render(f'Score: {score}  Level: {level}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()
