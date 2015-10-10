# apclary
# Insertion sort implementation
# CLRS 2.1

def insertion_sort(list):
    for j in range(1,len(list)):
        # The element to be inserted into the sorted section of the list
        key = list[j]
        # The comparison element is set to the end of the sorted section of the list
        i = j - 1 
        
        # Proceed downward through the sorted section
        # to find an element which is less than the key.
        # That location + 1 must be the correct spot for 
        # the key. Shift the rest of the elements forward
        # by one to make room.
        while i > 0 and list[i] > key:
            # Shift elements forward
            list[i+1] = list[i]
            i = i - 1
            
        # This is the position where the elment before is lower and 
        # the element above is higher, so this is the correct spot to
        # place it.
        list[i+1] = key 