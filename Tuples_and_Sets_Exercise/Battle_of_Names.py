num_lines = int(input())

set_even = set()
set_odd = set()

for i in range(num_lines):
    sum_chars = sum(map(ord, input()))
    div = sum_chars // (i + 1)

    if div % 2 == 0:
        set_even.add(div)
    else:
        set_odd.add(div)

sum_even = sum(set_even)
sum_odd = sum(set_odd)

list_even = list(map(str, set_even))
list_odd = list(map(str, set_odd))

if sum_even == sum_odd:
    list_output = list(map(str, set_even | set_odd))
    print(", ".join(list_output))
elif sum_odd > sum_even:
    list_output = list(map(str, set_even - set_odd))
    print(", ".join(list_output))
else:
    list_output = list(map(str, set_even ^ set_odd))
    print(", ".join(list_output))

# Solving from colleague
# number = int(input())
# char_sum = 0
#
# even_nums = set()
# odd_nums = set()
#
# for num in range(1, number + 1):
#     name = input()
#     char_sum = 0
#     for char in name:
#         char_sum += ord(char)
#
#     devised_num = char_sum // num
#     if devised_num % 2 == 0:
#         even_nums.add(devised_num)
#     else:
#         odd_nums.add(devised_num)
#
# even_nums_sum = sum(even_nums)
# odd_nums_sum = sum(odd_nums)
#
# if even_nums_sum == odd_nums_sum:
#     union_values = set(even_nums | odd_nums)
#     union_values = [str(x) for x in union_values]
#     print(f"{', '.join(union_values)}")
# elif odd_nums_sum > even_nums_sum:
#     different = set(odd_nums - even_nums)
#     different = [str(x) for x in different]
#     print(f"{', '.join(different)}")
# elif even_nums_sum > odd_nums_sum:
#     symmetric_different = set(even_nums ^ odd_nums)
#     symmetric_different = [str(x) for x in symmetric_different]
#     print(f"{', '.join(symmetric_different)}")