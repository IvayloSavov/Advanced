from collections import deque

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

colors_we_have = []
string_input = deque(input().split(" "))

while string_input:
    f_element = string_input.popleft()
    s_element = ""
    concatenate = ""
    concatenate_2 = ""
    if string_input:
        s_element = string_input.pop()

    if f_element and s_element:
        concatenate = f_element + s_element
        concatenate_2 = s_element + f_element
    else:
        concatenate = f_element

    if concatenate in main_colors:
        colors_we_have.append(concatenate)

    elif concatenate_2 in main_colors:
        colors_we_have.append(concatenate_2)

    elif concatenate in secondary_colors:
        colors_we_have.append(concatenate)

    elif concatenate_2 in secondary_colors:
        colors_we_have.append(concatenate_2)

    else:
        f_element = deque(f_element)
        f_element.pop()
        if s_element:
            s_element = deque(s_element)
            s_element.pop()

        if f_element and s_element:
            f_element = "".join(f_element)
            s_element = "".join(s_element)
            string_input.insert((len(string_input) // 2), f_element)
            string_input.insert((len(string_input) // 2 + 1), s_element)
        elif f_element and not s_element:
            f_element = "".join(f_element)
            string_input.insert((len(string_input) // 2), f_element)
        elif s_element and not f_element:
            s_element = "".join(s_element)
            string_input.insert((len(string_input) // 2), s_element)

if "orange" in colors_we_have:
    if "red" in colors_we_have and "yellow" in colors_we_have:
        pass
    else:
        colors_we_have.remove("orange")

if "purple" in colors_we_have:
    if "red" in colors_we_have and "blue" in colors_we_have:
        pass
    else:
        colors_we_have.remove("purple")

if "green" in colors_we_have:
    if "yellow" in colors_we_have and "blue" in colors_we_have:
        pass
    else:
        colors_we_have.remove("green")

print(colors_we_have)