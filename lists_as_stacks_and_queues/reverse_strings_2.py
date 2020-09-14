stack = list(input())

while len(stack) > 0: # this is better solution than by for loop, tight coupling mistake?
    item = stack.pop()
    print(item, end="")
