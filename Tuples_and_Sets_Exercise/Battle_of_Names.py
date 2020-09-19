def even_odd_numbers(count_n):

    even_numbers = set()
    odd_numbers = set()

    for i in range(1, count_n + 1):
        name_sum = sum(tuple(map(lambda ch: ord(ch), input())))
        v = name_sum // i
        if v % 2 == 0:
            even_numbers.add(v)
        else:
            odd_numbers.add(v)

    return even_numbers, odd_numbers


def operation(even_number: set, odd_number: set):

    result = set()

    if sum(even_number) == sum(odd_number):
        result = odd_number.union(even_number)
    elif sum(odd_number) > sum(even_number):
        result = odd_number.difference(even_number)
    elif sum(even_number) > sum(odd_number):
        result = odd_number.symmetric_difference(even_number)

    return result


def printing_the_result(res):
    print(", ".join(tuple(map(str, res))))


n = int(input())
even_numbers, odd_numbers = even_odd_numbers(n)
printing_the_result(operation(even_numbers, odd_numbers))
