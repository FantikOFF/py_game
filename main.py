import pygame

# инициализируем библиотеку Pygame
pygame.init()

# определяем размеры окна
window_size = (300, 300)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
