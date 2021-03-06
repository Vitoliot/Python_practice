import math
a = float(input("Начало интервала: "))
b = float(input("Конец интервала: "))
epsilon = float(input("Погрешность: "))
count = 0


def method(x, epsilon, count):
    count += 1
    f_n = math.exp(-0.5*x) - math.pow(x - 0.8, 2) + 0.1
    dro = -0.5*math.exp(-0.5*x) - 2*x + 1.6
    x_next = x - f_n/dro
    if abs(x_next - x) <= epsilon:
        return [round(x_next, sum(1 for i in str(epsilon) if i == '0')), count]
    else:
        return method(x_next, epsilon, count)


f = math.exp(-0.5*a) - math.pow(a - 0.8, 2) + 0.1
drt = 0.25*math.exp(-0.5*a) - 2
if f*drt > 0:
    answer = method(a, epsilon, count)
else:
    answer = method(b, epsilon, count)
for i in range(0, len(answer), 1):
    print(answer[i], end = ' ')