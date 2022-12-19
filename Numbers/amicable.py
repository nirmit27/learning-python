# Program to check whether two numbers are Amicable or not.

a = int(input("\n Enter the first number : "))
b = int(input("\n Enter the second number : "))

def amicable(x):
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum+=i
    return sum

if (amicable(a)==b and amicable(b)==a):
    print(f"\n {a} and {b} are amicable numbers.\n")
else:
    print(f"\n {a} and {b} are not amicable numbers.\n")