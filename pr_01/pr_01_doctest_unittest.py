import math as m
import doctest


def bubble_sort(arr):
    """
    Sorts an array of numbers in ascending order


    >>> bubble_sort([])
    []

    >>> bubble_sort([1])
    [1]

    >>> bubble_sort([10, 10, 10, 10])
    [10, 10, 10, 10]

    >>> bubble_sort([9, 99, 999])
    [9, 99, 999]

    >>> bubble_sort([3, 2, 1])
    [1, 2, 3]

    >>> bubble_sort([39, "12", 18, 85, 72, 10, 2, 18])
    Traceback (most recent call last):
        ...
    TypeError: '>' not supported between instances of 'int' and 'str'
    """

    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not swapped:
            break
    return arr
    

if __name__ == '__main__':
    error_msg = "Неверное значение функции сортировки"

    assert bubble_sort([]) == [], error_msg
    assert bubble_sort([1]) == [1], error_msg
    assert bubble_sort([10, 10, 10, 10]) == [10, 10, 10, 10], error_msg
    assert bubble_sort([9, 99, 999]) == [9, 99, 999], error_msg
    assert bubble_sort([3, 2, 1]) == [1, 2, 3], error_msg
    assert bubble_sort([39, 12, 18, 85, 72, 10, 2, 18]) == [2, 10, 12, 18, 18, 39, 72, 85], error_msg

    doctest.testmod()


