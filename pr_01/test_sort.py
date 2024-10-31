import unittest
from pr_01_doctest_unittest import bubble_sort

class TestSort (unittest.TestCase):
    def test_case1(self):
        self.assertEqual(bubble_sort([]), [])

    def test_case2(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_case3(self):
        self.assertEqual(bubble_sort([10, 10, 10, 10]), [10, 10, 10, 10])

    def test_case4(self):
        self.assertEqual(bubble_sort([9, 99, 999]), [9, 99, 999])

    def test_case5(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])

    def test_case6(self):
        self.assertEqual(bubble_sort([39, 12, 18, 85, 72, 10, 2, 18]), [2, 10, 12, 18, 18, 39, 72, 85])

if __name__ == '__main__':
    unittest.main()