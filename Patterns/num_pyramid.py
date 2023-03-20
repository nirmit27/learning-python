# Number pyramid

rows = int(input("\n Enter the number of rows : "))

for i in range(1, rows + 1):
    j = i
    k = 2
    sp = rows
    while (1):
        if sp >= i:
            print('  ', end='')
            sp -= 1
            continue
        elif j >= 1:
            print(j, end=' ')
            j -= 1
            continue
        elif k <= i:
            print(k, end=' ')
            k += 1
            continue
        else:
            break
    print()
