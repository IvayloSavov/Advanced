def numbers_searching(*args):
    start_n = min(args)
    end_n = max(args)
    correct_numbers = set(range(start_n, end_n + 1))
    missing_number = correct_numbers.difference(set(args))
    dublicate_numbers = set()

    for n in correct_numbers:
        if args.count(n) > 1:
            dublicate_numbers.add(n)

    return [*missing_number, sorted(dublicate_numbers)]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

