def input_to_list(count):

    all_guests = set()

    for _ in range(count):
        guest = input()
        all_guests.add(guest)

    return all_guests


def guest_who_came_to_the_party(command, all_guests):

    while True:
        token = input()
        if token == command:
            break
        if token in all_guests:
            all_guests.remove(token) # removing the people who have been at the party

    return all_guests


def print_result(people_at_party):
    print(len(people_at_party))
    [print(guest) for guest in sorted(people_at_party) if guest[0].isdecimal()]
    [print(guest) for guest in sorted(people_at_party) if not guest[0].isdecimal()]


number_guests = int(input())
invited_people = input_to_list(number_guests)
people_at_party = sorted(guest_who_came_to_the_party("END", invited_people))
print_result(people_at_party)
