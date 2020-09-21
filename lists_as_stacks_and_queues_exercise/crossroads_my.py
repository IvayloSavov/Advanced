from collections import deque

duration_green_light = int(input())
duration_free_window = int(input())
is_crash = False
cars = deque()
total_cars = 0

while True:
    tokens = input()

    if tokens == "END":
        break

    if tokens == "green":
        if cars:
            current_car = deque(cars.popleft())
            car_to_print = "".join(current_car)

            for _ in range(duration_green_light):

                # current_car.popleft() ако е тук Judge ми дава 71/100

                if not current_car:
                    if cars:
                        current_car = deque(cars.popleft())
                        car_to_print = "".join(current_car)
                    else:
                        break

                current_car.popleft() # ако е тук ми дава 100/100.

            if current_car:
                for _ in range(duration_free_window):
                    if current_car:
                        current_car.popleft()

                if current_car:
                    print("A crash happened!")
                    print(f"{car_to_print} was hit at {current_car.popleft()}.")
                    is_crash = True
                    break

    else:
        cars.append(tokens)
        total_cars += 1

if not is_crash:
    print("Everyone is safe.")
    print(f"{total_cars - len(cars)} total cars passed the crossroads.")
