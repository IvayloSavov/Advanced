def numbers_searching(*args):
    all_numbers = set(range(min(args), max(args) + 1))
    missing_number = sum(all_numbers) - sum(set(args))
    duplicates = {n for i, n in enumerate(args) if n in args[i+1:]}

    return [missing_number, sorted(duplicates)]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
