import random

from distance_calculation import get_list_distance

coords = []
list_points = []
way_now = {}
shortest_way = 0
shortest_way_coords = [[0, 0]]

for i in range(int(input())):
    # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    list_point = list(map(int, input().split(' ')))
    coords.append(list_point)

coords.insert(0, [0, 0])
# print(coords)

while len(coords) > 2:
    for i in range(len(coords)):
        if i != 0:
            list_points.append(coords[0])
            list_points.append(coords[i])
            distance = get_list_distance(list_points)
            distance = distance[0]
            way_now[i] = distance
            # print(distance)
            list_points.clear()
    d = [k for k, v in way_now.items() if v == min(way_now.values())]
    shortest_way += way_now[d[0]]
    shortest_way_coords.append(coords[d[0]])
    coords.insert(0, coords.pop(d[0]))
    del coords[1]
    way_now.clear()
    # print(coords)

distance = get_list_distance(coords)
distance = distance[0]
shortest_way += distance
shortest_way_coords.append(coords[-1])

print(shortest_way)
print(shortest_way_coords)
