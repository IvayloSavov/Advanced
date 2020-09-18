def creating_phone_book():

    phone_book_def = {}

    while True:
        tokens = input()
        if tokens.isdecimal():
            times_to_search_def = int(tokens)
            break
        name, number = tokens.split("-")

        if name not in phone_book_def.keys():
            phone_book_def[name] = ""
        phone_book_def[name] = number

    return phone_book_def, times_to_search_def


def printing_searched_contacts(phone_book_dict, count_contacts):
    for _ in range(count_contacts):
        searched_contact = input()
        if searched_contact not in phone_book_dict.keys():
            print(f"Contact {searched_contact} does not exist.")
            continue

        print(f"{searched_contact} -> {phone_book_dict[searched_contact]}")


phone_book, times_to_search = creating_phone_book()
printing_searched_contacts(phone_book, times_to_search)