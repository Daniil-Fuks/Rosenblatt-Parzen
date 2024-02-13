import math
import random

import matplotlib.pyplot as plt


# Функция для создания данных
def get_input_data():
    lst_x = []
    lst_y = []
    for i in range(100):
        num = random.uniform(-5, 5)
        lst_x.append(round(num, 5))
        lst_y.append(round(5 * math.sin(num), 5))
    h = (max(lst_y) - min(lst_y) * 0.05) / 2
    for num in range(len(lst_y)):
        lst_y[num] = round(lst_y[num] + random.uniform(-h, h), 4)
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
def result(lst_y, lst_x, x_dot, c, c2=1):
    global where_f_bigger_zero
    # Если точка уже существует, функция ее выкидывает
    up = 0
    up2 = 0
    down = 0
    down2 = 0
    for i in range(len(lst_y)):
        xi_dot = lst_x[i]
        if xi_dot != x_dot and off_doter(x_dot, xi_dot, c) > 0:
            up += lst_y[i] * off_doter(x_dot, xi_dot, c) * off_doter(max(where_f_bigger_zero), y[i], c2)
            down += off_doter(x_dot, xi_dot, c) * off_doter(max(where_f_bigger_zero), y[i], c2)
            up2 += lst_y[i] * off_doter(x_dot, xi_dot, c) * off_doter(min(where_f_bigger_zero), y[i], c2)
            down2 += off_doter(x_dot, xi_dot, c) * off_doter(min(where_f_bigger_zero), y[i], c2)
        else:
            up += lst_y[i] * off_doter(x_dot, xi_dot, c)
            down += off_doter(x_dot, xi_dot, c)
            
    if down == 0:
        return 0
    return up / down


def result_beta(lst_y, lst_x, x_dot, c):
    up = 0
    down = 0
    for i in range(len(lst_y)):
        xi_dot = lst_x[i]
        if xi_dot != x_dot:
            up += lst_y[i] * off_doter(x_dot, xi_dot, c)
            down += off_doter(x_dot, xi_dot, c)
    if down == 0:
        return 0
    return up / down

# def result_for_x(lst_y, lst_x, y_dot, c2):
#     up = 0
#     down = 0
#     for i in range(len(lst_x)):
#         yi_dot = lst_y[i]
#         if yi_dot != y_dot:
#             up += lst_x[i] * off_doter(y_dot, yi_dot, c2)
#             down += off_doter(y_dot, yi_dot, c2)
#     if down == 0:
#         return
#     else:
#         return up / down


# Вычисление ошибки по полученной точке
def calc_mistake(lst_y, mb_y):
    up = 0
    down = 0
    for i in range(len(lst_y)):
        up += (lst_y[i] - mb_y[i]) ** 2
        down += 1
    return (up / down) ** 0.5


x = [1.58931, 3.80218, -1.70577, 3.98532, 2.66689, -2.06356, 4.43763, 3.06586, -4.59412, 4.22462, -3.13256, -2.86898,
     3.94885, 3.34973, 0.72399, 3.38369, -4.05588, -1.84873, 2.499, -1.42878, -0.74418, 4.82556, -2.77553, -0.0212,
     -1.37357, -0.11358, 3.38157, -2.60577, -2.11877, 1.51264, -4.27645, -3.99351, -3.9991, -3.74123, 4.34228, -1.97436,
     -2.05312, 0.73588, 2.1418, -1.70676, -3.59102, -0.77821, -4.61795, 4.84027, -3.49024, 0.62837, -2.08385, 3.69567,
     4.39704, 3.24175, 3.26905, -3.41692, -2.80505, 1.11656, -4.54709, -2.06286, 3.90301, 2.56825, -4.94292, -3.34979,
     3.53188, 0.70476, 4.81959, -0.03945, -2.45723, 3.88808, 4.89665, -0.27517, -2.41544, 3.65152, 3.7528, 3.8956,
     2.64622,
     4.91723, 3.79506, -0.56377, 3.77543, 0.3576, -3.17768, -3.87524, 4.0215, 0.90488, -4.97106, 0.43076, 2.1804,
     -0.61497,
     2.31891, 2.17971, -4.27111, -4.0463, 2.26045, -1.95803, -3.16014, -0.04545, -1.26152, 1.61507, -0.67688, -3.69236,
     1.20876, -0.72016]

y = [2.8791, -0.6158, -5.0619, -4.9169, 3.2302, -2.5018, -4.927, -1.982, 4.6586, -3.5874, -1.9395, -0.4315, -4.9503,
     -2.7124, 5.9269, 0.2217, 3.9426, -2.7968, 4.9932, -6.9263, -3.9007, -3.8525, -1.6593, -0.1945, -5.4385, -1.9051,
     -3.6352, -1.4537, -2.1656, 2.9358, 3.6786, 4.8728, 3.6655, 2.6252, -7.2039, -4.1752, -6.7125, 1.2483, 2.9649,
     -2.6742, -0.196, -3.0002, 2.9884, -6.6473, 4.3028, 3.9817, -4.7957, -3.0079, -3.7059, -2.8731, -0.5725, 2.7265,
     -1.6283, 6.2934, 2.7384, -4.3472, -1.37, 2.6677, 6.6226, -0.9904, -4.0852, 1.5451, -7.2994, -1.2119, -5.195,
     -3.2957, -3.0708, -2.3897, -4.8649, -4.6628, -0.3138, -1.545, 4.4923, -6.3128, -4.9221, -4.043, -3.1615, 1.7956,
     0.6264, 3.1248, -4.9833, 4.5426, 7.3569, 2.3972, 4.8308, -0.3735, 5.9866, 3.3934, 5.6017, 2.3227, 5.9764, -3.2256,
     0.8924, -0.8589, -4.8207, 3.2701, -3.8122, 0.6057, 6.1021, -3.8536]


mist_e = []

mb_y = []
mb_x = []

c_lst = []
c2_lst = []

C = 0.17
C2 = 5.001

# Нахождение оптимального параметра C

# c = 0
# while c < 5:
#     c += 0.01
#     for i in range(len(x)):
#         mb_y.append(result_beta(y, x, x[i], c))
#     c_lst.append(c)
#     # Получение предположительных точек для каждого Х с одним параметром С.
#     # Вычисление ошибки для каждой точки
#
#     e = calc_mistake(y, mb_y)
#     mist_e.append(e)
#     mb_y = []
# optimal_c = c_lst[mist_e.index(min(mist_e))]
# print(optimal_c)


# c2 = 0
# mist_e_x = []
# while c2 < 5:
#     c2 += 0.01
#     for i in range(len(y)):
#         mb_x.append((result_beta(y, x, y[i], c2)))
#     c2_lst.append(c2)
#     e = calc_mistake(y, mb_x)
#     mist_e_x.append(e)
#     mb_x = []
# optimal_c2 = c2_lst[mist_e_x.index(min(mist_e_x))]
# print(optimal_c2)


# Определение точек, при которых фи больше нуля
where_f_bigger_zero = []
for i in range(len(y)):
    for j in range(len(y)):
        x_dot = x[i]
        xi_dot = x[j]
        for yi in y:
            if yi * off_doter(x_dot, xi_dot, C) > 0 and yi not in where_f_bigger_zero:
                where_f_bigger_zero.append(yi)

i = -8
mb_y = []
while i < 9:
    print(result(y, x, x[i], C, C2))
    print(x[i])
    mb_y.append(result(y, x, x[i], C, C2))
    mb_x.append(i)
    i += 0.1

plt.scatter(x, y)
plt.plot(mb_x, mb_y, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# print(len(x2), len(y2))
