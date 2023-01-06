import atexit
from functools import wraps, partial
from time import time
from typing import Callable

TIMEIT_CACHE = {}


@atexit.register
def display_timeit_cache():
    """Display timed function at exit"""
    if not TIMEIT_CACHE:
        return

    sorted_cache = {
        key: value for key, value in sorted(
            TIMEIT_CACHE.items(),
            key=lambda item: item[1]['total_time'],
            reverse=True,
        )
    }
    max_name_size = max(len(name) for name in sorted_cache)

    print()
    print('Time Spent in functions:')
    for name, metrics in sorted_cache.items():
        try:
            meantime = metrics['total_time'] / metrics['calls']
        except ZeroDivisionError:
            meantime = None
        print('> {name}:  {total_time:.5f}s [mean={meantime:.5f}s] | called {calls} time(s) [{fails} fail(s)]'.format(
            name=name.ljust(max_name_size),
            meantime=meantime,
            **metrics,
        ))


def timeit(func: Callable = None, name: str = None, display: bool = False) -> Callable:
    """Decorator to track func calls and time spent"""
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
