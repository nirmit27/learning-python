"""        *
          * *
         * * *
        * * * *
       * * * * *        """

rows = int(input("Enter the number of rows: "))
space=rows
for i in range(0,rows):
    for sp in range(space):
        print(end=' ')
    for j in range(0,i+1):
        print('*',end=' ')
    print()
    space-=1