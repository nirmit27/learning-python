# Merge Sort
# Time Complexity : O(n log n)

def merge_sort(li):

    # Base case
    if len(li) <= 1:
        return li

    else:
        # Partioning
        mid = len(li)//2
        left = merge_sort(li[mid:])
        right = merge_sort(li[:mid])

        # Merging
        i, j, k = 0, 0, 0
        while True:
            if left[i] <= right[j]:
                li[k] = left[i]
                i += 1
                k += 1
                if i == len(left):
                    li[k:] = right[j:]  # sorting in place without append()
                    return li  # returns the left sorted sub-list
            else:
                li[k] = right[j]
                j += 1
                k += 1
                if j == len(right):
                    li[k:] = left[i:]
                    return li


if __name__ == "__main__":

    li = list(map(lambda x: int(x), input("\n Unsorted List : ").split(' ')))
    print("\n Sorted list : ", end='')
    for x in merge_sort(li):
        print(f" {x}", end='')
