import atexit
from functools import wraps, partial
from time import time
from typing import Callable

TIMEIT_CACHE = {}


def display_timeit_cache():
    if not TIMEIT_CACHE:
        return
    print()
    print('Time Spent in functions:')
    for name, metrics in TIMEIT_CACHE.items():
        print('> {name}:  {total_time}s | called {calls} time(s) [{fails} fail(s)]'.format(name=name, **metrics))


def timeit(func: Callable = None, name: str = None, display: bool = False) -> Callable:
    if func is None:
        return partial(timeit, name=name, display=display)

    name = func.__name__ if name is None else name
    TIMEIT_CACHE[name] = {
        'calls': 0,
        'fails': 0,
        'total_time': 0,
    }

    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time()
        try:
            res = func(*args, **kwargs)
        except Exception:
            TIMEIT_CACHE[name]['fails'] += 1
        finally:
            time_spent = time() - start
            TIMEIT_CACHE[name]['total_time'] += time_spent
            TIMEIT_CACHE[name]['calls'] += 1
            if display:
                print(f'{name} took {time_spent}s')
        return res
    return wrapped


atexit.register(display_timeit_cache)
