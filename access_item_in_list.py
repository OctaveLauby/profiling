from line_profiler_pycharm import profile

from utils.timeit import timeit


@timeit(display=True)
@profile
def multi_access(access_nb, numbers):
    middle = len(numbers) // 2
    for _ in range(access_nb):
        numbers[0]
        numbers[middle]
        numbers[-1]


@timeit
@profile
def main(access_nb: int, number_nb: int) -> None:

    # ---- Basic
    numbers = list(range(number_nb))
    multi_access(access_nb, numbers)


    # ---- Numpy
    import numpy as np
    numbers = np.array(range(number_nb))
    multi_access(access_nb, numbers)


if __name__ == '__main__':
    main(int(10e4), 100)
