
from toolz import compose, pipe, curry
from toolz.sandbox import *


def add(a, b):
    return a + b


def double(a):
    return 2 * a


@curry
def curried_sum(x, y, z):
    return x + y + z


def is_eaten(food, eater):
    return f'({food} is eaten by {eater})'

# compose(*functions)(*args)
# pipe(arg, *functions)
# fold(func, iterator)
