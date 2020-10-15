import operator
from functools import reduce
from collections import deque

string_expression = deque(input().split(" "))
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}

current_numbers = []
while string_expression:
    current_element = string_expression.popleft()
    if current_element in operators:
        cur_res = reduce(operators[current_element], current_numbers)
        current_numbers.clear()
        current_numbers.append(cur_res)
    else:
        current_numbers.append(int(current_element))

print(*current_numbers)