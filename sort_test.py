# -*- coding: cp1251 -*-
from random import randint 
from sort import *
 
def test():
    res = []
    array = []
    for i in range(3):
        array.append(randint(1, 99))
    print("Исходный массив:", array)
    for i in range(4):
        res.append(result())
        res[i].array = array.copy()
    bubble_sort(res[0]);
    selection_sort(res[1]);
    insertion_sort(res[2]);
    quick_sort(0, len(res[3].array), res[3]);
    print("\nСортировка пузырьком:\nПолученный массив:", res[0].array, "\nколичество сравнений:", res[0].comparisons,
          "\nколичество перестановок:", res[0].permutations)
    print("\nСортировка выбором:\nПолученный массив:", res[1].array,
         "\nколичество сравнений:", res[1].comparisons, "\nколичество перестановок:", res[1].permutations)
    print("\nСортировка вставкой:\nПолученный массив:", res[2].array,
         "\nколичество сравнений:", res[2].comparisons, "\nколичество перестановок:", res[2].permutations)
    print("\nБыстрая сортировка:\nПолученный массив:", res[3].array,
         "\nколичество сравнений:", res[3].comparisons, "\nколичество перестановок:", res[3].permutations)