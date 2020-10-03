n = list(map(int, input().split()))
neg = sum(list(filter(lambda x: x < 0, n)))
pos = sum(list(filter(lambda x: x >= 0, n)))

print(neg)
print(pos)

if pos > abs(neg):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")

