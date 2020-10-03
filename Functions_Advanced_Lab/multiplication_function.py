import operator
from math import prod
from functools import reduce


multiply = lambda *args: reduce(lambda a, b: a * b, args)


# def multiply(*args):
#     return reduce(operator.mul, args)
#
# multiply = lambda *args: prod(args)


