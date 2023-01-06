from line_profiler_pycharm import profile

from utils.timeit import timeit


def access(numbers, indexes, i):
    return numbers[i]


@profile
def multi_access(access_nb, numbers, indexes):
    middle = len(numbers) // 2
    for _ in range(access_nb):
        access(numbers, indexes, 0)
        access(numbers, indexes, middle)
        access(numbers, indexes, -1)


@timeit
@profile
def main(access_nb: int, number_nb: int) -> None:

    # ---- Basic
    numbers = list(range(number_nb))
    indexes = list(range(number_nb))
    multi_access(access_nb, numbers, indexes)


    # ---- Numpy
    import numpy as np
    numbers = np.array(range(number_nb))
    indexes = np.array(range(number_nb))
    multi_access(access_nb, numbers, indexes)


if __name__ == '__main__':
    main(int(10e4), 100)
