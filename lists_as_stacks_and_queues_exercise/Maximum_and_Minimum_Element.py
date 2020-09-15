number_of_queries = int(input())
stack = []

for _ in range(number_of_queries):
    query = input()
    if query.startswith("1"):
        num_to_push = int((query.split(" "))[1])
        stack.append(num_to_push)

    elif query.startswith("2") and len(stack) > 0:
        stack.pop()

    elif query.startswith("3") and len(stack) > 0:
        print(max(stack))

    elif query.startswith("4") and len(stack) > 0:
        print(min(stack))

while len(stack) > 0:
    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=", ")

# stack_to_print = []
#
# while len(stack) > 0:
#     stack_to_print.append(str(stack.pop()))
#
# print(", ".join(stack_to_print))
