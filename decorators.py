from functools import wraps


def make_bold(func):
    # @wraps(func)
    def func_wrapper(name):
        return '<strong>{}</strong>'.format(func(name))
    return func_wrapper


@make_bold
def say_hello(name):
    return 'Hello, {}'.format(name)
