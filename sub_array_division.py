n = input()
numbers = list(map(int, input().split(' ')))
d, m =  map(int, input().split(' '))

total_solutions = 0
for i in range(len(numbers) - m + 1):
    tmp = 0
    for j in range(i, i + m):
        tmp += numbers[j]
    if tmp == d:
        total_solutions += 1

print(total_solutions)
