"""
apclary
Quicksort implementation in Python
CLRS 7.1
"""
def quicksort(lst):
    _quicksort(lst, 0, len(lst)-1)

def _quicksort(lst, start, end):
    if start < end:
        pivot = partition(lst, start, end)
        _quicksort(lst, start, pivot-1)
        _quicksort(lst, pivot, end)

"""
Reorder a list such that all elements less than the last element are before it,
and conversely all elements larger than the last element after after it.
"""
def partition(lst, start, end):
    pivot = lst[end]
    i = start
    for j in range(start+1, end):
        if lst[j] <= pivot:
            i += 1
            swap(lst, i, j)
    swap(lst, i+1, end)
    return i+1
            
# Swap two values in an array
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = lst[i]
    
       