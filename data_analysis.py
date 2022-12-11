# -*- coding: cp1251 -*-
# from email.policy import default
from random import randint
from collections import defaultdict
from sort import *


def output_result(res):
    for i in range(len(res)):
        # res[i].time = res[i].time.copy()
        print("\n", res[i].sort_type, "\nЧисло сравнений:", res[i].comparisons,
        "\nЧисло перестановок:", res[i].permutations, "\nВремя: (мс)", res[i].time)

    print("\nЭффективность выполнения сортировки массива(от самого эффективного к худшему):\n")
    res.sort(key=lambda res: res.time * 0.05 + res.permutations * 0.2 + res.comparisons)
    for i in range(4):
        print(i + 1, res[i].sort_type)


def get_data(res, array):
    for i in range(4):
        res[i].array = array.copy()
    bubble_sort(res[0])
    selection_sort(res[1])
    insertion_sort(res[2])
    quick_sort(0, len(res[3].array), res[3])


def halfsorted_array_analysis(array_size, halfsorted_result, first_item, second_item, array):
    #array = [randint(first_item, second_item) for i in range(array_size // 2)]
    array.sort()
    for i in range(array_size - array_size // 2):
        array.append(randint(first_item, second_item))
    get_data(halfsorted_result, array)
    print("\nТестирование на частично упорядоченном массиве из", array_size, "элементов")
    output_result(halfsorted_result)


def reversed_array_analysis(array_size, reversed_result, first_item, second_item, array):
    #array = [randint(first_item, second_item) for i in range(array_size)]
    array.sort(reverse=True)
    get_data(reversed_result, array)
    print("\nТестирование на обратно упорядоченном массиве из", array_size, "элементов")
    output_result(reversed_result)


def sorted_array_analysis(array_size, sorted_result, first_item, second_item, array):
    #array = [randint(first_item, second_item) for i in range(array_size)]
    array.sort()
    get_data(sorted_result, array)
    print("\nТестирование на упорядоченном массиве из", array_size, "элементов")
    output_result(sorted_result)


def chaos_array_analysis(array_size, chaos_result, first_item, second_item, array):
    get_data(chaos_result, array)
    print("\nТестирование на случайном массиве из", array_size, "элементов")
    output_result(chaos_result)


def sorts_analysis(array_size, first_item, second_item, choose_item, array):
    res = [[result() for i in range(4)] for j in range(4)]
    if choose_item == "Chaos":
        chaos_array_analysis(array_size, res[0], first_item, second_item, array)
    elif choose_item == "Sorted":
        sorted_array_analysis(array_size, res[1], first_item, second_item, array)
    elif choose_item == "Reversed":
        reversed_array_analysis(array_size, res[2], first_item, second_item, array)
    elif choose_item == "Half-Sorted":
        halfsorted_array_analysis(array_size, res[3], first_item, second_item, array)
    d = defaultdict(int)
    if (choose_item == "All"):
        chaos_array_analysis(array_size, res[0], first_item, second_item)
        sorted_array_analysis(array_size, res[1], first_item, second_item)
        reversed_array_analysis(array_size, res[2], first_item, second_item)
        halfsorted_array_analysis(array_size, res[3], first_item, second_item)

    for i in range(4):
        for j in range(4):
            d.setdefault(res[i][j].sort_type, []).append(j + 1)
    analysis_result = sorted(d.keys(), key=lambda key: sum(d[key]))
    print("\nЭффективность выполнения сортировки в общем случае (от лучшего к худшему):")
    for i in range(4):
        print(i + 1, analysis_result[i])

    # return x
