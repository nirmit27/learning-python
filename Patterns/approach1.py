"""        4 3 2 1 2 3 4
             3 2 1 2 3 
               2 1 2
                 1              """

import time as t

start = t.time()

space = 0
n = int(input("Enter the number of rows between 1-9: "))
for i in range(n, 0, -1):
    for sp in range(space):
        print(end=' ')
    for j in range(i, 0, -1):
        print(j, end='')
    for k in range(2, i+1):
        print(k, end='')
    print()
    space += 1

end = t.time()

print(f"\n Time taken : {end - start}\n")
