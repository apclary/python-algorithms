import unittest
import random
import copy

from python_algorithms import quicksort
from tests import print_timing, test_sort


class TestInsertionSort(test_sort.TestSort):

    @print_timing.print_timing
    def test_quicksort(self):     
        # Generate an unsorted and sorted list of the same values
        # to verify a sort worked
        unsorted_list = random.sample(range(100), 50) 
        sorted_list = copy.copy(unsorted_list).sort()
        
        self.assertEqual(quicksort.quicksort(unsorted_list), sorted_list)

if __name__ == '__main__':
    unittest.main()