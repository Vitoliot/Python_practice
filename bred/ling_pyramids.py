import random
from data import words
actions = ['обобщить', 'конкретизировать', 'привести аналогию']
results = []


def begin():
    word = random.choice(words)
    abundance = 0
    past_action = 'ы'
    print('Ваше слово', word)
    results.append(word)
    while(True):
        random_action = random.choice(actions)
        if random_action == past_action: abundance += 1
        if abundance > 1:
            while random_action == past_action:
                random_action = random.choice(actions)
            abundance = 0
        print('Вам надо', random_action, end = '\n')
        in_data = input()
        if in_data == 'завершить': break
        elif in_data == 'текущий список слов': 
            print(results)
            print('Вам надо', random.choice(actions), end = '')
            in_data = input()
        results.append(in_data)
        past_action = random_action
    print(results)

begin()