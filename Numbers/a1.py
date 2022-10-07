# Accepting an input from the user
num = int(input("Enter any number: "))

def OddOrEven(num):
    if num%2==0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number")

OddOrEven(num)