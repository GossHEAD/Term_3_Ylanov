# -*- coding: cp1251 -*-
from kivy.app import App

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
#from kivymd
Builder.load_file('main.kv')

import random
from sort import *
from data_analysis import *


Window.size = {800, 380}
Window.clearcolor = (0.6, 0.6, 0.6, 1)

Config.set('kivy', 'keyboard_mode', 'systemanddock')


class StartPage(Screen):
    def start(self):
        #ep = self.ids.screen2
        text_int = int(self.text_input_count.text)
        frst_int = int(self.text_input_st.text)
        scnd_int = int(self.text_input_ed.text)
        choose_item = str(self.spin.text)
        if choose_item == "Chaos":
            array_b = [randint(frst_int, scnd_int) for i in range(text_int)]
            #sorts_analysis(text_int, frst_int, scnd_int, choose_item, array_b)
            main_array = [[result() for i in range(4)] for j in range(4)]
            get_data(main_array[0], array_b)
            self.time_bubble.text = str(main_array[0][0].time ) + "мс"
            self.time_quick.text = str(main_array[0][3].time) + "мс"
            self.time_insert.text = str(main_array[0][2].time) + "мс"
            self.time_select.text = str(main_array[0][1].time) + "мс"

            self.coc_bubble.text = str(main_array[0][0].comparisons) + "ч/c"
            self.coc_quick.text = str(main_array[0][3].comparisons) + "ч/c"
            self.coc_insert.text = str(main_array[0][2].comparisons) + "ч/c"
            self.coc_select.text = str(main_array[0][1].comparisons) + "ч/c"

            self.coch_bubble.text = str(main_array[0][0].permutations)+ "ч/п"
            self.coch_quick.text = str(main_array[0][3].permutations)+ "ч/п"
            self.coch_insert.text = str(main_array[0][2].permutations)+ "ч/п"
            self.coch_select.text = str(main_array[0][1].permutations)+ "ч/п"

        if choose_item == "Sorted":
            array_b = [randint(frst_int, scnd_int) for i in range(text_int)]
            #sorts_analysis(text_int, frst_int, scnd_int, choose_item, array_b)
            main_array = [[result() for i in range(4)] for j in range(4)]
            get_data(main_array[1], array_b)
            self.time_bubble.text = str(main_array[1][0].time) + "мс"
            self.time_quick.text = str(main_array[1][3].time) + "мс"
            self.time_insert.text = str(main_array[1][2].time) + "мс"
            self.time_select.text = str(main_array[1][1].time) + "мс"

            self.coc_bubble.text = str(main_array[1][0].comparisons)+ "ч/c"
            self.coc_quick.text = str(main_array[1][3].comparisons)+ "ч/c"
            self.coc_insert.text = str(main_array[1][2].comparisons)+ "ч/c"
            self.coc_select.text = str(main_array[1][1].comparisons)+ "ч/c"

            self.coch_bubble.text = str(main_array[1][0].permutations) + "ч/п"
            self.coch_quick.text = str(main_array[1][3].permutations) + "ч/п"
            self.coch_insert.text = str(main_array[1][2].permutations) + "ч/п"
            self.coch_select.text = str(main_array[1][1].permutations) + "ч/п"
        if choose_item == "Reversed":
            array_b = [randint(frst_int, scnd_int) for i in range(text_int)]
            #sorts_analysis(text_int, frst_int, scnd_int, choose_item, array_b)
            main_array = [[result() for i in range(4)] for j in range(4)]
            get_data(main_array[2], array_b)
            self.time_bubble.text = str(main_array[2][0].time) + "мс"
            self.time_quick.text = str(main_array[2][3].time) + "мс"
            self.time_insert.text = str(main_array[2][2].time) + "мс"
            self.time_select.text = str(main_array[2][1].time)+ "мс"

            self.coc_bubble.text = str(main_array[2][0].comparisons)+ "ч/c"
            self.coc_quick.text = str(main_array[2][3].comparisons)+ "ч/c"
            self.coc_insert.text = str(main_array[2][2].comparisons)+ "ч/c"
            self.coc_select.text = str(main_array[2][1].comparisons)+ "ч/c"

            self.coch_bubble.text = str(main_array[2][0].permutations) + "ч/п"
            self.coch_quick.text = str(main_array[2][3].permutations) + "ч/п"
            self.coch_insert.text = str(main_array[2][2].permutations) + "ч/п"
            self.coch_select.text = str(main_array[2][1].permutations) + "ч/п"
        if choose_item == "Half-Sorted":
            array_b = [randint(frst_int, scnd_int) for i in range(text_int // 2)]
            #sorts_analysis(text_int, frst_int, scnd_int, choose_item, array_b)
            main_array = [[result() for i in range(4)] for j in range(4)]
            get_data(main_array[3], array_b)
            self.time_bubble.text = str(main_array[3][0].time) + "мс"
            self.time_quick.text = str(main_array[3][3].time) + "мс"
            self.time_insert.text = str(main_array[3][2].time) + "мс"
            self.time_select.text = str(main_array[3][1].time) + "мс"

            self.coc_bubble.text = str(main_array[3][0].comparisons) + "ч/с"
            self.coc_quick.text = str(main_array[3][3].comparisons)+ "ч/с"
            self.coc_insert.text = str(main_array[3][2].comparisons) + "ч/с"
            self.coc_select.text = str(main_array[3][1].comparisons) + "ч/с"

            self.coch_bubble.text = str(main_array[3][0].permutations) + "ч/п"
            self.coch_quick.text = str(main_array[3][3].permutations) + "ч/п"
            self.coch_insert.text = str(main_array[3][2].permutations) + "ч/п"
            self.coch_select.text = str(main_array[3][1].permutations) + "ч/п"


class EffectivePage(Screen):
    #bible = StartPage()
    #bible.bible_func()
    pass


class ScreenManagment(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return ScreenManagment()


if __name__ == "__main__":
    app = MainApp()
    app.run()
