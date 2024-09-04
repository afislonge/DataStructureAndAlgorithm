import unittest
import twosum as ts

class TestTwoSum(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(ts.twoSum([2,7,11,15], 9), [0, 1])
    self.assertEqual(ts.twoSum([3,2,4], 6), [1, 2])
    self.assertEqual(ts.twoSum([3,3], 6), [0, 1])


if __name__ == '__main__':
  unittest.main()