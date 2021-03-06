import math
a = float(input('нач '))
b = float(input('кон '))
epsilon = float(input('точность '))
count = 0
answers = []


def func(x):
    return math.exp(-x) + x - 2


def der_one(x):
    return 1 - math.exp(-x)


def der_two(x):
    return math.exp(-x)


def method(x, epsilon, count):
    f = func(x)
    dro = der_one(x)
    count += True
    x_next = x - f/dro
    if abs(x_next - x) <= epsilon:
        return [round(x_next, sum(1 for i in str(epsilon) if i == '0')), count]
    else:
        return method(x_next, epsilon, count)

while a < b:
    f = func(a)
    drt = der_two(a)
    if f*drt > 0:
        answer = method(a, epsilon, count)
    else:
        answer = method(b, epsilon, count)
    flag = False
    for i in range(0, len(answers), 1):
        if answer[0] == answers[i]:
            flag = True
    if flag == False:
        answers += answer
    a += epsilon
for i in range(0, len(answers) - 1, 2):
    print('ответ ', answers[i], '\n', 'кол-во итераций ', answers[i + 1], sep = "")