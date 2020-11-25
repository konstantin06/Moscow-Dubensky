import pygame


def draw():
    screen.fill((0, 0, 0))
    center1, center2 = w * n, w * n
    color = 'red'
    for i in range(1, n + 1):
        pygame.draw.circle(screen, color, (center1, center2), w * i, w)
        if color == 'red':
            color = 'green'
        elif color == 'green':
            color = 'blue'
        elif color == 'blue':
            color = 'red'


if __name__ == '__main__':
    try:
        w, n = map(int, input().split())

        # инициализация Pygame:
        pygame.init()

        pygame.display.set_caption('Шахматная клетка')
        # размеры окна:
        size = width, height = w * n * 2, w * n * 2
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        draw()
        # ...
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()

    except ValueError:
        print('Неправильный формат ввода')
        pygame.quit()

