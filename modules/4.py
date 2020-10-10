import mathops

expr = input()
res = mathops.exec(*mathops.parse_exr(expr))
print(res)