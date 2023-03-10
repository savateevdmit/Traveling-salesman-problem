import itertools
import random
import time
from copy import copy

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from python_tsp.heuristics import solve_tsp_local_search
from scipy.spatial import distance_matrix

from distance_calculation import get_list_distance

POLN = []
GHAD = []
VETV = []
MONTE = []
GA = []


def gg(COORDS):
    # if [0, 0] in COORDS:
    #     COORDS.remove([0, 0])
        # coords_view.remove('(0;0)')
    list_points = []
    way_now = {}
    shortest_way = 0
    town = 0
    shortest_way_coords = [[0, 0]]
    shortest_way_coords2 = []
    mtx = []
    vip = []
    result = []
    coords2 = []

    for i in COORDS:
        # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
        list_point = i
        coords2.append(list_point[:2])
        if len(list_point) == 3:
            vip.append(list_point[:2])
        else:
            mtx.append(list_point)

    if len(vip) != 0:
        vip.insert(0, [0, 0])
    else:
        mtx.insert(0, [0, 0])
    coords2.insert(0, (0, 0))

    # del coords[0]
    if len(vip) != 0:
        while len(vip) > 2:
            for i in range(len(vip)):
                if i != 0:
                    list_points.append(vip[0])
                    list_points.append(vip[i])
                    distance = get_list_distance(list_points)
                    distance = distance[0]
                    way_now[i] = distance
                    # print(distance)
                    list_points.clear()
            d = [k for k, v in way_now.items() if v == min(way_now.values())]
            shortest_way += way_now[d[0]]
            shortest_way_coords.append(vip[d[0]])
            vip.insert(0, vip.pop(d[0]))
            del vip[1]
            way_now.clear()
            # print(coords)

        distance = get_list_distance(vip)
        distance = distance[0]
        shortest_way += distance
        shortest_way_coords.append(vip[-1])
        # shortest_way_coords = shortest_way_coords.reverse()
        for i in shortest_way_coords:
            result.append(i)

    shortest_way = 0
    distance = 0
    way_now = {}
    # print('..........')

    # print(coords)
    mtx.insert(0, shortest_way_coords[-1])

    while len(mtx) > 2:
        for i in range(len(mtx)):
            if i != 0:
                list_points.append(mtx[0])
                list_points.append(mtx[i])
                distance = get_list_distance(list_points)
                distance = distance[0]
                way_now[i] = distance
                # print(distance)
                list_points.clear()
        d = [k for k, v in way_now.items() if v == min(way_now.values())]
        shortest_way += way_now[d[0]]
        shortest_way_coords2.append(mtx[d[0]])
        mtx.insert(0, mtx.pop(d[0]))
        del mtx[1]
        way_now.clear()
        # print(coords)

    distance = get_list_distance(mtx)
    distance = distance[0]
    shortest_way += distance
    shortest_way_coords2.append(mtx[-1])
    # shortest_way_coords = shortest_way_coords[:]

    for i in shortest_way_coords2:
        result.append(i)
    GHAD.append(sum(get_list_distance(result)))
    print(f'{sum(get_list_distance(result))} ???????????? ????????????????')
    print()


    # if [0, 0] in COORDS:
    #     COORDS.remove([0, 0])
        # coords_view.remove('(0;0)')
    # print(coords_view)
    #
    #
    # if len(COORDS) < 7:
    #     route = 0
    #     list_points = []
    #     town = 0
    #     dict_coords = {}
    #     number_towns_list = []
    #     shortest_path = 100000
    #     mtx = []
    #     vip = []
    #     coords2 = []
    #
    #     for i in COORDS:
    #         # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    #         list_point = i
    #         coords2.append(list_point[:2])
    #         if len(list_point) == 3:
    #             vip.append(list_point[:2])
    #         else:
    #             mtx.append(list_point)
    #
    #     if len(vip) != 0:
    #         vip.insert(0, [0, 0])
    #     # coords2.insert(0, (0, 0))
    #
    #     coords2.insert(0, [0, 0])
    #     # del coords[0]
    #     for i in coords2:
    #         if i not in vip:
    #             dict_coords[town] = (i[0], i[1])
    #             number_towns_list.append(town)
    #             town += 1
    #         else:
    #             dict_coords[town] = (i[0], i[1])
    #             number_towns_list.append(town)
    #             town += 1
    #
    #     for i in itertools.permutations(number_towns_list):
    #         for j in i:
    #             if list(dict_coords[int(j)]) not in vip:
    #                 list_points.append(dict_coords[int(j)])
    #         if len(vip) > 0:
    #             for i in vip:
    #                 list_points.insert(0, (i[0], i[1]))
    #         else:
    #             list_points.insert(0, (0, 0))
    #         # print(list_points)
    #         distance = sum(get_list_distance(list_points))
    #         # print(get_list_distance(list_points)[:-1])
    #         if distance < shortest_path:
    #             shortest_path = distance
    #             route = copy(list_points)
    #         list_points.clear()
    #
    #     b = route[route[1:].index((0, 0)) + 1:]
    #
    #     del route[route[1:].index((0, 0)) + 1:]
    #     route.reverse()
    #     b.reverse()
    #     for i in b:
    #         route.append(i)
    #
    #     route.insert(0, route.pop())
    #
    #     POLN.append(shortest_path)
    #     print(f'{shortest_path} ???????????? ??????????????')
    #     print()
    #
    #
    # def Min(lst, myindex):
    #     return min(x for idx, x in enumerate(lst) if idx != myindex)
    #
    # # ?????????????? ???????????????? ???????????? ???????????? ?? ????????????????
    # def Delete(matrix, index1, index2):
    #     del matrix[index1]
    #     for i in matrix:
    #         del i[index2]
    #     return matrix
    #
    #
    # H = 0
    # n = len(COORDS)
    # PathLenght = 0
    # Str = []
    # Stb = []
    # res = []
    # result = []
    # StartMatrix = []
    # mtx = []
    # lll = []
    # coords2 = []
    # vip = []
    # first = []
    # last_coords = []
    #
    # for i in COORDS:
    #     # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    #     # list_point = list(map(int, input().split(' ')))
    #     if len(i) == 3:
    #         vip.append(i[:2])
    #     else:
    #         mtx.append(i)
    #
    # if len(vip) != 0:
    #     vip.insert(0, [0, 0])
    # # else:
    #
    # df_vip = pd.DataFrame(vip)
    # m_vip = pd.DataFrame(distance_matrix(df_vip.values, df_vip.values))
    #
    # # print(m)
    # # print()
    # # print(mtx)
    #
    # print()
    # matrix_vip = m_vip.values.tolist()
    #
    # if len(matrix_vip) > 0:
    #     for i in range(len(matrix_vip)):
    #         matrix_vip[i][i] = float('inf')
    #         for g in range(len(matrix_vip[i])):
    #             matrix_vip[i][g] = round(matrix_vip[i][g], 3)
    #     # print(matrix_vip)
    #     # print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix_vip]))
    #     # ???????????????????????????? ?????????????? ?????? ???????????????????? ????????????????
    #     for i in range(len(matrix_vip)):
    #         Str.append(i)
    #         Stb.append(i)
    #
    #     # ?????????????????? ?????????????????????? ??????????????
    #     for i in range(len(matrix_vip)):
    #         StartMatrix.append(matrix_vip[i].copy())
    #
    #     while True:
    #         # ????????????????????
    #         # --------------------------------------
    #         # ???????????????? ?????????????????????? ?????????????? ?? ??????????????
    #         for i in range(len(matrix_vip)):
    #             min_row = min(matrix_vip[i])
    #             min_column = min(row[i] for row in matrix_vip)
    #             H += min_row + min_column
    #             for j in range(len(matrix_vip)):
    #                 matrix_vip[i][j] -= min_row
    #                 matrix_vip[j][i] -= min_column
    #         # --------------------------------------
    #         # ?????????????????? ?????????????? ???????????? ?? ???????? ?????????????? ???????????? ?? ???????????????????????? ??????????????
    #         # --------------------------------------
    #         NullMax = 0
    #         index1 = 0
    #         index2 = 0
    #         tmp = 0
    #         for i in range(len(matrix_vip)):
    #             for j in range(len(matrix_vip)):
    #                 if matrix_vip[i][j] == 0:
    #                     tmp = Min(matrix_vip[i], j) + Min((row[j] for row in matrix_vip), i)
    #                     if tmp >= NullMax:
    #                         NullMax = tmp
    #                         index1 = i
    #                         index2 = j
    #                         lll.append((index1, index2))
    #         # --------------------------------------
    #
    #         # ?????????????? ???????????? ?????? ????????, ???????????????????? ?????? ?? res ?? ?????????????? ?????? ????????????????
    #         res.append(Str[index1] + 1)
    #         res.append(Stb[index2] + 1)
    #
    #         oldIndex1 = Str[index1]
    #         oldIndex2 = Stb[index2]
    #         if oldIndex2 in Str and oldIndex1 in Stb:
    #             NewIndex1 = Str.index(oldIndex2)
    #             NewIndex2 = Stb.index(oldIndex1)
    #             matrix_vip[NewIndex1][NewIndex2] = float('inf')
    #         del Str[index1]
    #         del Stb[index2]
    #         matrix_vip = Delete(matrix_vip, index1, index2)
    #         if len(matrix_vip) == 1: break
    #
    #     # ?????????????????? ?????????????? ????????
    #     for i in range(0, len(res) - 1, 2):
    #         if res.count(res[i]) < 2:
    #             result.append(res[i])
    #             result.append(res[i + 1])
    #     for i in range(0, len(res) - 1, 2):
    #         for j in range(0, len(res) - 1, 2):
    #             if result[len(result) - 1] == res[j]:
    #                 result.append(res[j])
    #                 result.append(res[j + 1])
    #     # print("----------------------------------")
    #     result_sort = list(dict.fromkeys(result))
    #     result_sort.reverse()
    #
    #     # print(result)
    #     # print(result_sort)
    #     # print()
    #
    #     if len(result_sort) == len(vip):
    #
    #         # print(result_sort)
    #         # print()
    #
    #         for i in result_sort:
    #             coords2.append(vip[i - 1])
    #             if vip[i - 1] != [0, 0]:
    #                 last_coords.append(vip[i - 1])
    #             else:
    #                 last_coords.insert(0, vip[i - 1])
    #         # coords.insert(0, coords.pop())
    #         # coords.reverse()
    #
    #         # ?????????????? ?????????? ????????
    #         for i in range(0, len(result) - 1, 2):
    #             if i == len(result) - 2:
    #                 PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
    #                 PathLenght += StartMatrix[result[i + 1] - 1][result[0] - 1]
    #             else:
    #                 PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
    #         # print(PathLenght)
    #         # print(coords2)
    #         # print("----------------------------------")
    #
    #     else:
    #         dm = np.array(StartMatrix)
    #         result, distance = solve_tsp_local_search(dm)
    #         # print(result, distance)
    #
    #         for i in result:
    #             coords2.append(vip[i])
    #             if vip[i] != [0, 0]:
    #                 last_coords.append(vip[i])
    #             else:
    #                 last_coords.insert(0, vip[i])
    #
    #     if [0, 0] in coords2:
    #         coords2.remove([0, 0])
    #         coords2.insert(0, [0, 0])
    #
    #     # print(coords2)
    #     first.append(coords2[-1])
    #
    # StartMatrix.clear()
    # coords2.clear()
    #
    # mtx.insert(0, [0, 0])
    #
    # if len(first) > 0:
    #     mtx.insert(0, first[0])
    #
    # # mtx.append([1, 1])
    #
    # # ctys = ['Boston', 'Phoenix', 'New York']
    # df = pd.DataFrame(mtx)
    # m = pd.DataFrame(distance_matrix(df.values, df.values))
    #
    # town = 1
    #
    # matrix = m.values.tolist()
    #
    # for i in range(len(matrix)):
    #     matrix[i][i] = float('inf')
    #     for g in range(len(matrix[i])):
    #         matrix[i][g] = round(matrix[i][g], 3)
    # # print(matrix)
    # # print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
    # # ???????????????????????????? ?????????????? ?????? ???????????????????? ????????????????
    # for i in range(len(matrix)):
    #     Str.append(i)
    #     Stb.append(i)
    #
    # # ?????????????????? ?????????????????????? ??????????????
    # for i in range(len(matrix)):
    #     StartMatrix.append(matrix[i].copy())
    #
    # while True:
    #     # ????????????????????
    #     # --------------------------------------
    #     # ???????????????? ?????????????????????? ?????????????? ?? ??????????????
    #     for i in range(len(matrix)):
    #         min_row = min(matrix[i])
    #         min_column = min(row[i] for row in matrix)
    #         H += min_row + min_column
    #         for j in range(len(matrix)):
    #             matrix[i][j] -= min_row
    #             matrix[j][i] -= min_column
    #     # --------------------------------------
    #     # ?????????????????? ?????????????? ???????????? ?? ???????? ?????????????? ???????????? ?? ???????????????????????? ??????????????
    #     # --------------------------------------
    #     NullMax = 0
    #     index1 = 0
    #     index2 = 0
    #     tmp = 0
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix)):
    #             if matrix[i][j] == 0:
    #                 tmp = Min(matrix[i], j) + Min((row[j] for row in matrix), i)
    #                 if tmp >= NullMax:
    #                     NullMax = tmp
    #                     index1 = i
    #                     index2 = j
    #                     lll.append((index1, index2))
    #     # --------------------------------------
    #
    #     # ?????????????? ???????????? ?????? ????????, ???????????????????? ?????? ?? res ?? ?????????????? ?????? ????????????????
    #     res.append(Str[index1] + 1)
    #     res.append(Stb[index2] + 1)
    #
    #     oldIndex1 = Str[index1]
    #     oldIndex2 = Stb[index2]
    #     if oldIndex2 in Str and oldIndex1 in Stb:
    #         # Str = list(dict.fromkeys(Str))
    #         # Stb = list(dict.fromkeys(Stb))
    #
    #         NewIndex1 = Str.index(oldIndex2)
    #         NewIndex2 = Stb.index(oldIndex1)
    #         matrix[NewIndex1][NewIndex2] = float('inf')
    #     del Str[index1]
    #     del Stb[index2]
    #     matrix = Delete(matrix, index1, index2)
    #     if len(matrix) == 1: break
    #
    # # ?????????????????? ?????????????? ????????
    # for i in range(0, len(res) - 1, 2):
    #     if res.count(res[i]) < 2:
    #         result.append(res[i])
    #         result.append(res[i + 1])
    # for i in range(0, len(res) - 1, 2):
    #     for j in range(0, len(res) - 1, 2):
    #         if result[len(result) - 1] == res[j]:
    #             result.append(res[j])
    #             result.append(res[j + 1])
    # # print("----------------------------------")
    # result_sort = list(dict.fromkeys(result))
    # result_sort.reverse()
    #
    # # print(result)
    # # print(result_sort)
    # # print()
    #
    # if len(result_sort) == len(mtx):
    #
    #     # print(result_sort)
    #     # print()
    #
    #     for i in result_sort:
    #         coords2.append(mtx[i - 1])
    #         last_coords.append(mtx[i - 1])
    #         # else:
    #         #     last_coords.insert(0, mtx[i - 1])
    #
    #     # coords.insert(0, coords.pop())
    #     # coords.reverse()
    #
    #     # ?????????????? ?????????? ????????
    #     for i in range(0, len(result) - 1, 2):
    #         if i == len(result) - 2:
    #             PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
    #             PathLenght += StartMatrix[result[i + 1] - 1][result[0] - 1]
    #         else:
    #             PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
    #     # print(PathLenght)
    #
    #     # print("----------------------------------")
    #
    # else:
    #     dm = np.array(StartMatrix)
    #     result, distance = solve_tsp_local_search(dm)
    #     # print(result, distance)
    #
    #     for i in result:
    #         coords2.append(mtx[i])
    #         last_coords.append(mtx[i])
    #         # else:
    #         #     last_coords.insert(0, mtx[i])
    #
    # # print('*******************************')
    # # last_coords[-2], last_coords[-1] = last_coords[-1], last_coords[-2]
    # # last_coords[-3], last_coords[-2:] = last_coords[-2:], last_coords[-3]
    #
    # last_coords2 = []
    #
    # if last_coords.count([0, 0]) > 1:
    #     b = last_coords[last_coords[1:].index([0, 0]) + 1:]
    #
    #     del last_coords[last_coords[1:].index([0, 0]) + 1:]
    #     b.reverse()
    #     for i in b:
    #         last_coords.append(i)
    # # print(last_coords)
    #
    # for i in last_coords:
    #     if i not in last_coords2:
    #         last_coords2.append(i)
    #
    # print(f'{sum(get_list_distance(last_coords2))} ?????????? ???????????? ?? ????????????')
    # VETV.append(sum(get_list_distance(last_coords2)))
    # print()
    #
    #
    # n = len(COORDS)
    # coords2 = []
    # last_coords = []
    # last_coords2 = []
    # last = []
    # vip = []
    # mtx = []
    # population = []
    # dict_populations = {}
    # dict_populations2 = {}
    # way = []
    # POPULATIONS = n * 3
    #
    # for i in COORDS:
    #     # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    #     # list_point = list(map(int, input().split(' ')))
    #     # coords2.append(list_point[:2])
    #     if len(i) == 3:
    #         vip.append(i[:2])
    #     else:
    #         mtx.append(i)
    #
    # if len(vip) != 0:
    #     vip.insert(0, [0, 0])
    # else:
    #     mtx.insert(0, [0, 0])
    # coords2.insert(0, [0, 0])
    #
    # if len(vip) > 0:
    #     for i in range(POPULATIONS * (len(vip))):  # ???????????????????? ?????????????????? ?????????????????? ??????????????????
    #         way.clear()
    #         a = np.random.permutation(len(vip))
    #         popul = a.tolist()
    #         popul.insert(0, popul.pop(popul.index(0)))
    #         for i in popul:
    #             way.append(vip[i])
    #         dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])
    #
    #     dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))
    #
    #     dct = list(dict_populations.keys())
    #     for i in dct:
    #         population = [int(x) for x in i[1:-1].split(', ')]
    #         break
    #
    #     for i in population:
    #         last_coords.append(vip[i])
    #
    #     last = last_coords[-1]
    #     # del last_coords[-1]
    #     mtx.insert(0, last)
    #     mtx.append([0, 0])
    #
    #     for i in range(POPULATIONS * (n - len(vip) + 1)):  # ???????????????????? ?????????????????? ?????????????????? ??????????????????
    #         way.clear()
    #         a = np.random.permutation(len(mtx))
    #         popul = a.tolist()
    #         popul.insert(0, popul.pop(popul.index(0)))
    #         popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))
    #         for i in popul:
    #             way.append(mtx[i])
    #         dict_populations2[str(popul)] = sum(get_list_distance(way)[:-1])
    #
    #     dict_populations2 = dict(sorted(dict_populations2.items(), key=lambda item: item[1]))
    #
    #     dct = list(dict_populations2.keys())
    #     for i in dct:
    #         population = [int(x) for x in i[1:-1].split(', ')]
    #         break
    #
    #     for i in population:
    #         last_coords2.append(mtx[i])
    #
    #
    # else:
    #     for i in range(POPULATIONS * n):  # ???????????????????? ?????????????????? ?????????????????? ??????????????????
    #         way.clear()
    #         a = np.random.permutation(n + 1)
    #         popul = a.tolist()
    #         popul.insert(0, popul.pop(popul.index(0)))
    #         for i in popul:
    #             way.append(mtx[i])
    #         dict_populations[str(popul)] = sum(get_list_distance(way))
    #
    #     dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))
    #
    #     dct = list(dict_populations.keys())
    #     for i in dct:
    #         population = [int(x) for x in i[1:-1].split(', ')]
    #         break
    #
    #     for i in population:
    #         last_coords.append(mtx[i])
    #
    # last_coords3 = []
    #
    # for i in last_coords:
    #     if i not in last_coords3:
    #         last_coords3.append(i)
    #
    # for i in last_coords2:
    #     if i not in last_coords3:
    #         last_coords3.append(i)
    #
    # print(f'{sum(get_list_distance(last_coords3))} ?????????? ?????????? ??????????')
    # MONTE.append(sum(get_list_distance(last_coords3)))


    n = len(COORDS)
    coords2 = []
    last_coords = []
    last_coords2 = []
    vip = []
    mtx = []
    population = []
    st = []
    dead_individuals = []
    dict_populations = {}
    way = []
    PERCENTAGE_OF_MUTATIONS = 12
    NUMBER_OF_GENERATIONS = 50000
    POPULATIONS = n * 3

    for i in COORDS:
        # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
        # list_point = list(map(int, input().split(' ')))
        # coords2.append(list_point[:2])
        if len(i) == 3:
            vip.append(i[:2])
        else:
            mtx.append(i)

    if len(vip) != 0:
        vip.insert(0, [0, 0])
    else:
        mtx.insert(0, [0, 0])
    coords2.insert(0, [0, 0])

    if len(vip) > 0:
        for i in range(len(vip)):
            st.append(i)

        for i in st:
            way.append(vip[i])
        dict_populations[str(st)] = sum(get_list_distance(way)[:-1])
        population.insert(0, st)

        for i in range(POPULATIONS):  # ???????????????????? ?????????????????? ?????????????????? ??????????????????
            way.clear()
            a = np.random.permutation(len(vip))
            popul = a.tolist()
            popul.insert(0, popul.pop(popul.index(0)))
            for i in popul:
                way.append(vip[i])
            dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])
            if popul not in population:
                population.append(popul)
            else:
                a = np.random.permutation(n + 1)
                popul = a.tolist()
                popul.insert(0, popul.pop(popul.index(0)))
                population.append(popul)

        # print(dict_populations)
        # print()
        # print(population)
        # print()

        for i in range(NUMBER_OF_GENERATIONS):
            if len(dict_populations) < POPULATIONS:
                for i in range(POPULATIONS - len(dict_populations)):
                    a = np.random.permutation(len(vip))
                    popul = a.tolist()
                    popul.insert(0, popul.pop(popul.index(0)))

                    if str(popul) in dict_populations or str(popul) in dead_individuals:
                        a = np.random.permutation(len(vip))
                        popul = a.tolist()
                        popul.insert(0, popul.pop(popul.index(0)))

                    way.clear()
                    for i in popul:
                        way.append(vip[i])
                    dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])

            dct = list(dict_populations.keys())
            population = []
            for i in dct:
                population.append([int(x) for x in i[1:-1].split(', ')])

            # ???????????? ??????????????????
            # -------------------

            # 1 ??????
            q1 = random.choice(population)  # ???????????? ????????????????
            gg = population.index(q1)
            del population[gg]

            q2 = random.choice(population)
            gg = population.index(q2)
            # del population[gg]
            # ???????????? ????????????????

            # print(q1, q2)
            # print(dict_populations[str(q1)], dict_populations[str(q2)])

            if dict_populations[str(q1)] > dict_populations[str(q2)]:  # ?????????? ???????????????????? ?????????????? ????????
                win1 = q2
            else:
                win1 = q1

            # 2 ??????
            qq1 = random.choice(population)  # ???????????? ????????????????
            gg = population.index(qq1)
            # del population[gg]

            qq2 = random.choice(population)  # ???????????? ????????????????

            if dict_populations[str(qq1)] > dict_populations[str(qq2)]:  # ?????????? ???????????????????? ?????????????? ????????
                win2 = qq2
            else:
                win2 = qq1

            parent1 = win1  # ???????????? ????????????????
            parent2 = win2  # ???????????? ????????????????
            # parent1 = [0, 6, 2, 7, 3, 8, 1, 4, 9, 5]
            # parent2 = [0, 3, 9, 4, 1, 7, 5, 6, 2, 8]
            # print(parent1, parent2)

            point = random.randint(0, len(vip))  # ?????????????????? ?????????? ??????????????
            # print(point)
            # print()

            # ???????????????????????? ?????????????? ??????????????
            child1 = parent1[:point + 1]
            for i in parent2[:]:
                if i not in child1:
                    child1.append(i)

            # print(child1)

            # ???????????????????????? ?????????????? ??????????????
            child2 = parent2[:point + 1]
            for i in parent1[:]:
                if i not in child2:
                    child2.append(i)

            # print(child2)
            # print()

            #  ??????????????
            choice = []
            for i in range(len(vip)):
                if i != 0:
                    choice.append(i)

            # ?????????????? ?????????????? ??????????????
            for i in range(1, len(child1)):
                number1 = random.choice(choice)
                mutation = random.randint(0, 100)
                if mutation < PERCENTAGE_OF_MUTATIONS:
                    child1[number1], child1[i] = child1[i], child1[number1]

            # ?????????????? ?????????????? ??????????????
            for i in range(1, len(child2)):
                number2 = random.choice(choice)
                mutation = random.randint(0, 100)
                if mutation < PERCENTAGE_OF_MUTATIONS:
                    child2[number2], child2[i] = child2[i], child2[number2]

            # ???????????????????? ???????????????? ?? ?????????? ?????????????? ?? ???????????????? ???????????????? ?????????????????????????????? ????????????
            way.clear()
            for i in child1:
                way.append(vip[i])
            dict_populations[str(child1)] = sum(get_list_distance(way))

            way.clear()
            for i in child2:
                way.append(vip[i])
            dict_populations[str(child2)] = sum(get_list_distance(way))

            # ???????????????? ???????????????? ?????????????????????????????? ????????????
            dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

            if len(list(dict_populations.keys())) > 2:
                dead_individuals.append(list(dict_populations)[-1])
                dict_populations.pop(list(dict_populations)[-1])

                dead_individuals.append(list(dict_populations)[-1])
                dict_populations.pop(list(dict_populations)[-1])

            # print(dead_individuals)
            # print()
            # print(dict_populations)
            # print()

        # print('-------------------')
        dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

        dct = list(dict_populations.keys())
        population.clear()

        for i in dct:
            population = [int(x) for x in i[1:-1].split(', ')]
            break
        # print(population, dict_populations[next(iter(dict_populations))])

        for i in population:
            last_coords.append(vip[i])

        # print(last_coords)
        last = last_coords[-1]
        # del last_coords[-1]
        mtx.insert(0, last)
        mtx.append([0, 0])
        st.clear()
        dict_populations.clear()

        for i in range(len(mtx)):
            st.append(i)

        for i in st:
            way.append(mtx[i])
        dict_populations[str(st)] = sum(get_list_distance(way)[:-1])
        population.insert(0, st)

        for i in range(POPULATIONS):  # ???????????????????? ?????????????????? ?????????????????? ??????????????????
            way.clear()
            a = np.random.permutation(len(mtx))
            popul = a.tolist()
            popul.insert(0, popul.pop(popul.index(0)))
            popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))
            for i in popul:
                way.append(mtx[i])
            dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])
            if popul not in population:
                population.append(popul)
            else:
                a = np.random.permutation(n + 1)
                popul = a.tolist()
                popul.insert(0, popul.pop(popul.index(0)))
                popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))
                population.append(popul)

        # print(dict_populations)
        # print()
        # print(population)
        # print()

        for i in range(NUMBER_OF_GENERATIONS):
            if len(dict_populations) < POPULATIONS:
                for i in range(POPULATIONS - len(dict_populations)):
                    a = np.random.permutation(len(mtx))
                    popul = a.tolist()
                    popul.insert(0, popul.pop(popul.index(0)))
                    popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))

                    if str(popul) in dict_populations or str(popul) in dead_individuals:
                        a = np.random.permutation(len(mtx))
                        popul = a.tolist()
                        popul.insert(0, popul.pop(popul.index(0)))
                        popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))

                    way.clear()
                    for i in popul:
                        way.append(mtx[i])
                    dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])

            dct = list(dict_populations.keys())
            population = []
            for i in dct:
                population.append([int(x) for x in i[1:-1].split(', ')])

            # ???????????? ??????????????????
            # -------------------

            # 1 ??????
            q1 = random.choice(population)  # ???????????? ????????????????
            gg = population.index(q1)
            del population[gg]

            q2 = random.choice(population)
            gg = population.index(q2)
            del population[gg]
            # ???????????? ????????????????

            # print(q1, q2)
            # print(dict_populations[str(q1)], dict_populations[str(q2)])

            if dict_populations[str(q1)] > dict_populations[str(q2)]:  # ?????????? ???????????????????? ?????????????? ????????
                win1 = q2
            else:
                win1 = q1

            # 2 ??????
            qq1 = random.choice(population)  # ???????????? ????????????????
            gg = population.index(qq1)
            del population[gg]

            qq2 = random.choice(population)  # ???????????? ????????????????

            if dict_populations[str(qq1)] > dict_populations[str(qq2)]:  # ?????????? ???????????????????? ?????????????? ????????
                win2 = qq2
            else:
                win2 = qq1

            parent1 = win1  # ???????????? ????????????????
            parent2 = win2  # ???????????? ????????????????
            # parent1 = [0, 6, 2, 7, 3, 8, 1, 4, 9, 5]
            # parent2 = [0, 3, 9, 4, 1, 7, 5, 6, 2, 8]
            # print(parent1, parent2)

            point = random.randint(0, len(mtx))  # ?????????????????? ?????????? ??????????????
            # print(point)
            # print()

            # ???????????????????????? ?????????????? ??????????????
            child1 = parent1[:point + 1]
            for i in parent2[:]:
                if i not in child1:
                    child1.append(i)

            # print(child1)

            # ???????????????????????? ?????????????? ??????????????
            child2 = parent2[:point + 1]
            for i in parent1[:]:
                if i not in child2:
                    child2.append(i)

            # print(child2)
            # print()

            #  ??????????????
            choice = []
            for i in range(len(mtx)):
                if i != 0 and i != len(mtx) - 1:
                    choice.append(i)

            # ?????????????? ?????????????? ??????????????
            for i in range(1, len(child1) - 1):
                number1 = random.choice(choice)
                mutation = random.randint(0, 100)
                if mutation < PERCENTAGE_OF_MUTATIONS:
                    child1[number1], child1[i] = child1[i], child1[number1]

            # ?????????????? ?????????????? ??????????????
            for i in range(1, len(child2) - 1):
                number2 = random.choice(choice)
                mutation = random.randint(0, 100)
                if mutation < PERCENTAGE_OF_MUTATIONS:
                    child2[number2], child2[i] = child2[i], child2[number2]

            # ???????????????????? ???????????????? ?? ?????????? ?????????????? ?? ???????????????? ???????????????? ?????????????????????????????? ????????????
            way.clear()
            for i in child1:
                way.append(mtx[i])
            dict_populations[str(child1)] = sum(get_list_distance(way)[:-1])

            way.clear()
            for i in child2:
                way.append(mtx[i])
            dict_populations[str(child2)] = sum(get_list_distance(way)[:-1])

            # ???????????????? ???????????????? ?????????????????????????????? ????????????
            dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

            dead_individuals.append(list(dict_populations)[-1])
            dict_populations.pop(list(dict_populations)[-1])

            dead_individuals.append(list(dict_populations)[-1])
            dict_populations.pop(list(dict_populations)[-1])

            # print(dead_individuals)
            # print()
            # print(dict_populations)
            # print()

        # print('-------------------')
        dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

        dct = list(dict_populations.keys())
        population.clear()

        for i in dct:
            population = [int(x) for x in i[1:-1].split(', ')]
            break
        # print(population, dict_populations[next(iter(dict_populations))])

        for i in population:
            last_coords2.append(mtx[i])

        # print(last_coords2)

    else:
        for i in range(n + 1):
            st.append(i)

        for i in st:
            way.append(mtx[i])
        dict_populations[str(st)] = sum(get_list_distance(way))
        population.insert(0, st)

        for i in range(POPULATIONS):  # ???????????????????? ?????????????????? ?????????????????? ??????????????????
            way.clear()
            a = np.random.permutation(n + 1)
            popul = a.tolist()
            popul.insert(0, popul.pop(popul.index(0)))
            for i in popul:
                way.append(mtx[i])
            dict_populations[str(popul)] = sum(get_list_distance(way))
            if popul not in population:
                population.append(popul)
            else:
                a = np.random.permutation(n + 1)
                popul = a.tolist()
                popul.insert(0, popul.pop(popul.index(0)))
                population.append(popul)

        # print(dict_populations)
        # print()
        # print(population)
        # print()

        for i in range(NUMBER_OF_GENERATIONS):
            if len(dict_populations) < POPULATIONS:
                for i in range(POPULATIONS - len(dict_populations)):
                    a = np.random.permutation(n + 1)
                    popul = a.tolist()
                    popul.insert(0, popul.pop(popul.index(0)))
                    g = 0

                    while str(popul) in dead_individuals:
                        g += 1
                        # print(g)
                        if g == 50:
                            break
                        a = np.random.permutation(n + 1)
                        popul = a.tolist()
                        popul.insert(0, popul.pop(popul.index(0)))

                    way.clear()
                    for i in popul:
                        way.append(mtx[i])
                    dict_populations[str(popul)] = sum(get_list_distance(way))

            dct = list(dict_populations.keys())
            population = []
            for i in dct:
                population.append([int(x) for x in i[1:-1].split(', ')])

            # ???????????? ??????????????????
            # -------------------

            # 1 ??????
            q1 = random.choice(population)  # ???????????? ????????????????
            gg = population.index(q1)
            del population[gg]

            q2 = random.choice(population)
            gg = population.index(q2)
            # ???????????? ????????????????

            # print(q1, q2)
            # print(dict_populations[str(q1)], dict_populations[str(q2)])

            if dict_populations[str(q1)] > dict_populations[str(q2)]:  # ?????????? ???????????????????? ?????????????? ????????
                win1 = q2
            else:
                win1 = q1

            # 2 ??????
            qq1 = random.choice(population)  # ???????????? ????????????????
            gg = population.index(qq1)

            qq2 = random.choice(population)  # ???????????? ????????????????

            if dict_populations[str(qq1)] > dict_populations[str(qq2)]:  # ?????????? ???????????????????? ?????????????? ????????
                win2 = qq2
            else:
                win2 = qq1

            parent1 = win1  # ???????????? ????????????????
            parent2 = win2  # ???????????? ????????????????
            # parent1 = [0, 6, 2, 7, 3, 8, 1, 4, 9, 5]
            # parent2 = [0, 3, 9, 4, 1, 7, 5, 6, 2, 8]
            # print(parent1, parent2)

            point = random.randint(0, n - 1)  # ?????????????????? ?????????? ??????????????
            # print(point)
            # print()

            # ???????????????????????? ?????????????? ??????????????
            child1 = parent1[:point + 1]
            for i in parent2[:]:
                if i not in child1:
                    child1.append(i)

            # print(child1)

            # ???????????????????????? ?????????????? ??????????????
            child2 = parent2[:point + 1]
            for i in parent1[:]:
                if i not in child2:
                    child2.append(i)

            # print(child2)
            # print()

            #  ??????????????
            choice = []
            for i in range(n):
                if i != 0:
                    choice.append(i)

            # ?????????????? ?????????????? ??????????????
            for i in range(1, len(child1)):
                number1 = random.choice(choice)
                mutation = random.randint(0, 100)
                if mutation < PERCENTAGE_OF_MUTATIONS:
                    child1[number1], child1[i] = child1[i], child1[number1]

            # ?????????????? ?????????????? ??????????????
            for i in range(1, len(child2)):
                number2 = random.choice(choice)
                mutation = random.randint(0, 100)
                if mutation < PERCENTAGE_OF_MUTATIONS:
                    child2[number2], child2[i] = child2[i], child2[number2]

            # ???????????????????? ???????????????? ?? ?????????? ?????????????? ?? ???????????????? ???????????????? ?????????????????????????????? ????????????
            way.clear()
            for i in child1:
                way.append(mtx[i])
            dict_populations[str(child1)] = sum(get_list_distance(way))

            way.clear()
            for i in child2:
                way.append(mtx[i])
            dict_populations[str(child2)] = sum(get_list_distance(way))

            # ???????????????? ???????????????? ?????????????????????????????? ????????????
            dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

            dead_individuals.append(list(dict_populations)[-1])
            dict_populations.pop(list(dict_populations)[-1])

            dead_individuals.append(list(dict_populations)[-1])
            dict_populations.pop(list(dict_populations)[-1])

            # print(dead_individuals)
            # print()
            # print(dict_populations)
            # print()

        # print('-------------------')
        dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

        dct = list(dict_populations.keys())
        population.clear()

        for i in dct:
            population = [int(x) for x in i[1:-1].split(', ')]
            break
        # print(population, dict_populations[next(iter(dict_populations))])

        for i in population:
            last_coords.append(mtx[i])

        # print(last_coords)

    last_coords3 = []

    for i in last_coords:
        if i not in last_coords3:
            last_coords3.append(i)

    for i in last_coords2:
        if i not in last_coords3:
            last_coords3.append(i)

    print(f'{sum(get_list_distance(last_coords3))} ???????????????????????? ????????????????')
    GA.append(sum(get_list_distance(last_coords3)))
    print()
    print('----------------')

