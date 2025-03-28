import pygame 
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("third task")

step = 20
running = True
white = (255, 255, 255)
red = (255, 0, 0)
radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

while running: 
    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), radius)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and  ball_y-radius-step >= 0: 
                ball_y -= step  
            if event.key == pygame.K_DOWN and ball_y+radius+step <= HEIGHT: 
                ball_y += step
            if event.key == pygame.K_LEFT and ball_x-radius-step >= 0:
                ball_x -= step
            if event.key == pygame.K_RIGHT and ball_x+radius+step <= WIDTH:
                ball_x += step
    pygame.display.update()
pygame.quit()