import random
import pygame
from pygame.locals import *


def get_neighbours(cell):
    """
    Вернуть список соседних клеток для клетки `cell`.
    Соседними считаются клетки по горизонтали, вертикали и диагоналям,
    то есть, во всех направлениях.
    Parameters
    ----------
    cell : Cell
        Клетка, для которой необходимо получить список соседей. Клетка
        представлена кортежем, содержащим ее координаты на игровом поле.
    Returns
    ----------
    out : Cells
        Список соседних клеток.
    """
    neighbours = ()
    for i in range(cell[0] - 1, cell[0] + 2):
        if i < 0 or i > 15: continue
        for j in range(cell[1] - 1, cell[1] + 2):
            if j < 0 or j > 11: continue
            if [i, j] != cell:
                neighbours += ((i, j))
    return neighbours
    
    
class GameOfLife:

    def __init__(self, width: int=640, height: int=480, cell_size: int=10, speed: int=10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed
        self.Grid = self.create_grid(True)

    def draw_lines(self) -> None:
        # @see: http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))
    
    def create_grid(self, randomize: bool=False):
        if randomize:
            return [[random.choice([0, 1]) for _ in range(0, self.cell_height)] for _ in range(0, self.cell_width)]
        else:
            return [[0 for _ in range(0, self.cell_height)]  for _ in range(0, self.cell_width)]

    def draw_grid(self) -> None:
        for i in range(0, self.cell_width):
            for j in range(0, self.cell_height):
                if self.Grid[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))

    def get_next_generation(self):
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        for i in range(self.cell_width):
            for j in range(self.cell_height):
                neighbours = get_neighbours([i, j])
                count = sum(1 for c in range(0, len(neighbours) - 1, 2) if self.Grid[neighbours[c]][neighbours[c + 1]] == 1)
                if count == 3:
                    if self.Grid[i][j] == 0: self.Grid[i][j] = 1
                    continue
                if count == 2: continue
                self.Grid[i][j] = 0
        return self.Grid

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()
            self.draw_grid()
            self.Grid = self.get_next_generation()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    Grid = game.create_grid(True)
    game.run()