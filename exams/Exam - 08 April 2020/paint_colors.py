from collections import deque

colors = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ['red', 'yellow'], "purple": ['red', 'blue'], "green": ['yellow', 'blue']}
colors_we_have = []

while colors:
    ch_1 = colors.popleft()
    new_color_2 = ""
    ch_2 = ""
    if colors:
        ch_2 = colors.pop()
        new_color = ch_1 + ch_2
        new_color_2 = ch_2 + ch_1
    else:
        new_color = ch_1
    if new_color in main_colors or new_color in secondary_colors.keys():
        colors_we_have.append(new_color)
    elif new_color_2 in main_colors or new_color_2 in secondary_colors.keys():
        colors_we_have.append(new_color_2)
    else:
        middle_index = len(colors) // 2
        ch_1 = ch_1[:-1]
        ch_2 = ch_2[:-1]
        if ch_1:
            colors.insert(middle_index, ch_1)
        if ch_2:
            colors.insert(middle_index, ch_2)


for color in reversed(colors_we_have):
    if color in secondary_colors.keys():
        f_color, s_color = secondary_colors[color]
        if f_color in colors_we_have and s_color in colors_we_have:
            continue
        else:
            colors_we_have.remove(color)

print(colors_we_have)