import random
import pathlib
import copy


class GameOfLife:

    def __init__(self, size: tuple[int, int] = (10, 10), randomize: bool=True, max_generations: int = 30) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool=False):
        if randomize:
            return [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(0, self.rows)]
        else:
            return [[0 for _ in range(0, self.cols)]  for _ in range(0, self.rows)]
    
    def get_next_generation(self, grid):
        for i in range(self.rows):
            for j in range(self.cols):
                neighbours = self.get_neighbours([i, j])
                count = sum(1 for c in range(0, len(neighbours) - 1, 2) if self.prev_generation[neighbours[c]][neighbours[c + 1]] == 1)
                if count == 3:
                    if self.prev_generation[i][j] == 0: grid[i][j] = 1
                    continue
                elif count == 2:
                    continue
                else: 
                    grid[i][j] = 0
        return grid

    def get_neighbours(self, cell: list):
        neighbours = ()
        for i in range(cell[0] - 1, cell[0] + 2):
            if i < 0 or i > self.rows - 1: continue
            for j in range(cell[1] - 1, cell[1] + 2):
                if j < 0 or j > self.cols - 1: continue
                if [i, j] != cell:
                    neighbours += ((i, j))
        return neighbours

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        # """
        self.prev_generation = copy.deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation(self.curr_generation)
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.generations > self.max_generations:
            return True
        else: return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation != self.prev_generation:
            return True
        else: return False
    
    @staticmethod
    def from_file(filename) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        filename = pathlib.Path(filename)
        with filename.open() as f:
            load_grid = f.read()
        load_grid = load_grid.split('\n')
        load_grid = [list(i) for i in load_grid]
        for i in range(len(load_grid)):
            for j in range(len(load_grid[i])):
                load_grid[i][j] = int(load_grid[i][j])
        return load_grid
    
    def save(self, filename, replace = True) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        filename = pathlib.Path(filename)
        save_grid = str(self.curr_generation)
        save_grid = save_grid.replace('[', '').replace(']', '\n').replace(',', '').replace(' ', '')
        if replace:
            with filename.open('w') as f:
                f.write(save_grid)
        else:
            with filename.open('a') as f:
                f.write(save_grid)


# life = GameOfLife((10, 10), max_generations = 20)
# life.curr_generation = life.from_file('rpm_zakaraya\lab4\gg_in')
# while life.is_changing and not life.is_max_generations_exceeded:
#     life.step()
#     life.save('rpm_zakaraya\lab4\gg')