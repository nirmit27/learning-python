# Program to check for Palindrome strings
st = input("Enter the string to be checked: ")
if(st==st[::-1]):
    print(st+" is a Palindrome string.")
else:
    print(st+" is not a Palindrome string.")

# String slicing is done via [start_index:stop_index:step_value].