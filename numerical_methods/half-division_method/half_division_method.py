import math


a = float(input("Введите начальную точку отрезка "))
b = float(input("Введите конечную точку отрезка "))
epsilon = float(input("Введите абсолютную погрешность "))
count = 0


def hd(a, b, epsilon, count):
    count += 1
    c = (a+b)/2
    F_a = math.exp(-0.5*a) - math.pow(a - 0.8, 2) + 0.1
    F_c = math.exp(-0.5*c) - math.pow(c - 0.8, 2) + 0.1
    if abs(F_c) < epsilon: return [round(c, sum(1 for i in str(epsilon) if i == '0')), count]
    else:
        if (F_a * F_c) < 0:
            b = c
        else:
            a = c
    return hd(a, b, epsilon, count)


out = hd(a, b, epsilon, count)
print("%3.3f" % out[0], out[1])