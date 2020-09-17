cars_count = int(input())

cars = set()

def get_in_parking(number_plate):
    cars.add(number_plate)


def get_out_of_parking(number_plate):
    if number_plate in cars:
        cars.remove(number_plate)


for _ in range(cars_count):
    tokens = input().split(", ")
    direction, number_plate = tokens
    operations = {
        "IN": get_in_parking, # все още не искам да я извикваме затова не слагаме овалните скоби
        "OUT": get_out_of_parking,
    }
    operations[direction](number_plate)
    # fn = operations[direction]
    # fn(number_plate)

if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")