import os

import pygame
from pygame.locals import *
from sys import exit

# Инициализация Pygame
pygame.init()

# Определяем размеры окна
window_size = (600, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

# Начальные координаты и скорость ракетки
x, y = 250, 20  # Начальная позиция ракетки
move_x = 0

# Основной цикл игры
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Обработка нажатий клавиш
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -5  # Скорость движения влево
            elif event.key == K_RIGHT:
                move_x = 5   # Скорость движения вправо

        # Обработка отпускания клавиш
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                move_x = 0  # Остановка при отпускании
        
    # Обновление позиции ракетки
    x += move_x
    # Ограничение движения ракетки в пределах экрана
    if x < 10:
        x = 10
    elif x > 490:  # 600 - 100 (ширина ракетки) - 10 (граница)
        x = 490

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Отрисовка объектов
    pygame.draw.circle(screen, (0, 255, 0), [300, 300], 10)  # Мяч
    pygame.draw.rect(screen, (0, 0, 255), [10, 10, 580, 580], 3)  # Рамка
    pygame.draw.rect(screen, (255, 0, 0), [x, y, 100, 20])  # Ракетка

    # Обновление экрана
    pygame.display.update()
    clock.tick(60)  # Ограничение 60 FPS