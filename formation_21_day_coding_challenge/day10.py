"""
Implement merge sort on an array.
function mergeSort(data) {
  /* your code here */
}
"""
def merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

arr = [4, 5, 1, 3, 2]
print(mergeSort(arr))