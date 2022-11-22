"""
Sequential Search: In this, the list or array is traversed sequentially and every element is checked. For example: Linear Search.
"""


# Linear Search 
"""
Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found, otherwise the search continues till the end of the data set. It is the easiest searching algorithm
"""

# Iterative Method
def linear_seach(a, n):
    for i, j in enumerate(a):
        if j == n:
            return i
    return -1

# Recursive Method
def linear_search_recur(arr, key, size):
    if (size == 0):
        return -1
    elif (arr[size - 1] == key):
        return size - 1
    else:
        return linear_search_recur(arr, key, size - 1)



if __name__ == "__main__":
    list_01 = [2, 3, 4, 10, 40]
    list_02 = [2, 3, 4, 6, 1, 2, 5, 2, 10]
    search_element_01 = 10
    search_element_02 = 100

    # Linear Search
    print( linear_seach(list_01, search_element_01) )
    print( linear_seach(list_01, search_element_02) )
    print( linear_seach(list_02, search_element_01) )
    print( linear_seach(list_02, search_element_02) )