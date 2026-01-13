"""
sorting.py - реализация шейкерной сортировки
"""


def shaker_sort(arr, key=lambda x: x, reverse=False):
    """
    Сортирует список с использованием шейкерной сортировки.
    """
    n = len(arr)
    if n <= 1:
        return arr[:]

    result = arr[:]
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Проход слева направо
        for i in range(start, end):
            current_key = key(result[i])
            next_key = key(result[i + 1])
            should_swap = (current_key > next_key) if not reverse else (current_key < next_key)

            if should_swap:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # Проход справа налево
        for i in range(end - 1, start - 1, -1):
            current_key = key(result[i])
            next_key = key(result[i + 1])
            should_swap = (current_key > next_key) if not reverse else (current_key < next_key)

            if should_swap:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True

        start += 1

    return result
