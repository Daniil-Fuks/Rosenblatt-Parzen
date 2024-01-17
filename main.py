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
# x_dot - выбранная точка, для которой определяются точки, входящие нужную область
# С - искомый параметр
def off_doter(x_dot, xi_dot, c):
    if ((x_dot - xi_dot) / c) ** 2 <= 5:
        return 0.355 - 0.677 ** 2
    else:
        return 0


# Получаем предположительную точку
# x - выбранная точка
def result(lst_y, lst_x, x_dot, c):
    # Если точка уже существует, функция ее выкидывает
    up = 0
    down = 0
    for i in range(len(lst_y)):
        xi_dot = lst_x[i]
        if xi_dot != x_dot:
            up += lst_y[i] * off_doter(x_dot, xi_dot, c)
            down += off_doter(x_dot, xi_dot, c)
        else:
            continue
    if down == 0:
        return 0
    else:
        return up / down


# Вычисление ошибки по полученной точке
def calc_mistake(lst_y, mb_y):
    up = 0
    down = 0
    for i in range(len(lst_y)):
        up += (lst_y[i] - mb_y) ** 2
        down += 1
    return (up / down) ** 0.5


x = [-4.9056, 2.5524, -2.96923, -1.18132, -4.63106, 4.54592, -1.82194, -1.14801, 2.22342, 2.68198, 3.44386, 4.8055,
     -2.15474, -1.95093, 0.97942, 0.23584, 1.57265, 2.29331, 3.95314, 0.68536]

y = [4.90697, 2.77843, -0.85755, -4.62554, 4.98347, -4.93088, -4.84314, -4.55974, 3.97248, 2.21801, -1.48844, -4.97834,
     -4.17148, -4.64308, 4.15088, 1.16832, 4.99999, 3.75073, -3.62676, 3.16477]






c = 0
mistake = []
doters = []
c_lst = []
while c < 5:
    c += 0.001
    x_dot = result(y, x, 2.5, c)
    if x_dot not in doters:
        mist = calc_mistake(y, x_dot)
        print(f'{c}: {mist}')
        mistake.append(mist)
        doters.append(x_dot)
        c_lst.append(c)
print(doters)
print(c_lst)
# print(mistake.index(max(mistake)))
# print(c_lst[mistake.index(max(mistake))])
# print(result(y, x, 2.5, 0.415))
plt.plot(c_lst, mistake)
plt.show()

# res = result(y, 2.5, 6)
# print(res)

# plt.scatter(x, y)
# plt.axline(xy1=(1, res), xy2=(5, res))
# plt.show()
# print(res)
