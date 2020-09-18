from collections import deque

parentheses = deque(input())
stack = []
is_valid = True

pairs = {
    "{": "}",
    "(": ")",
    "[": "]"
}

for char in parentheses:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if stack:
            last = stack.pop()
            if pairs[last] != char:
                is_valid = False
                break
        else:
            is_valid = False
            break
if is_valid:
    print("YES")
else:
    print("NO")