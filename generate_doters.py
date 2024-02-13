import random
import math

import matplotlib.pyplot as plt

lst_x = []
lst_y = []
for i in range(100):
     num = random.uniform(-5, 5)
     lst_x.append(round(num, 5))
     lst_x.append(round(num, 5))
     lst_y.append(round(5 * math.sin(num), 5))
     lst_y.append(round(5 * math.sin(num), 5) - 40)
h = (max(lst_y) - min(lst_y) * 0.05) / 2
for num in range(len(lst_y)):
     lst_y[num] = round(lst_y[num] + random.uniform(-h, h), 4)

print(lst_x)
print(lst_y)

plt.scatter(lst_x, lst_y)
plt.show()