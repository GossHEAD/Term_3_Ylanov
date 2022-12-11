# -*- coding: cp1251 -*-
import time


class result:
    comparisons = 0
    permutations = 0
    time = 0
    array = []
    sort_type = ""


def bubble_sort(res):
    res.sort_type = "сортировка пузырьком"
    start_time = time.monotonic_ns()
    for i in range(len(res.array) - 1):
        is_changed = 0
        for j in range(len(res.array) - i - 1):
            res.comparisons += 1
            if res.array[j] > res.array[j + 1]:
                buff = res.array[j]
                res.array[j] = res.array[j + 1]
                res.array[j + 1] = buff
                res.permutations += 1
                is_changed = 1
        if is_changed == 0:
            break
    res.time = (time.monotonic_ns() - start_time) // 1000000


def selection_sort(res):
    res.sort_type = "сортировка выбором"
    start_time = time.monotonic_ns()
    for i in range(0, len(res.array) - 1):
        smallest = i
        for j in range(i + 1, len(res.array)):
            res.comparisons += 1
            if res.array[j] < res.array[smallest]:
                smallest = j
        if res.array[smallest] != res.array[i]:
            res.array[i], res.array[smallest] = res.array[smallest], res.array[i]
            res.permutations += 1
    res.time = (time.monotonic_ns() - start_time) // 1000000


def insertion_sort(res):
    res.sort_type = "сортировка вставкой"
    start_time = time.monotonic_ns()
    for i in range(1, len(res.array)):
        temp = res.array[i]
        j = i - 1
        while j >= 0 and temp < res.array[j]:
            res.comparisons += 1
            res.array[j + 1] = res.array[j]
            j = j - 1
        if j >= 0:
            res.comparisons += 1
        if res.array[j + 1] != temp:
            res.array[j + 1] = temp
            res.permutations += 1
    res.time = (time.monotonic_ns() - start_time) // 1000000


def quick_sort(start, end, res):
    res.sort_type = "быстрая сортировка"
    start_time = time.monotonic_ns()
    quicksort(start, end, res)
    res.time = (time.monotonic_ns() - start_time) // 1000000


def quicksort(start, end, res):
    """Sorts the list from indexes start to end - 1 inclusive."""
    if end - start > 1:
        p = partition(start, end, res)
        quicksort(start, p, res)
        quicksort(p + 1, end, res)


def partition(start, end, res):
    pivot = res.array[start]
    i = start + 1
    j = end - 1

    while True:
        res.comparisons += 1
        while i <= j and res.array[i] <= pivot:
            i += 1
        res.comparisons += 1
        while i <= j and res.array[j] >= pivot:
            j -= 1

        if i <= j:
            res.array[i], res.array[j] = res.array[j], res.array[i]
            res.permutations += 1
        else:
            res.array[start], res.array[j] = res.array[j], res.array[start]
            res.permutations += 1
            return j
