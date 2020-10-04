command = input()
numbers = list(map(int, input().split()))

if command == "Odd":
    odd = list(filter(lambda x: x % 2 != 0, numbers))  # тук няма нужда от list
    print(sum(odd) * len(numbers))
else:
    even = list(filter(lambda x: x % 2 == 0, numbers))
    print(sum(even) * len(numbers))
