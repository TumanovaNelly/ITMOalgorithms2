from random import randint
from typing import List, Tuple


def partition(lst: List[int], start: int, end: int, pivot: int) -> Tuple[int, int]:
    end_left = end_mid = start
    for i in range(start, end):
        if lst[i] > pivot:
            lst[i], lst[end_mid], lst[end_left] = lst[end_mid], lst[end_left], lst[i]
            end_left += 1
            end_mid += 1
        elif lst[i] == pivot:
            lst[end_mid], lst[i] = lst[i], lst[end_mid]
            end_mid += 1

    return end_left, end_mid


def quick_max(lst: List[int], number: int, start: int = 0, end: int = -1) -> int:
    if end == -1: end = len(lst)
    if end - start < 1: return lst[number]

    end_left, end_mid = partition(lst, start, end, lst[randint(start, end - 1)])

    if end_left <= number:
        if end_mid <= number:
            return quick_max(lst, number, end_mid, end)
        return lst[number]
    return quick_max(lst, number, start, end_left)
