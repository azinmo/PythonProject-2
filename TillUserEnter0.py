num = int(input('Enter a number: '))

sum_even = 0
sum_odd = 0

while num != 0:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    num =int(input('Enter a number: '))

print(f'The sum of even numbers is {sum_even}')
print(f'The sum of odd numbers is {sum_odd}')