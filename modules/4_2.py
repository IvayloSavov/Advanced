from math_ops import parser, executor

expr = input()
res = executor.exec(*parser.parse_exr(expr))
print(res)