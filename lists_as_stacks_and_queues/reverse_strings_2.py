stack = list(input())

while len(stack) > 0: # this is better solution than by for loop type cappaning mistake?
    item = stack.pop()
    print(item, end="")
