n = int(input())
a = [list(input()) for _ in range(n)]
burrows = []

for i in range(n):
    for j in range(n):
        if a[i][j] == 'S':
            x = i
            y = j
        elif a[i][j] == 'B':
            burrows.append((i, j))

food_quantity = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
while True:
    movement = input()
    a[x][y] = '.'
    x += directions[movement][0]
    y += directions[movement][1]
    if not (0 <= x < n and 0 <= y < n):
        print('Game over!')
        break
    if a[x][y] == '*':
        food_quantity += 1
        a[x][y] = 'S'
        if food_quantity >= 10:
            print('You won! You fed the snake.')
            break
    elif a[x][y] == 'B':
        burrows.remove((x, y))
        a[x][y] = '.'
        x, y = burrows[0]
        a[x][y] = 'S'

print(f'Food eaten: {food_quantity}')
[print(''.join(row)) for row in a]