itog1 = []
itog2 = []
itog3 = []
itog4 = []
itog5 = []
n = 18

for i in range(10):
    n += 2

    COORDS = []
    print(n)

    for i in range(n):
        b = random.choice([0, 1])
        if b == 1:
            a = f'{random.randint(0, 500)} {random.randint(0, 500)} 1'
            list_point = list(map(int, a.split(' ')))
            COORDS.append(list_point)
        else:
            a = f'{random.randint(0, 500)} {random.randint(0, 500)}'
            list_point = list(map(int, a.split(' ')))
            COORDS.append(list_point)
        # if len(list_point) == 3:
        #     vip.append(list_point[:2])
        # else:
        #     mtx.append(list_point)

    if len(GA) > 0:
        itog1.append(sum(POLN) / len(POLN))
        itog2.append(sum(GHAD) / len(GHAD))
        itog3.append(sum(VETV) / len(VETV))
        itog4.append(sum(MONTE) / len(MONTE))
        itog5.append(sum(GA) / len(GA))
        # print(POLN)
        POLN.clear()
        GHAD.clear()
        VETV.clear()
        MONTE.clear()
        GA.clear()

    for i in range(10):
        gg(COORDS)

    if len(GA) > 0:
        if len(POLN) != 0:
            itog1.append(sum(POLN) / len(POLN))
        itog2.append(sum(GHAD) / len(GHAD))
        itog3.append(sum(VETV) / len(VETV))
        itog4.append(sum(MONTE) / len(MONTE))
        itog5.append(sum(GA) / len(GA))
        print(POLN)
        POLN.clear()
        GHAD.clear()
        VETV.clear()
        MONTE.clear()
        GA.clear()

print(itog1)
print()
print(itog2)
print()
print(itog3)
print()
print(itog4)
print()
print(itog5)
