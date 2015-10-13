"""
apclary
Heap sort implementation
CLRS 6.1
"""

class MaxHeap:

    def __init__(self):
        self.heap_size = 0
        self.heap = []
        
    @staticmethod
    def _left(i):
        return 2 * i + 1
    
    @staticmethod
    def _right(i):
        return 2 * i + 2
    
    @staticmethod
    def _parent(i):
        return int((i+1)/2) - 1
     
    def _swap(self,i,j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def _max_heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        largest = None
        
        if l < self.heap_size and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
            
        if r < self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        
        if largest != i:
            self._swap(i,largest)
            self._max_heapify(largest)
    
    def _build_max_heap(self):
        self.heap_size = len(self.heap)
        pos_last_non_leaf_node = int(self.heap_size/2) - 1
        for i in range(pos_last_non_leaf_node, -1, -1):
            #print("calling _max_heapify for",i+1)
            self._max_heapify(i)
        
    def set_heap(self, new_heap):
        self.heap = new_heap
        self.heap_size = len(new_heap)
        
    def sort(self):
        self._build_max_heap()
        for i in range(len(self.heap)-1,0,-1):
            self._swap(0,i)
            self.heap_size -= 1
            self._max_heapify(0)
            
        
            
            
    
    