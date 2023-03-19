# Inverted Pyramid 

def triangle(n):
    for i in range(n):
        if i < (n//2):
            for j in range(i+1):
                print('* ', end='')
            print()
        else:
            for k in range(n, i, -1):
                print('* ', end='')
            print()


if __name__ == "__main__":
    rows = int(input("\n Enter the number of rows : "))

    print("\n The required pattern is as follows : \n")

    triangle(rows)

# *
# * *
# * * *
# * * * *
# * * *
# * *
# *