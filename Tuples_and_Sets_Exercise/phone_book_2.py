is_finished = False

num_names = 0

address_book = {}

while not is_finished:
    next_input = input()

    try:
        num_names = int(input())
        is_finished = True
    except ValueError:
        name, phone = tuple(next_input.split("-"))
        address_book[name] = phone

for i in range(num_names):
    name_to_check = input()
    if name_to_check not in address_book.keys():
        print(f"Contact {name_to_check} does not exist.")
    else:
        print(f"{name_to_check} -> {address_book[name_to_check]}")