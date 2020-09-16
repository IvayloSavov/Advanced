from collections import deque

parenthesis = deque(input())
opening_parenthesis = []
balanced = True

for element in parenthesis:
    if element == "(" or element == "[" or element == "{":
        opening_parenthesis.append(element)

    else:
        if len(opening_parenthesis) <= 0:
            balanced = False
            break

        if element == ")":
            if opening_parenthesis.pop() != "(":
                balanced = False
                break

        elif element == "]":
            if opening_parenthesis.pop() != "[":
                balanced = False
                break

        elif element == "}":
            if opening_parenthesis.pop() != "{":
                balanced = False
                break

if not balanced:
    print("NO")
else:
    print("YES")