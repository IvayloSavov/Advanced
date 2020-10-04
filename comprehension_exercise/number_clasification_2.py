types_dict = {'Positive:': [], 'Negative:': [], 'Even:': [], 'Odd:': []}
numbers = [int(i) for i in input().split(', ')]
[types_dict["Positive:"].append(i) if i >= 0 else types_dict["Negative:"].append(i) for i in numbers]
[types_dict["Even:"].append(i) if i % 2 == 0 else types_dict["Odd:"].append(i) for i in numbers]
for k, v in types_dict.items():
    print(f"{k} {', '.join([str(i) for i in v])}")