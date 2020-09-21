from collections import deque, defaultdict


def time_plus_one_second(h_1, m_1, s_1):
    s_1 = (s_1 + (m_1 * 60) + (h_1 * 3_600)) + 1

    s_1 = s_1 % (24 * 3600)
    h_1 = s_1 // 3_600
    s_1 %= 3_600
    m_1 = s_1 // 60
    s_1 %= 60

    return h_1, m_1, s_1


robot_info = deque(input().split(";"))
free_robots = deque()
official_time = tuple(map(int, input().split(":")))

robots_with_times = defaultdict(int)
busy_robots = defaultdict(int)
products = deque()

for robot in robot_info:
    name, time_robot = robot.split("-")
    robots_with_times[name] = int(time_robot)
    free_robots.append(name)

while True:
    tokens = input()
    if tokens == "End":
        break
    products.append(tokens)

while len(products) > 0:
    h, m, s = official_time
    official_time = time_plus_one_second(h, m, s)
    busy_robots_list = list(busy_robots.keys())

    for r in busy_robots_list:
        busy_robots[r] -= 1
        if busy_robots[r] <= 0:
            free_robots.append(r)
            busy_robots.pop(r)

    current_product = products.popleft()

    if not free_robots:
        products.append(current_product)
        continue

    current_robot = free_robots.popleft()
    busy_robots[current_robot] = robots_with_times[current_robot]
    h, m, s = official_time
    print(f"{current_robot} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")