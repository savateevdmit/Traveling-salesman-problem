# с возвратом в начальные координаты

import time
import itertools
from copy import copy

import matplotlib.pyplot as plt
from distance_calculation import get_list_distance

fig, ax = plt.subplots()

route = 0
list_points = []
town = 1
coords = []
dict_coords = {}
number_towns_list = []
shortest_path = 100000

for i in range(int(input())):
    list_point = list(map(int, input().split(' ')))
    coords.append(list_point)
coords.insert(0, (0, 0))

t1 = time.time()
for x, y in coords:
    dict_coords[town] = (x, y)
    number_towns_list.append(town)
    if x == 0 and y == 0:
        ax.add_patch(plt.Circle((x, y), 0.3, facecolor='#FF0000', alpha=1))
    else:
        ax.add_patch(plt.Circle((x, y), 0.3, facecolor='#9ebcda', alpha=1))

    plt.text(x - 0.12, y - 0.12, f'{town}')
    town += 1

for i in itertools.permutations(number_towns_list):
    for j in i:
        list_points.append(dict_coords[int(j)])
    # list_points.insert(0, (0, 0))
    # print(list_points)
    distance = sum(get_list_distance(list_points))
    print(get_list_distance(list_points)[:-1])
    if distance < shortest_path:
        shortest_path = distance
        route = copy(list_points)
    list_points.clear()

t2 = time.time()
print(f'Самый короткий путь: {shortest_path}, маршрут: {route}')
print(f'Потраченное время: {t2 - t1}')

for i in range(len(route)):
    if len(route) > i + 1:
        plt.plot((route[i][0], route[i + 1][0]), (route[i][1], route[i + 1][1]), alpha=0.6)
    else:
        plt.plot((route[-1][0], route[0][0]), (route[-1][1], route[0][1]), alpha=0.6)
# Use adjustable='box-forced' to make the plot area square-shaped as well.
ax.set_aspect('equal', adjustable='datalim')
ax.set_xbound(3, 4)

ax.plot()  # Causes an autoscale update.
plt.show()

'''
5
4 9
6 2
5 7
6 1
6 9

7
1 0
1 1
1 2
1 3
1 4
1 5
1 6
'''