start = int(input())
end = int(input())
result = [
    n
    for n in range(start, end + 1)
    if any([n % m == 0 for m in range(2, 11)])
]
print(result)

# start_inp = int(input())
# end_inp = int(input())
# list_filter = set(x for i in range(2, 10 + 1)for x in range(start_inp, end_inp + 1) if x % i == 0)
# print(list(list_filter))

# print([x for x in range(int(input()), int(input()) + 1) if any([x % n == 0 for n in range(2, 11)])])