# -*- coding: cp1251 -*-
from random import randint 
from sort import *
 
def test():
    res = []
    array = []
    for i in range(3):
        array.append(randint(1, 99))
    print("�������� ������:", array)
    for i in range(4):
        res.append(result())
        res[i].array = array.copy()
    bubble_sort(res[0]);
    selection_sort(res[1]);
    insertion_sort(res[2]);
    quick_sort(0, len(res[3].array), res[3]);
    print("\n���������� ���������:\n���������� ������:", res[0].array, "\n���������� ���������:", res[0].comparisons,
          "\n���������� ������������:", res[0].permutations)
    print("\n���������� �������:\n���������� ������:", res[1].array,
         "\n���������� ���������:", res[1].comparisons, "\n���������� ������������:", res[1].permutations)
    print("\n���������� ��������:\n���������� ������:", res[2].array,
         "\n���������� ���������:", res[2].comparisons, "\n���������� ������������:", res[2].permutations)
    print("\n������� ����������:\n���������� ������:", res[3].array,
         "\n���������� ���������:", res[3].comparisons, "\n���������� ������������:", res[3].permutations)