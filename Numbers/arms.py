# Checking for Armstrong Number

sum = 0  # initialise to an integer value
num = (input('Enter the number:	'))
l = len(num) 	# no. of digits
n = int(num)  # typecast to integer
while n != 0:
    dig = n % 10
    sum = sum+(dig**l)  # each digit raised to total number of digits
    n = n//10
if sum == int(num):
    print(f'{num} is an Armstrong number.')
else:
    print(f'{num} is not an Armstrong number')
