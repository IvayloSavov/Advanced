count_racks = 1
clothes_in_the_box = list(map(int, input().split(" ")))
capacity_of_rack = int(input())

sum_current_rack = 0

while len(clothes_in_the_box) > 0:
    current_clothe = clothes_in_the_box.pop()
    if sum_current_rack + current_clothe < capacity_of_rack:
        sum_current_rack += current_clothe

    elif sum_current_rack + current_clothe == capacity_of_rack and len(clothes_in_the_box) > 0:
        sum_current_rack += current_clothe
        sum_current_rack = 0
        count_racks += 1

    elif sum_current_rack + current_clothe > capacity_of_rack:
        sum_current_rack = 0
        count_racks += 1
        sum_current_rack += current_clothe

print(count_racks)
