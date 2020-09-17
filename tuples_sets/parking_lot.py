parking_lot = set()

command_count = int(input())

for _ in range(command_count):
    (command, car) = input().split(", ")
    if command == "IN":
        parking_lot.add(car)
    else:
        if car in parking_lot:
            parking_lot.remove(car)

if len(parking_lot) > 0:
    [print(car) for car in parking_lot]
else:
    print("Parking Lot is Empty")