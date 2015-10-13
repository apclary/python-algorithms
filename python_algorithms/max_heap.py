import math

class MaxHeap:

    def __init__(self):
        self.heap_size = 0
        self.heap = []
        
    def __str__(self):
        print(self.heap)
        
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
            self._max_heapify(i)
            
    def get_heap(self):
       return self.heap[:self.heap_size]
        
    def set_heap(self, new_heap):
        self.heap = new_heap
        self.heap_size = len(new_heap)
        
    def sort(self):
        self._build_max_heap()
        for i in range(len(self.heap)-1,0,-1):
            self._swap(0,i)
            self.heap_size -= 1
            self._max_heapify(0)
    
    def max(self):
        return self.heap[0]
        
    def print_tree(self):
        one_level = ''
        print('')
        for i in range(0,self.heap_size):
            one_level += ' ' + str(self.heap[i])
            # if last element in a level of a binary tree
            if (math.log2(i+2).is_integer()): 
                print(one_level)
                one_level = ''
        
        # to account for a partially-filled last row
        if one_level != '':
            print(one_level)
        
    
    def extract_max(self):
        if (self.heap_size) < 1:
            raise HeapEmptyException("Heap is empty")
        max_elem = self.heap[0]
        last_elem = self.heap[self.heap_size-1]
        self.heap[0] = last_elem
        self.heap_size -= 1
        self._max_heapify(0)
        return max_elem
    
    def increase_key(self, i, key):
        if key < self.heap[i]:
            raise ValueError("New key must be greater than or equal to the current key")
        self.heap[i] = key
        
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self._swap(i,self._parent(i))
            i = self._parent(i)
    
    def insert(self, key):
        self.heap_size += 1
        self.heap[self.heap_size - 1] = -math.inf
        self.increase_key(self.heap_size - 1, key)
                

class HeapEmptyException(BaseException):
    pass