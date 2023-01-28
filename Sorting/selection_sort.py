# Selection Sort
# Time Complexity : O(n^2)

def sel_sort(li):

    for i in range(len(li)):
        pos = i

        for j in range(i+1, len(li)):

            if li[j] < li[pos]: # finding smallest element
                pos = j

        li[pos], li[i] = li[i], li[pos] # swapping 

    return li


if __name__ == "__main__":

    li = list(map(lambda x: int(x), input(
        '''\n Enter unsorted list : ''').split(' ')))
    
    print("\n Sorted list : ", end='')
    
    for x in sel_sort(li):
        print(f" {x}", end='')
