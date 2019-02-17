def rock_paper_scissor():
    """
    simple generator
    """
    yield 'rock'

    yield 'paper'

    yield 'scissor'


def infinite_generator():
    """
    generator with a loop
    """
    i = 0
    while True:
        yield i
        i += 1


"""
Generator expression
"""
thousand = list(range(1000))
gen = (num * 2 for num in thousand)
