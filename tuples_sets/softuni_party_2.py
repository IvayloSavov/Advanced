number_guests = int(input())

all_guests = {input() for _ in range(number_guests)}

attended = set()

while True:
    guest = input()
    if guest == "END":
        break
    attended.add(guest)

unattended = all_guests - attended
print(len(unattended))
print("\n".join(sorted(unattended)))



