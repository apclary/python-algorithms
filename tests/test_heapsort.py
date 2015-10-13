import unittest
import random
import copy

from python_algorithms.max_heap import MaxHeap
from python_algorithms import heapsort
from tests import print_timing, test_sort


class TestInsertionSort(test_sort.TestSort):

    @print_timing.print_timing
    def test_heapsort(self):     
        # Generate an unsorted and sorted list of the same values
        # to verify a sort worked

        unsorted_list = random.sample(range(1000000), 500) 
        sorted_list = copy.copy(unsorted_list)
        sorted_list.sort()
        heap = MaxHeap()
        heap.set_heap(unsorted_list)
        heap.sort()
        self.assertEqual(heap.heap, sorted_list)

    def test_init(self):
        heap = MaxHeap()
        self.assertEqual(heap.heap_size, 0)
    
    def test_max_heapify(self):
        heap = MaxHeap()
        heap.heap = [16,4,10,14,7,9,3,2,8,1]
        heap.heap_size = len(heap.heap)
        heap._max_heapify(1)
        self.assertEqual(heap.heap, [16,14,10,8,7,9,3,2,4,1]) 
         
    def test_set_heap(self):
        heap = MaxHeap()
        lst = [16,14,10,8,7,9,3,2,4,1]
        heap.set_heap(lst)
        self.assertEqual(heap.heap, lst)
        
    def test_build_max_heap(self):        
        heap = MaxHeap()
        heap.heap = [16,4,10,14,7,9,3,2,8,1]
        heap._build_max_heap()
        self.assertEqual(heap.heap, [16,14,10,8,7,9,3,2,4,1])
        
        heap.set_heap([4,1,3,2,16,9,10,14,8,7])
        heap._build_max_heap()
        self.assertEqual(heap.heap, [16,14,10,8,7,9,3,2,4,1]) 
    
    @print_timing.print_timing
    def test_heapsort_wrapper(self):
        unsorted_list = random.sample(range(1000000), 500) 
        sorted_list = copy.copy(unsorted_list)
        sorted_list.sort()
        heapsort.heapsort(unsorted_list)
        self.assertEqual(unsorted_list, sorted_list)
    
    def test_increase(self):        
        heap = MaxHeap()
        heap.set_heap([16,14,10,8,7,9,3,2,4,1])
        heap.increase_key(8,15)
        self.assertEqual(heap.heap, [16,15,10,14,7,9,3,2,8,1])
        
    def test_extract_max(self):
        heap = MaxHeap()
        heap.set_heap([16,14,10,8,7,9,3,2,4,1])
        max_elem = heap.extract_max()
        self.assertEqual(max_elem, 16)
        self.assertEqual(heap.get_heap(), [14,8,10,4,7,9,3,2,1])      

if __name__ == '__main__':
    unittest.main()