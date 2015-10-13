import unittest
import random
import copy

from python_algorithms import merge_sort
from tests import print_timing, test_sort


class TestInsertionSort(test_sort.TestSort):

    @print_timing.print_timing
    def test_merge_sort(self):     
        # Generate an unsorted and sorted list of the same values
        # to verify a sort worked
        unsorted_list = random.sample(range(1000000), 500) 
        sorted_list = copy.copy(unsorted_list).sort()
        
        self.assertEqual(merge_sort.merge_sort(unsorted_list), sorted_list)

if __name__ == '__main__':
    unittest.main()