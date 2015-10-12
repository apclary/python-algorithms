"""
apclary
Heap sort implementation
CLRS 6.1
"""

#todo
__all__ = ['methods i want to expose']

def left(i):
    return 2 * i
    
def right(i):
    return 2 * i + 1
    
def parent(i):
    return i / 2

def max_heapify(lst, i):
    l = left(i)
    r = right(i)
    
    
    