# apclary
# hello world implementation

from python_algorithms import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(hello_world.say_hello(), 'Hello World!')

if __name__ == '__main__':
    unittest.main()
