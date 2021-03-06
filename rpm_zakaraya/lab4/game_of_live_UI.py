import abc
import curses
import time
from game_of_live_logic import GameOfLife


class UI(abc.ABC):

    def __init__(self, life: GameOfLife) -> None:
        self.life = life

    @abc.abstractmethod
    def run(self) -> None: 
        pass


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.cols = life.cols
        self.rows = life.rows

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку """   
        screen.border()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток """
        for i in range(self.rows):
            for j in range(self.cols):
                if life.curr_generation[i][j] == 1:
                    screen.addstr(i+1, j+1, "A", curses.A_BLINK|curses.A_BOLD)
                else:
                    screen.addstr(i+1, j+1, "0")
        pass

    def run(self) -> None:
        screen = curses.initscr()
        curses.update_lines_cols()
        while life.is_changing and not life.is_max_generations_exceeded:
            curses.wrapper(self.draw_borders)
            self.draw_borders(screen)
            curses.wrapper(self.draw_grid)
            self.draw_grid(screen)
            life.step()
            screen.refresh()
            time.sleep(0.1)
        screen.getch()
        curses.endwin()


life = GameOfLife((int(input("Введите кол-во строк: ")), int(input("Введите кол-во столбцов: "))), max_generations = int(input("Введите кол-во поколений: ")))
ui = Console(life)
ui.run()