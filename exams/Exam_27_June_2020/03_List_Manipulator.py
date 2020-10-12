def list_manipulator(numbers, *args):
    if args[0] == "add" and args[1] == "beginning":
        numbers = [*args[2:]] + numbers
        return numbers

    elif args[0] == "add" and args[1] == "end":
        numbers = numbers + [*args[2:]]
        return numbers

    elif args[0] == "remove" and args[1] == "beginning":
        try:
            i = args[2]
            return numbers[i:]
        except IndexError:
            return numbers[1:]

    elif args[0] == "remove" and args[1] == "end":
        try:
            i = args[2]
            return numbers[:-i]
        except IndexError:
            return numbers[:-1]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
