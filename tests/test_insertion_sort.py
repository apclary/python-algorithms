from python_algorithms import insertion_sort
from tests import print_timing
from tests import test_sort
import unittest
import random

import copy

class TestInsertionSort(test_sort.TestSort):

    @print_timing.print_timing
    def test_insertion_sort(self):
      short_list = [4,3,5,1,2]
      short_list_sorted = copy.copy(short_list).sort()
      
      self.assertEqual(insertion_sort.insertion_sort(short_list), short_list_sorted)

if __name__ == '__main__':
    unittest.main()