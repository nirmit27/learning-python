# (Driver code)
from lib import Library as lib

l1 = lib()

while True:
    try:
        ch = input(f'''
            \n{"MAIN MENU".center(33)} \n\n    [1] Display all books\n    [2] Find a book\n    [3] Exit\n\n{"Enter your choice".rjust(23)} : ''')

        match ch:
            case '1':
                print(f"\n{'-'*33}\n")
                l1.show()
                print(f"\n{'-'*33}\n")
            case '2':
                print(f"\n{'-'*33}\n")
                book = input(" Book : ")
                author = input(" Author : ")
                l1.find(book,author)
                print(f"\n{'-'*33}\n")
            case '3':
                print(f"\n{'-'*33}\n\n{'Goodbye!'.center(33)}\n\n{'-'*33}\n")
                break
            case _:
                print(f"\n{'-'*33}")
                raise ValueError('\n  Please select a valid option.\n')

    except ValueError as v:
        print(v)
        print(f"{'-'*33}")
