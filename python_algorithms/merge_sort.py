# apclary
# Merge sort implementation
# CLRS 2.3

import sys
import math

def merge_sort(lst):

    # if the list has 0 or 1 elements, it's already sorted
    if len(lst) < 2:
        return lst
        
    # split the list into two halves
    mid_point = int(len(lst)/2)
    left_half = lst[:mid_point]
    right_half = lst[mid_point:]
    
    # sort those lists using the magic of recursion
    merge_sort(left_half)
    merge_sort(right_half)
    
    # Resizing a list is not very performant!
    # Well, whatever, it's python.
    # The infinity at the end prevents index out
    # of range errors in the next section.
    left_half += [math.inf]
    right_half += [math.inf]
    
    # merge the two sorted lists
    i_left = 0
    i_right = 0
    length = len(lst)
    for i_list in range(0,length):
        if left_half[i_left] < right_half[i_right]:
            lst[i_list] = left_half[i_left]
            i_left += 1
        else:
            lst[i_list] = right_half[i_right]
            i_right += 1  

# Allow user to run this script directly and pass in a string of ints to sort
if __name__ == '__main__':
    # convert the first argument from a string of comma-separated ints
    # into an array of ints
    input_list = [int(s) for s in sys.argv[1].split(',')]
    merge_sort(input_list)
    print(input_list)