class ValueCannotBeNegative(Exception):
    pass

def read_values():
    for _ in range(5):
        n = int(input())
        if n < 0:
            raise ValueCannotBeNegative()

try:
    read_values()
except ValueCannotBeNegative:
    print("You entered a negative value which is not allowed")