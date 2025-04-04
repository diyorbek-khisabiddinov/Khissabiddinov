import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Paint')

# Brush settings
drawing = False
brush_color = BLACK
mode = "brush"  # Modes: brush, rect, circle, eraser
start_pos = None  # To store initial position for shapes
temp_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Temporary surface for preview

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 25)
        text_surface = font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 5))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.action()

# Button actions
def set_black():
    global brush_color
    brush_color = BLACK

def set_green():
    global brush_color
    brush_color = GREEN

def set_red():
    global brush_color
    brush_color = RED

def set_blue():
    global brush_color
    brush_color = BLUE

def set_brush():
    global mode
    mode = "brush"

def set_rect():
    global mode
    mode = "rect"

def set_circle():
    global mode
    mode = "circle"

def set_eraser():
    global mode, brush_color
    mode = "eraser"
    brush_color = WHITE

def clear_screen():
    screen.fill(WHITE)

def exit_app():
    pygame.quit()
    sys.exit()

# Buttons
buttons = [
    Button(10, 10, 60, 30, 'Black', BLACK, set_black),
    Button(80, 10, 60, 30, 'Green', GREEN, set_green),
    Button(150, 10, 60, 30, 'Red', RED, set_red),
    Button(220, 10, 60, 30, 'Blue', BLUE, set_blue),
    Button(290, 10, 60, 30, 'Brush', GRAY, set_brush),
    Button(360, 10, 60, 30, 'Rect', GRAY, set_rect),
    Button(430, 10, 60, 30, 'Circle', GRAY, set_circle),
    Button(500, 10, 60, 30, 'Eraser', GRAY, set_eraser),
    Button(570, 10, 60, 30, 'Clear', GRAY, clear_screen),
    Button(640, 10, 60, 30, 'Exit', GRAY, exit_app)
]

# Fill screen initially
clear_screen()

# Main loop
while True:
    temp_surface.fill((0, 0, 0, 0))  # Clear temp surface
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for button in buttons:
            button.check_action(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == "rect":
                pygame.draw.rect(screen, brush_color, pygame.Rect(min(start_pos[0], event.pos[0]), min(start_pos[1], event.pos[1]), abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1])))
            elif mode == "circle":
                radius = int(((event.pos[0] - start_pos[0]) ** 2 + (event.pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, brush_color, start_pos, radius)
            drawing = False

    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:
            if mode == "brush" or mode == "eraser":
                pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)
            elif mode == "rect" and drawing:
                pygame.draw.rect(temp_surface, brush_color + (100,), pygame.Rect(min(start_pos[0], mouse_x), min(start_pos[1], mouse_y), abs(mouse_x - start_pos[0]), abs(mouse_y - start_pos[1])))
            elif mode == "circle" and drawing:
                radius = int(((mouse_x - start_pos[0]) ** 2 + (mouse_y - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(temp_surface, brush_color + (100,), start_pos, radius)
    
    screen.blit(temp_surface, (0, 0))
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 50))
    for button in buttons:
        button.draw(screen)
    
    pygame.display.flip()
