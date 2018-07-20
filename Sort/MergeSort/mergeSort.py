def merge(arr , l, m, r) :
    # TODO
    pass

def mergeSort(arr, l, r) :
    if l < r :
        # To avoid overflow for large l and h.
        m = (l + (r - 1))/2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ('Given array is')
for i in range(n) :
    print ('%d' %arr[i])

mergeSort(arr, 0, n-1)
print ('sdfa')
