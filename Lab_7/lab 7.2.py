import pygame

pygame.init()
screen = pygame.display.set_mode((995, 535))  # Терезе өлшемі

isDone = True
index = 0
sounds = [
    r"C:\Users\user\Desktop\PP2\Lab_7\Bernward Koch - Cafe Noir.mp3",
    r"C:\Users\user\Desktop\PP2\Lab_7\Danny Wright - Do You Live Do You Love.mp3",
    r"C:\Users\user\Desktop\PP2\Lab_7\Stan Whitmire - Turn Your Eyes Upon Jesus.mp3",
]

images = [
    r"C:\Users\user\Desktop\PP2\Lab_7\1.jpeg",
    r"C:\Users\user\Desktop\PP2\Lab_7\2.jpeg",
    r"C:\Users\user\Desktop\PP2\Lab_7\3.jpeg",
]

color = (255, 255, 255)

isPaused = False
isPlayed = True

def load_and_play_music(index):
    pygame.mixer.music.load(sounds[index])
    pygame.mixer.music.play(2)
    
    image = pygame.image.load(images[index])  # Суретті жүктеу
    image = pygame.transform.scale(image, (995, 535))  # Суретті экран өлшеміне бейімдеу
    
    screen.blit(image, (0, 0))
    pygame.display.update()

load_and_play_music(index)

while isDone:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isDone = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            index = (index + 1) % len(sounds)
            isPaused = False
            isPlayed = True
            load_and_play_music(index)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            index = (index - 1) % len(sounds)
            isPaused = False
            isPlayed = True
            load_and_play_music(index)

        if event.type == pygame.KEYDOWN and isPlayed:
            if isPaused:
                pygame.mixer.music.unpause()
                isPaused = not isPaused
            else:
                load_and_play_music(index)
            isPlayed = not isPlayed

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not isPlayed:
            pygame.mixer.music.pause()
            isPlayed = not isPlayed
            isPaused = not isPaused

    pygame.display.flip()

pygame.quit()
