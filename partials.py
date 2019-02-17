from functools import partial


def add(a, b):
    return a + b


add_two = partial(add, 2)
print(add_two(10))
