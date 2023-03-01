import random

import numpy as np
import matplotlib.pyplot as plt

from distance_calculation import get_list_distance


GA1 = []
GA2 = []
itog1 = []
itog2 = []

for i in range(1):
    n = random.randint(15, 40)
    coords2 = []
    last_coords = []
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

    for i in range(n):
        b = random.choice([0, 0])
        a = f'{random.randint(0, 500)} {random.randint(0, 500)}'
        list_point = list(map(int, a.split(' ')))
        coords2.append(list_point[:2])
        if len(list_point) == 3:
            vip.append(list_point[:2])
        else:
            mtx.append(list_point)

    if len(GA1) > 0:
        itog1.append(sum(GA1) / len(GA1))
        itog2.append(sum(GA2) / len(GA2))
        GA1.clear()
        GA2.clear()

    for i in range(10):
        for i in range(n + 1):
            st.append(i)

        if len(vip) != 0:
            vip.insert(0, [0, 0])
        elif [0, 0] not in mtx:
            mtx.insert(0, [0, 0])
        coords2.insert(0, [0, 0])

        # print(mtx)

        for i in st:
            way.append(mtx[i])
        dict_populations[str(st)] = sum(get_list_distance(way))
        population.insert(0, st)

        for i in range(POPULATIONS):  # количество генераций начальных популяций
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

                    while str(popul) in dict_populations or str(popul) in dead_individuals:
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

            # турнир родителей
            # -------------------

            # 1 тур
            q1 = random.choice(population)  # первый участник
            gg = population.index(q1)
            del population[gg]

            q2 = random.choice(population)
            gg = population.index(q2)
            del population[gg]
            # второй участник

            # print(q1, q2)
            # print(dict_populations[str(q1)], dict_populations[str(q2)])

            if dict_populations[str(q1)] > dict_populations[str(q2)]:  # поиск победителя первого тура
                win1 = q2
            else:
                win1 = q1

            # 2 тур
            qq1 = random.choice(population)  # первый участник
            gg = population.index(qq1)
            del population[gg]

            qq2 = random.choice(population)  # второй участник

            if dict_populations[str(qq1)] > dict_populations[str(qq2)]:  # поиск победителя второго тура
                win2 = qq2
            else:
                win2 = qq1


            parent1 = win1  # первый родитель
            parent2 = win2  # второй родитель
            # parent1 = [0, 6, 2, 7, 3, 8, 1, 4, 9, 5]
            # parent2 = [0, 3, 9, 4, 1, 7, 5, 6, 2, 8]
            # print(parent1, parent2)

            point = random.randint(0, n - 1)  # генерация точки разрыва
            # print(point)
            # print()

            # формирование первого потомка
            child1 = parent1[:point + 1]
            for i in parent2[:]:
                if i not in child1:
                    child1.append(i)

            # print(child1)

            # формирование второго потомка
            child2 = parent2[:point + 1]
            for i in parent1[:]:
                if i not in child2:
                    child2.append(i)

            # print(child2)
            # print()

            #  мутация
            mutation = random.randint(0, 100)
            # print(mutation)
            if mutation < PERCENTAGE_OF_MUTATIONS:
                choice = []
                for i in range(n):
                    if i != 0:
                        choice.append(i)

                # мутация первого потомка
                number1 = random.choice(choice)
                del choice[choice.index(number1)]
                number2 = random.choice(choice)
                choice.append(number1)

                if number1 != number2:
                    child1[number1], child1[number2] = child1[number2], child1[number1]
                else:
                    number2 = random.randint(1, n - 1)
                    child1[number1], child1[number2] = child1[number2], child1[number1]
                # мутация второго потомка
                number1 = random.choice(choice)
                del choice[choice.index(number1)]
                number2 = random.choice(choice)

                if number1 != number2:
                    child2[number1], child2[number2] = child2[number2], child2[number1]
                else:
                    number2 = random.randint(1, n - 1)
                    child2[number1], child2[number2] = child2[number2], child2[number1]

            # print(child1, child2)
            # print()

            # добавление потомков в общий словарь и удаление наименее приспособленных особей
            way.clear()
            for i in child1:
                way.append(mtx[i])
            dict_populations[str(child1)] = sum(get_list_distance(way))

            way.clear()
            for i in child2:
                way.append(mtx[i])
            dict_populations[str(child2)] = sum(get_list_distance(way))

            # удаление наименее приспособленных особей
            dead_individuals.append(list(dict_populations)[list(dict_populations.keys()).index(str(win1))])  # убийство родителей :(
            dict_populations.pop(list(dict_populations)[list(dict_populations.keys()).index(str(win1))])

            dead_individuals.append(list(dict_populations)[list(dict_populations.keys()).index(str(win2))])
            dict_populations.pop(list(dict_populations)[list(dict_populations.keys()).index(str(win2))])

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
        # print()
        GA1.append(dict_populations[next(iter(dict_populations))])


        coords2 = []
        population = []
        st = []
        dead_individuals = []
        dict_populations = {}
        way = []


        for i in range(n + 1):
            st.append(i)

        for i in st:
            way.append(mtx[i])
        dict_populations[str(st)] = sum(get_list_distance(way))
        population.insert(0, st)

        for i in range(POPULATIONS):  # количество генераций начальных популяций
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

                    while str(popul) in dict_populations or str(popul) in dead_individuals:
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

            # турнир родителей
            # -------------------

            # 1 тур
            q1 = random.choice(population)  # первый участник
            gg = population.index(q1)
            del population[gg]

            q2 = random.choice(population)
            gg = population.index(q2)
            del population[gg]
            # второй участник

            # print(q1, q2)
            # print(dict_populations[str(q1)], dict_populations[str(q2)])

            if dict_populations[str(q1)] > dict_populations[str(q2)]:  # поиск победителя первого тура
                win1 = q2
            else:
                win1 = q1

            # 2 тур
            qq1 = random.choice(population)  # первый участник
            gg = population.index(qq1)
            del population[gg]

            qq2 = random.choice(population)  # второй участник

            if dict_populations[str(qq1)] > dict_populations[str(qq2)]:  # поиск победителя второго тура
                win2 = qq2
            else:
                win2 = qq1


            parent1 = win1  # первый родитель
            parent2 = win2  # второй родитель
            # parent1 = [0, 6, 2, 7, 3, 8, 1, 4, 9, 5]
            # parent2 = [0, 3, 9, 4, 1, 7, 5, 6, 2, 8]
            # print(parent1, parent2)

            point = random.randint(0, n - 1)  # генерация точки разрыва
            # print(point)
            # print()

            # формирование первого потомка
            child1 = parent1[:point + 1]
            for i in parent2[:]:
                if i not in child1:
                    child1.append(i)

            # print(child1)

            # формирование второго потомка
            child2 = parent2[:point + 1]
            for i in parent1[:]:
                if i not in child2:
                    child2.append(i)

            # print(child2)
            # print()

            #  мутация
            choice = []
            for i in range(n):
                if i != 0:
                    choice.append(i)

            # мутация первого потомка
            for i in range(1, len(child1)):
                number1 = random.choice(choice)
                mutation = random.randint(0, 100)
                if mutation < PERCENTAGE_OF_MUTATIONS:
                    child1[number1], child1[i] = child1[i], child1[number1]

            # мутация второго потомка
            for i in range(1, len(child2)):
                number2 = random.choice(choice)
                mutation = random.randint(0, 100)
                if mutation < PERCENTAGE_OF_MUTATIONS:
                    child1[number2], child1[i] = child1[i], child1[number2]


            # добавление потомков в общий словарь и удаление наименее приспособленных особей
            way.clear()
            for i in child1:
                way.append(mtx[i])
            dict_populations[str(child1)] = sum(get_list_distance(way))

            way.clear()
            for i in child2:
                way.append(mtx[i])
            dict_populations[str(child2)] = sum(get_list_distance(way))

            # удаление наименее приспособленных особей
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
        # print()
        GA2.append(dict_populations[next(iter(dict_populations))])

if len(GA1) > 0:
    itog1.append(sum(GA1) / len(GA1))
    itog2.append(sum(GA2) / len(GA2))
    GA1.clear()
    GA2.clear()

print(itog1)
print()
print(itog2)
