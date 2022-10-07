def factorial(*args):
    f=1
    #print(type(args))
    for x in args:
        f*=x
    return f
print(f"Factorial of {5} is = {factorial(1,2,3,4,5)}")

op = input("Enter the operation: ")
n1 = int(input("Enter the first value: "))
n2 = int(input("Enter the second value: "))
def calc(op,n1,n2):
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='*':
        return n1*n2
    elif op=='//':
        return n1//n2
    else:
        print("\nEnter the valid operation.\n")
print(f"{n1} {op} {n2} = {calc(op,n1,n2)}")
