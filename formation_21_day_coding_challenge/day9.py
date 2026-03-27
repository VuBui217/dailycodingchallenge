"""
Implement binary search on an array. Return the index of the value if found and -1 otherwise.
function binarySearch(data, k) {
  /* your code here */
}
"""

def binary_search(arr, k):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            r = mid - 1
        else:
            l = mid + 1
    return -1 


