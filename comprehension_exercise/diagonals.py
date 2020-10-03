n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][n - 1 - i] for i in range(n)]

print(f"First diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Second diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")
