'''   5 4 3 2 1 2 3 4 5 
        4 3 2 1 2 3 4  
          3 2 1 2 3
            2 1 2 
              1         '''

import time as t

# start = t.time()

rows = int(input("Enter the number of rows : "))

start = t.time()

for i in range(rows):
    sp = 0
    j = rows - i
    k = 2
    while (1):
        if sp < i:
            print(" ", end='')
            sp += 1
            continue
        elif j >= 1:
            print(j, end='')
            j -= 1
            continue
        elif k <= (rows-i):
            print(k, end='')
            k += 1
            continue
        else:
            break
    print()

end = t.time()

print(f"\n Time taken : {end - start}\n")
