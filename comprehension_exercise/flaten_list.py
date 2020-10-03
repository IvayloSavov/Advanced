
# result = [[el for el in x.split(" ") if el != ""] for x in line.split("|")[::-1]] # така ще го върне като лист в листа
line = input()
result = [el for x in line.split("|")[::-1] for el in x.split(" ") if el != ""] # а така ще го върне като един лист
print(" ".join(result))