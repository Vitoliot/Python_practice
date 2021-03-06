import pathlib
import math
import copy
import random
from itertools import chain
from pprint import pprint as pp

def group(values, n):
    n_groups = math.ceil(len(values)/n) #считаем кол-во строк 
    values_many = [["."] * n for i in range(n_groups)] #генератор двумерного списка для записи сгрупированных значений
    a = 0 # индекс для списка из вход. 
    for i in range(n_groups):
        for j in range(n):
                values_many[i][j] = values[a]
                a = a + 1
    return values_many

def create_grid(puzzle: str):
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid

def read_sudoku(path):
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)

def display(grid) -> None:
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()

def get_row(grid, pos):
    return grid[pos[0]]

def get_col(grid, pos):
    n_sudoku = math.ceil(sum(map(len, grid))/len(grid))#рассчёт кол-во строк и столбцов(судоку квадратная, они равны)
    values_col = [["."]  for i in range(n_sudoku)]#создание одномерного списка для записи значений
    for i in range(n_sudoku):
        values_col[i] = grid[i][pos[1]] 
    return values_col

def get_block(grid, pos):
    n_sudoku = math.ceil(sum(map(len, grid))/len(grid))#рассчёт кол-во строк и столбцов(судоку квадратная, они равны)
    values_block =  [["."] * (n_sudoku) for i in range(n_sudoku)] #список с квадратами
    n_square = 2 #минимальный размер квадрата
    count_square = 0 #счётчик для прехода на след. строку квадрата
    square_i = 0 # счётчик для переходу к другому квадрату
    square_j = 0 # счётчик для перемещения по квадрату
    cof_i = 0 # метка для цикла 
    cof_j = 0 # метка для цикла
    flag_square = 0 # флаг 
    is_square = 0 #метка, указывающая на квадрат с позицией

    while n_square != (n_sudoku):
      if ((n_sudoku) % n_square == 0): break
      n_square = n_square + 1
    # поиск квадрата минимального размера (кроме 1)

    for i in range(n_sudoku):
      for j in range(n_sudoku):
        values_block[square_i][square_j] = grid[i][j]
        count_square = count_square + 1 
        square_j = square_j + 1 
        if i == pos[0] and j == pos[1]: #проверка координат на соответствие позиции
           is_square = square_i
           flag_square = 1
        if (count_square % n_square) == 0:
          count_square = 0
          square_i = square_i + 1
          square_j = cof_j
          #переход к следующему квадрату
      cof_j = cof_j + n_square #после одной итерации i заполнены первые строки нескольких квадратов. Для того, чтобы не допустить накладывания значений делаем сдвиг на длину квадрата.
      if ( i + 1 ) % n_square == 0: #если true, то квадраты заполнены и работу с ними мы прекращаем.
        cof_i = cof_i + n_square
        cof_j = 0
        if flag_square != 0 : break #прекращаем работу цикла, если условие выполнено
      square_i = cof_i
      square_j = cof_j
    return values_block[is_square]

def find_empty_positions(grid):
    n_sudoku = math.ceil(sum(map(len, grid))/len(grid))
    for i in range(n_sudoku):
      for j in range(n_sudoku):
        if grid[i][j] == '.':
          return [i, j]
    return False


def find_possible_values(grid, pos):
  values = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
  row = get_row( grid, pos )
  col = get_col( grid, pos )
  block = get_block( grid, pos)
  values -= set(row)
  values -= set(col)
  values -= set(block)
  return list(values)


def solve(grid):
  pos_now = find_empty_positions(grid)
  if pos_now != False:
      all_possible = find_possible_values(grid, pos_now)
      for possible in all_possible:
          new_grid = copy.deepcopy(grid)
          new_grid[pos_now[0]][pos_now[1]] = possible
          solution = solve(new_grid)
          if solution is not None:
              return solution
      return None
  return grid


def check_solution(solution) -> bool:
    for i in range(9):
        for j in range(9):
            values = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            if values != set(get_col(solution, [i,j])): return False
            if values != set(get_row(solution, [i,j])): return False
            if values != set(get_block(solution, [i,j])): return False
    return True

def gen_sudoku(N) -> list:
    new_sudoku = [[(str(math.floor((i*3 + i/3 + j) % (9) + 1))) for j in range(9)] for i in range(9)]
    display(new_sudoku)
    field = [["."] * 9 for i in range(9)]
    value = [i for i in range(9)]
    for gen in range(25):
      new_sudoku = transponing(new_sudoku)
      new_sudoku = swap_row_small(new_sudoku)
      new_sudoku = swap_col_small(new_sudoku)
    if (N >= 81): return new_sudoku
    else:
      a = 0
      while a !=(81-N):
        i_point = random.choice(value)
        j_point = random.choice(value)
        if field[i_point][j_point] == '.':
          new_sudoku[i_point][j_point] = '.'
          field[i_point][j_point] = 1
          a +=1
    return new_sudoku

def transponing(grid):
    res_grid = []
    for j in range(9):
        tran_grid = []
        for i in range(9):
            tran_grid += [grid[i][j]]
        res_grid += [tran_grid]
    return res_grid

def swap_row_small(grid):
  value = [i for i in range(9)]
  i = random.choice(value)
  if i < 3:
    value = [v for v in range(3)]
    value.remove(i)
    i_i = random.choice(value)
  if (i < 6) and (i > 2):
    value = [v for v in range(3, 6)]
    value.remove(i)
    i_i = random.choice(value)
  if i >= 6:
    value = [v for v in range(6, 9)]
    value.remove(i)
    i_i = random.choice(value)

  for a in range(9):
    swap_val = grid[i][a]
    grid[i][a] = grid[i_i][a]
    grid[i_i][a] = swap_val
  return grid

def swap_col_small(grid):
  value = [i for i in range(9)]
  j = random.choice(value)
  if j < 3:
    value = [v for v in range(3)]
    value.remove(j)
    j_j = random.choice(value)
  if (j < 6) and (j > 2):
    value = [v for v in range(3, 6)]
    value.remove(j)
    j_j = random.choice(value)
  if j >= 6:
    value = [v for v in range(6, 9)]
    value.remove(j)
    j_j = random.choice(value)
  for a in range(9):
    swap_val = grid[a][j]
    grid[a][j] = grid[a][j_j]
    grid[a][j_j] = swap_val
  return grid

grid = read_sudoku('rpm_zakaraya\lab2\puzzle1.txt')
display(grid)
solution = solve(grid)
display(solution)
print(check_solution(solution))
new = (gen_sudoku(2))
print(sum(1 for row in new for e in row if e == '.'))
display(new)
solution = solve(new)
display(solution)
print(check_solution(solution))
