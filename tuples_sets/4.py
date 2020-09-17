cars_count = int(input())

cars = set()

for _ in range(cars_count):
    tokens = input().split(", ")
    direction, number_plate = tokens
    operations = {
        "IN": cars.add,
        "OUT": cars.remove
    }
    operations[direction](number_plate)
    
if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")