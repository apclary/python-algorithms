"""
apclary
Heap sort implementation
CLRS 6.1
"""
from python_algorithms.max_heap import MaxHeap

def heapsort(lst):
    heap = MaxHeap()
    heap.set_heap(lst)
    heap.sort()
            
        
            
            
    
    