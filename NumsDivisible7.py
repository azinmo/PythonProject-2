count = 0
sum_num = 0

for i in range(200, 800, 1):
    if i % 7 == 0:
        sum_num += i
        count += 1
        print(i)

print(f'There are {count} numbers divisible by 7')