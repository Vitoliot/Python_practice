import abc
import pygame
from game_of_live_logic import GameOfLife
from pygame.locals import *


class UI(abc.ABC):

    def __init__(self, life: GameOfLife) -> None:
        self.life = life

    @abc.abstractmethod
    def run(self) -> None: 
        pass


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int=10, speed: int=10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.rows, self.cols = life.rows, life.cols
        self.screen_size = self.rows * cell_size, self.cols * cell_size
        self.screen = pygame.display.set_mode(self.screen_size)
    
    def draw_lines(self) -> None:
        # @see: http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.cols * self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.rows * self.cell_size))
        for y in range(0, self.rows * self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.cols * self.cell_size, y))

    def draw_grid(self) -> None:
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if life.curr_generation[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('red'), (i * self.cell_size + 1, j * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (i * self.cell_size + 1, j * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        paused = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(num_buttons = 3)[0] == 1:
                        coords = pygame.mouse.get_pos()
                        print(coords[0]//self.cell_size, coords[1]//self.cell_size)
                        if life.curr_generation[coords[0]//self.cell_size][coords[1]//self.cell_size] == 1:
                            life.curr_generation[coords[0]//self.cell_size][coords[1]//self.cell_size] = 0
                        else: life.curr_generation[coords[0]//self.cell_size][coords[1]//self.cell_size] = 1
                    if pygame.mouse.get_pressed(num_buttons = 3)[2] == 1:
                        print(not paused)
                        paused = not paused
            if not paused:
                self.draw_lines()
                self.draw_grid()
                life.step()
                life.save('rpm_zakaraya\lab4\gg_his', False) #путь надо изменить
                pygame.display.flip()
                clock.tick(self.speed)
                if life.is_changing == False or life.is_max_generations_exceeded:
                    break
            if paused:
                self.draw_lines()
                self.draw_grid()
                pygame.display.flip()
                clock.tick(self.speed)
        life.save('rpm_zakaraya\lab4\gg') # путь надо изменить
        pygame.quit()


life = GameOfLife((int(input("Введите кол-во строк: ")), int(input("Введите кол-во столбцов: "))), randomize = int(input("Задать начальные значения? 1 - да, 0 - нет ")), max_generations = int(input("Введите кол-во поколений: ")))
gui = GUI(life, int(input("Введите размер клетки: ")))
gui.run()