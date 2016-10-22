import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """tests for `primes.py`"""

    def test_is_four_prime(self):
        """is four successfully determined to not be prime?"""
        self.assertTrue(is_prime(4))

    def test_is_five_prime(self):
        """is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()
