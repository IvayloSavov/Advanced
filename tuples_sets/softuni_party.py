number_guests = int(input())

all_guests = {input() for _ in range(number_guests)}

while True:
    guest = input()
    if guest == "END":
        break
    if guest in all_guests:
        all_guests.remove(guest) # removing the guest who has come


print(len(all_guests))
[print(v_guest) for v_guest in sorted(all_guests) if v_guest[0].isdigit()]
[print(r_guest) for r_guest in sorted(all_guests) if not r_guest[0].isdigit()]


