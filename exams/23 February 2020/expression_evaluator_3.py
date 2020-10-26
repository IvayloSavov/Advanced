
import operator
import collections
from math import floor

expression = collections.deque(input().split())
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}

numbers = []
while expression:
    current_el = expression.popleft()
    if current_el in operators.keys():
        res = eval(current_el.join(numbers))
        numbers.clear()
        numbers.append(str(floor(res)))
    else:
        numbers.append(current_el)

print(*numbers)