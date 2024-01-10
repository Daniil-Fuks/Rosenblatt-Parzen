import math
import random
import matplotlib.pyplot as plt


# Функция для создания данных
def get_input_data():
    lst_x = []
    lst_y = []
    for i in range(20):
        num = random.uniform(-5, 5)
        lst_x.append(round(num, 5))
        lst_y.append(round(5 * math.sin(num), 5))
    return (lst_x, lst_y)


# Функция, выключающая ненужные точки
# x - выбранная точка, для которой определяются точки, входящие нужную область
# С - искомый параметр
def off_doter(x_dot, xi_dot, c):
    z = (x_dot - xi_dot) / c

    if z ** 2 <= 5:
        return 0.355 - 0.677 ** 2
    else:
        return 0


# Получаем предположительную точку
# x - выбранная точка
def result(lst_y, x_dot, c):
    up = 0
    down = 0
    for i in range(len(lst_y)):
        up += lst_y[i] * off_doter(x_dot, lst_y[i], c)

    for j in range(len(lst_y)):
        down += off_doter(x_dot, lst_y[j], c)

    return up / down


x = [-4.9056, 2.5524, -2.96923, -1.18132, -4.63106, 4.54592, -1.82194, -1.14801, 2.22342, 2.68198, 3.44386, 4.8055,
     -2.15474, -1.95093, 0.97942, 0.23584, 1.57265, 2.29331, 3.95314, 0.68536]

y = [4.90697, 2.77843, -0.85755, -4.62554, 4.98347, -4.93088, -4.84314, -4.55974, 3.97248, 2.21801, -1.48844, -4.97834,
     -4.17148, -4.64308, 4.15088, 1.16832, 4.99999, 3.75073, -3.62676, 3.16477]

res = result(y, 2.5, 0.6)

plt.scatter(x, y)
plt.axline(xy1=(1, res), xy2=(5, res))
plt.show()
print(res)
