class Car:
    def __init__(self, reg_num):
        self.reg_num = reg_num


class Parking:
    def __init__(self):
        self.__cars = set()

    def process_car(self, direction, car: Car):
        if direction == "IN":
            self.__cars.add(car)

        elif direction == "OUT" and car in self.__cars:
            self.__cars.remove(car)

    def print_status(self):
        if self.__cars:
            print("\n".join([reg_num for reg_num in self.__cars]))
        else:
            print("Parking Lot is Empty")


parking = Parking()

n = int(input())
for _ in range(n):
    direction, reg_num = input().split(", ")
    car = Car(reg_num)
    parking.process_car(direction, reg_num)

parking.print_status()