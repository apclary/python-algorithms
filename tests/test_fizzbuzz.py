from python_algorithms import fizzbuzz
from contextlib import redirect_stdout
import io
import unittest
import os

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizzbuzz(self):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        
        correct_output = None
        with open (os.path.join(test_dir,"fizzbuzz-correct-output.txt"), "r") as output_file:
            correct_output = output_file.read()
        f = io.StringIO()
        with redirect_stdout(f):
            fizzbuzz.fizzbuzz()
        s = f.getvalue()
        self.assertEqual(s, correct_output)

if __name__ == '__main__':
    unittest.main()