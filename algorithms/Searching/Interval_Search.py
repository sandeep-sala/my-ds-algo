"""
Interval Search: These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half. For Example: Binary Search.
"""

# Binary Search
"""
Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).
"""

# Iterative Method
def binary_search(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Recursive Method
def binary_search_recur(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search_recur(array, x, low, mid-1)
        else:
            return binary_search_recur(array, x, mid + 1, high)
    else:
        return -1


if __name__ == "__main__":
    list_01 = [2, 3, 4, 10, 40]
    list_02 = [2, 3, 4, 6, 1, 2, 5, 2, 10]
    search_element_01 = 10
    search_element_02 = 100

    # Linear Search
    print( binary_search(list_01, search_element_01, 0, len(list_01)-1) )
    print( binary_search(list_01, search_element_02, 0, len(list_01)-1) )
    print( binary_search_recur(list_02, search_element_01, 0, len(list_02)-1) )
    print( binary_search_recur(list_02, search_element_02, 0, len(list_02)-1) )