num_lines = int(input())

unique_elements = set()

for _ in range(num_lines):
    line_elements = set(input().split(' '))
    unique_elements.update(line_elements)

print('\n'.join(unique_elements))