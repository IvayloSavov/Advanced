import math

n = float(input())
base = input()

if base == "natural":
    print(f"{math.log(n):.2f}")
else:
    print(f"{math.log(n, float(base)):2f}")