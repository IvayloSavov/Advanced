number_of_queries = int(input())
stack = []

for _ in range(number_of_queries):
    query = input().split()
    command = int(query[0])
    if command == 1:
        num_to_push = int(query[1])
        stack.append(num_to_push)

    elif command == 2 and len(stack) > 0:
        stack.pop()

    elif command == 3 and len(stack) > 0:
        print(max(stack))

    elif command == 4 and len(stack) > 0:
        print(min(stack))

print(", ".join([str(x) for x in reversed(stack)]))
