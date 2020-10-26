jobs = list(map(int, input().split(", ")))
index = int(input())
my_task_priority = jobs.pop(index)
sum_jobs = my_task_priority

for n in jobs:
    if n <= my_task_priority:
        sum_jobs += n

print(sum_jobs)