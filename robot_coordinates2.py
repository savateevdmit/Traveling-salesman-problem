import itertools
import time
from copy import copy
import random
import matplotlib.pyplot as plt
from choise_metod import checkboxs


from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
import serial as serial
from distance_calculation import get_list_distance
from kivy.lang import Builder
import x
import y

ONGR = [False]
ONR = [False]
coords_view = []
COORDS = []
METOD = [0]


class Demo(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        self.screen = Screen()

        self.label = MDLabel(text="Пока никуда не едет(", pos_hint={'center_x': 0.52, 'center_y': 0.1},
                            font_style="Subtitle1")

        self.label1 = MDLabel(text="Полный перебор", pos_hint={'center_x': 1.17, 'center_y': 0.8},
                             font_style="Subtitle1")
        self.label2 = MDLabel(text="Жадный алгоритм", pos_hint={'center_x': 1.17, 'center_y': 0.7},
                             font_style="Subtitle1")

        self.label3 = MDLabel(text="Введите координаты:", pos_hint={'center_x': 0.65, 'center_y': 0.93},
                            font_style="Subtitle1")
        self.label4 = MDLabel(text="Выберите алгоритм решения:", pos_hint={'center_x': 1.08, 'center_y': 0.93},
                              font_style="Subtitle1")

        green = MDRectangleFlatButton(text="Добавить", pos_hint={'center_x': 0.15, 'center_y': 0.6}, on_release=self.greenf, ripple_color='orange', line_color="orange")
        delite = MDRectangleFlatButton(text="Очистить", pos_hint={'center_x': 0.35, 'center_y': 0.6}, on_release=self.delite, ripple_color='red', line_color="red")
        red = MDRectangleFlatButton(text="Старт", pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.redf, ripple_color='green', line_color="green")

        sample1 = MDRectangleFlatButton(text="Тестовые данные №1", pos_hint={'center_x': 0.15, 'center_y': 0.4}, on_release=self.sample1, ripple_color='pink', line_color="pink")
        sample2 = MDRectangleFlatButton(text="Тестовые данные №2", pos_hint={'center_x': 0.45, 'center_y': 0.4}, on_release=self.sample2, ripple_color='pink', line_color="blue")


        self.x = Builder.load_string(x.x_input)
        self.y = Builder.load_string(y.y_input)

        checkbox = Builder.load_string(checkboxs)

        self.screen.add_widget(green)
        self.screen.add_widget(red)
        self.screen.add_widget(delite)
        self.screen.add_widget(sample1)
        self.screen.add_widget(sample2)
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.label1)
        self.screen.add_widget(self.label2)
        self.screen.add_widget(self.label3)
        self.screen.add_widget(self.label4)
        self.screen.add_widget(self.x)
        self.screen.add_widget(self.y)
        self.screen.add_widget(checkbox)

        # adding widgets to screen

        return self.screen

    def greenf(self, obj):
        coords_view.append(f'({int(self.x.text)};{int(self.y.text)})')
        COORDS.append([int(self.x.text), int(self.y.text)])
        self.label.text = ', '.join(coords_view)
        self.x.text = ''
        self.y.text = ''

    def sample1(self, obj):
        coords_view.append('(4;9)')
        coords_view.append('(6;2)')
        coords_view.append('(5;7)')
        coords_view.append('(6;1)')
        coords_view.append('(6;9)')

        COORDS.append([4, 9])
        COORDS.append([6, 2])
        COORDS.append([5, 7])
        COORDS.append([6, 1])
        COORDS.append([6, 9])
        self.label.text = ', '.join(coords_view)
        self.x.text = ''
        self.y.text = ''

    def sample2(self, obj):
        coords_view.append('(2;3)')
        coords_view.append('(1;7)')
        coords_view.append('(4;6)')
        coords_view.append('(6;9)')
        coords_view.append('(6;12)')
        coords_view.append('(18;5)')
        coords_view.append('(9;2)')
        coords_view.append('(8;4)')


        COORDS.append([2, 3])
        COORDS.append([1, 7])
        COORDS.append([4, 6])
        COORDS.append([6, 9])
        COORDS.append([6, 12])
        COORDS.append([18, 5])
        COORDS.append([9, 2])
        COORDS.append([8, 4])

        self.label.text = ', '.join(coords_view)
        self.x.text = ''
        self.y.text = ''


    def delite(self, obj):
        coords_view.clear()
        COORDS.clear()
        self.label.text = 'Пока никуда не едет('
        self.x.text = ''
        self.y.text = ''

    def redf(self, obj):
        print(COORDS)
        if len(COORDS) == 0:
            self.dialog = MDDialog(title='Введите координаты!',
                                   size_hint=(0.4, 0),
                                   buttons=[MDFlatButton(text='Закрыть', on_release=self.close_dialog)]
                                   )
            self.dialog.open()

        elif METOD[0] == 2:
            print('жадный алгоритм')
            if [0, 0] in COORDS:
                COORDS.remove([0, 0])
                # coords_view.remove('(0;0)')
            list_points = []
            way_now = {}
            shortest_way = 0
            town = 0
            shortest_way_coords = [[0, 0]]
            fig, ax = plt.subplots()


            COORDS.insert(0, [0, 0])
            # print(coords)
            for x, y in COORDS:
                if x == 0 and y == 0:
                    ax.add_patch(plt.Circle((x, y), 0.3, facecolor='#FF0000', alpha=1))
                else:
                    ax.add_patch(plt.Circle((x, y), 0.3, facecolor='#9ebcda', alpha=1))

                plt.text(x - 0.22, y - 0.22, f'{town}')
                town += 1
            # del coords[0]

            while len(COORDS) > 2:
                for i in range(len(COORDS)):
                    if i != 0:
                        list_points.append(COORDS[0])
                        list_points.append(COORDS[i])
                        distance = get_list_distance(list_points)
                        distance = distance[0]
                        way_now[i] = distance
                        # print(distance)
                        list_points.clear()
                d = [k for k, v in way_now.items() if v == min(way_now.values())]
                shortest_way += way_now[d[0]]
                shortest_way_coords.append(COORDS[d[0]])
                COORDS.insert(0, COORDS.pop(d[0]))
                del COORDS[1]
                way_now.clear()
                # print(coords)

            distance = get_list_distance(COORDS)
            distance = distance[0]
            shortest_way += distance
            shortest_way_coords.append(COORDS[-1])

            print(shortest_way)
            print(shortest_way_coords)

            self.dialog = MDDialog(title='Системное оповещение',
                                   text=f'Самый короткий путь: {shortest_way}, маршрут: {shortest_way_coords} \n'
                                        f'Данные отправились по Bluetooth микроконтроллеру', size_hint=(0.8, 0),
                                   buttons=[MDFlatButton(text='Ok', on_release=self.close_dialog)]
                                   )
            self.dialog.open()
            # self.label.text = f'Самый короткий путь: {shortest_way}, маршрут: {shortest_way_coords}'
            self.label.text = ', '.join(coords_view)
            self.x.text = ''
            self.y.text = ''

            for i in range(len(shortest_way_coords)):
                if len(shortest_way_coords) > i + 1:
                    plt.plot((shortest_way_coords[i][0], shortest_way_coords[i + 1][0]), (shortest_way_coords[i][1], shortest_way_coords[i + 1][1]), alpha=0.6)
                else:
                    plt.plot((shortest_way_coords[-1][0], shortest_way_coords[0][0]), (shortest_way_coords[-1][1], shortest_way_coords[0][1]), alpha=0.6)
            # Use adjustable='box-forced' to make the plot area square-shaped as well.
            ax.set_aspect('equal', adjustable='datalim')
            ax.set_xbound(3, 4)

            ax.plot()  # Causes an autoscale update.
            plt.show()

            # coords_view.clear()
            # coords.clear()

            # s = serial.Serial("COM4", 9600)
            # shortest_way_coords.append([0, 0])
            # for i in range(len(shortest_way_coords)):
            #     if i != 0:
            #         s.write(bytes(shortest_way_coords[i]))

        elif METOD[0] == 1:
            if [0, 0] in COORDS:
                COORDS.remove([0, 0])
                # coords_view.remove('(0;0)')
            print('полный перебор')
            print(coords_view)
            fig, ax = plt.subplots()

            route = 0
            list_points = []
            town = 0
            dict_coords = {}
            number_towns_list = []
            shortest_path = 100000

            t1 = time.time()
            COORDS.insert(0, [0, 0])
            for x, y in COORDS:
                dict_coords[town] = (x, y)
                number_towns_list.append(town)
                if x == 0 and y == 0:
                    ax.add_patch(plt.Circle((x, y), 0.3, facecolor='#FF0000', alpha=1))
                else:
                    ax.add_patch(plt.Circle((x, y), 0.3, facecolor='#9ebcda', alpha=1))

                plt.text(x - 0.22, y - 0.22, f'{town}')
                town += 1
            # del coords[0]

            for i in itertools.permutations(number_towns_list):
                for j in i:
                    list_points.append(dict_coords[int(j)])
                list_points.insert(0, (0, 0))
                # print(list_points)
                distance = sum(get_list_distance(list_points))
                print(get_list_distance(list_points)[:-1])
                if distance < shortest_path:
                    shortest_path = distance
                    route = copy(list_points)
                list_points.clear()

            t2 = time.time()
            print(f'Самый короткий путь: {shortest_path}, маршрут: {route[1:]}')
            print(f'Потраченное время: {t2 - t1}')

            self.dialog = MDDialog(title='Системное оповещение',
                                   text=f'Самый короткий путь: {shortest_path}, маршрут: {route[1:]} \n'
                                        f'Данные отправились по Bluetooth микроконтроллеру', size_hint=(0.8, 0),
                                   buttons=[MDFlatButton(text='Ok', on_release=self.close_dialog)]
                                   )
            self.dialog.open()
            # self.label.text = f'Самый короткий путь: {shortest_way}, маршрут: {shortest_way_coords}'
            self.label.text = ', '.join(coords_view)
            self.x.text = ''
            self.y.text = ''

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

            # coords_view.clear()
            # coords.clear()

            # s = serial.Serial("COM4", 9600)
            # shortest_way_coords.append([0, 0])
            # for i in range(len(shortest_way_coords)):
            #     if i != 0:
            #         s.write(bytes(shortest_way_coords[i]))

        else:
            self.dialog = MDDialog(title='Выберите алгоритм решения!',
                                size_hint=(0.4, 0),
                                   buttons=[MDFlatButton(text='Закрыть', on_release=self.close_dialog)]
                                   )
            self.dialog.open()


    def close_dialog(self, obj):
       self.dialog.dismiss()

    def check(self, checkbox, active):
        if active:
            METOD[0] = 1

    def check1(self, checkbox, active):
        if active:
            METOD[0] = 2


if __name__ == "__main__":
    Demo().run()
