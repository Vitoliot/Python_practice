import math
a = float(input('нач '))
b = float(input('кон '))
epsilon = float(input('точность '))
count = 0
answers = []


def method(x, epsilon, count):
    f = math.exp(-0.5*x) - math.pow(x - 0.8, 2) + 0.1
    dro = -0.5*math.exp(-0.5*x) - 2*x + 1.6
    count += 1
    x_next = x - f/dro
    if abs(x_next - x) <= epsilon:
        return [round(x_next, sum(1 for i in str(epsilon) if i == '0')), count]
    else:
        return method(x_next, epsilon, count)

while a < b:
    f = math.exp(-0.5*a) - math.pow(a - 0.8, 2) + 0.1
    drt = 0.25*math.exp(-0.5*a) - 2
    if f*drt > 0:
        answer = method(a, epsilon, count)
    else:
        answer = method(b, epsilon, count)
    flag = 0
    for i in range(0, len(answers), 1):
        if answer[0] == answers[i]:
            flag = 1
    if flag == 0:
        answers += answer
    a += epsilon
for i in range(0, len(answers) - 1, 2):
    print('ответ ', answers[i], '\n', 'кол-во итераций ', answers[i + 1], sep = "")