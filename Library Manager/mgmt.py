# Library Management Class Script

class Management:
    '''
    This class contains methods for the management of the library.
    '''
    @classmethod
    def update(self, b: str, a: str, d=0):
        '''
        For adding new books by the same author ...
        '''
        self.book = b.lower()
        self.author = a.lower()
        i = 0
        temp = ''
        try:
            with open('lib.txt') as f:
                f.seek(0)
                entries = f.readlines()
                for entry in entries:
                    i = entries.index(entry)
                    if d == 0:
                        if self.author in entry and self.book not in entry:
                            temp = entry.rstrip('\n') + f" {self.book}\n"
                            break
                        else:
                            print("\n {self.book} already in the records!\n")
                            break
                    else:

                        # For deleting a book from an author ...

                        t = entry.split(f' {self.book}')
                        temp = t[0] + ' ' + t[1]
                        break
                    print("\n Updated Entry : {temp}\n")
                entries[i] = temp
            with open('lib.txt', 'w') as f:
                f.writelines(entries)
                print("\n Record updated succesfully!")
        except:
            print("\n The library doesn't exist!\n")

    @classmethod
    def add(self, b, a):
        '''
        For adding new books by the different authors ...
        '''
        self.book = b.lower()
        self.author = a.lower()
        flag = 0
        try:
            with open('lib.txt', 'a+') as f:
                f.seek(0)
                entries = f.readlines()

                # In case the library is empty ...

                if len(entries) == 0:
                    f.append(f"{self.author}, {self.book}\n")
                    print("\n Record updated succesfully!")
                else:
                    for entry in entries:
                        if self.author in entry:
                            flag += 1

                    if flag:
                        f.append(f"{self.author}, {self.book}\n")
                        print("\n Record updated succesfully!")
                    else:
                        f.close()
                        self.update(b, a)
        except:
            print("\n The library doesn't exist!\n")

    @classmethod
    def delete(self, db: list = [], rn=0):
        '''
        For deleting books ...
        '''
        self.del_books = list(set(db))
        self.record_no = rn - 1

        try:
            if self.record_no != -1:

                with open('lib.txt') as f:
                    entries = f.readlines()

                with open('lib.txt', 'w') as f:
                    for i in range(len(entries)):
                        if i != self.record_no:
                            f.write(entries[i])
                        else:
                            print("\n Record deleted successfully!\n")

            elif len(self.del_books) != 0:
                with open('lib.txt', 'r') as f:
                    entries = f.readlines()

                for entry in entries:
                    for bname in self.del_books:
                        if bname.lower() in entry:
                            temp = entry.split(',')
                            self.update(bname, temp[0], 'yes')

            else:
                print("\n Incorrect index!\n")

        except:
            print("\n The library doesn't exist!\n")
