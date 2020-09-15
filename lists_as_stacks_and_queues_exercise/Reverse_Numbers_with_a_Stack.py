def reverse_numbers(list_with_int):
    for n in list_with_int:
        stack.append(n)

    while len(stack) > 0:
        print(stack.pop(), end=" ")


list_with_numbers = list(input().split(" "))
stack = []

reverse_numbers(list_with_numbers)
