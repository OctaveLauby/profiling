from line_profiler_pycharm import profile

from access_item_in_list import multi_access
from utils.timeit import timeit


def cross_access(numbers, indexes, i):
    return numbers[indexes[i]]


@timeit(display=True)
@profile
def multi_cross_access(access_nb, numbers, indexes):
    middle = len(numbers) // 2
    for _ in range(access_nb):
        cross_access(numbers, indexes, 0)
        cross_access(numbers, indexes, middle)
        cross_access(numbers, indexes, -1)


@timeit
@profile
def main(access_nb: int, number_nb: int) -> None:

    # ---- Basic
    numbers = list(range(number_nb))
    indexes = list(range(number_nb))
    multi_cross_access(access_nb, numbers, indexes)


    # ---- Numpy
    import numpy as np
    numbers = np.array(range(number_nb))
    indexes = np.array(range(number_nb))
    multi_cross_access(access_nb, numbers, indexes)

    # ---- Elaborate
    class IntPointer:
        __slots__ = ('value',)

        def __init__(self, value: int):
            self.value = value

    numbers = [IntPointer(i) for i in range(number_nb)]
    multi_access(access_nb, numbers)



if __name__ == '__main__':
    main(int(10e4), 100)
