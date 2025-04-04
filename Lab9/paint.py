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
mode = "brush"  # Modes: brush, rect, circle, square, rtriangle, etriangle, rhombus, eraser
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
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

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

def set_mode(new_mode):
    global mode
    mode = new_mode

def set_eraser():
    global mode, brush_color
    mode = "eraser"
    brush_color = WHITE

def clear_screen():
    screen.fill(WHITE)

def exit_app():
    pygame.quit()
    sys.exit()

# Button definitions
buttons = [
    Button(10, 10, 60, 30, 'Black', BLACK, set_black),
    Button(80, 10, 60, 30, 'Green', GREEN, set_green),
    Button(150, 10, 60, 30, 'Red', RED, set_red),
    Button(220, 10, 60, 30, 'Blue', BLUE, set_blue),
    Button(290, 10, 60, 30, 'Brush', GRAY, lambda: set_mode("brush")),
    Button(360, 10, 60, 30, 'Rect', GRAY, lambda: set_mode("rect")),
    Button(430, 10, 60, 30, 'Circle', GRAY, lambda: set_mode("circle")),
    Button(500, 10, 60, 30, 'Square', GRAY, lambda: set_mode("square")),
    Button(570, 10, 60, 30, 'R-Tri', GRAY, lambda: set_mode("rtriangle")),
    Button(640, 10, 60, 30, 'E-Tri', GRAY, lambda: set_mode("etriangle")),
    Button(710, 10, 60, 30, 'Rhombus', GRAY, lambda: set_mode("rhombus")),
    Button(10, 50, 60, 30, 'Eraser', GRAY, set_eraser),
    Button(80, 50, 60, 30, 'Clear', GRAY, clear_screen),
    Button(150, 50, 60, 30, 'Exit', GRAY, exit_app)
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
            end_pos = event.pos
            if mode == "rect":
                pygame.draw.rect(screen, brush_color, pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])))
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, brush_color, start_pos, radius)
            elif mode == "square":
                side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos[0], start_pos[1], side, side))
            elif mode == "rtriangle":
                pygame.draw.polygon(screen, brush_color, [start_pos, (start_pos[0], end_pos[1]), end_pos])
            elif mode == "etriangle":
                height = abs(end_pos[1] - start_pos[1])
                top = (start_pos[0], start_pos[1])
                left = (start_pos[0] - height // 2, start_pos[1] + height)
                right = (start_pos[0] + height // 2, start_pos[1] + height)
                pygame.draw.polygon(screen, brush_color, [top, left, right])
            elif mode == "rhombus":
                # Optimized rhombus drawing
                cx = (start_pos[0] + end_pos[0]) // 2
                cy = (start_pos[1] + end_pos[1]) // 2
                dx = (end_pos[0] - start_pos[0]) // 2
                dy = (end_pos[1] - start_pos[1]) // 2
                points = [
                    (cx, start_pos[1]),     # top
                    (end_pos[0], cy),       # right
                    (cx, end_pos[1]),       # bottom
                    (start_pos[0], cy)      # left
                ]
                pygame.draw.polygon(screen, brush_color, points)
            drawing = False

    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 90:
            if mode == "brush" or mode == "eraser":
                pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)
            elif drawing:
                if mode == "rect":
                    pygame.draw.rect(temp_surface, brush_color + (100,), pygame.Rect(min(start_pos[0], mouse_x), min(start_pos[1], mouse_y), abs(mouse_x - start_pos[0]), abs(mouse_y - start_pos[1])))
                elif mode == "circle":
                    radius = int(((mouse_x - start_pos[0]) ** 2 + (mouse_y - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(temp_surface, brush_color + (100,), start_pos, radius)
                elif mode == "square":
                    side = max(abs(mouse_x - start_pos[0]), abs(mouse_y - start_pos[1]))
                    pygame.draw.rect(temp_surface, brush_color + (100,), pygame.Rect(start_pos[0], start_pos[1], side, side))
                elif mode == "rtriangle":
                    pygame.draw.polygon(temp_surface, brush_color + (100,), [start_pos, (start_pos[0], mouse_y), (mouse_x, mouse_y)])
                elif mode == "etriangle":
                    height = abs(mouse_y - start_pos[1])
                    top = (start_pos[0], start_pos[1])
                    left = (start_pos[0] - height // 2, start_pos[1] + height)
                    right = (start_pos[0] + height // 2, start_pos[1] + height)
                    pygame.draw.polygon(temp_surface, brush_color + (100,), [top, left, right])
                elif mode == "rhombus":
                    # Optimized rhombus preview
                    cx = (start_pos[0] + mouse_x) // 2
                    cy = (start_pos[1] + mouse_y) // 2
                    dx = (mouse_x - start_pos[0]) // 2
                    dy = (mouse_y - start_pos[1]) // 2
                    points = [
                        (cx, start_pos[1]),     # top
                        (mouse_x, cy),          # right
                        (cx, mouse_y),          # bottom
                        (start_pos[0], cy)      # left
                    ]
                    pygame.draw.polygon(temp_surface, brush_color + (100,), points)

    # Draw UI
    screen.blit(temp_surface, (0, 0))
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 90))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()