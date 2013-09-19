import math
import unittest


def binary_chop(target, int_array, balance=0):
    mid = int(math.floor((len(int_array) - 1) / 2))

    try:
        if target == int_array[mid]:
            return mid + balance
        elif len(int_array) == 1:
            return -1
    except IndexError:
        return -1

    if target < int_array[mid]:
        index = binary_chop(target, int_array[:mid])

    else:
        index = binary_chop(target, int_array[mid+1:], balance+mid+1)

    return index


class TestBinaryChop(unittest.TestCase):
    def test_chop(self):
        self.assertEqual(-1, binary_chop(3, []))
        self.assertEqual(-1, binary_chop(3, [1]))
        self.assertEqual(0,  binary_chop(1, [1]))
        self.assertEqual(0,  binary_chop(1, [1, 3, 5]))
        self.assertEqual(1,  binary_chop(3, [1, 3, 5]))
        self.assertEqual(2,  binary_chop(5, [1, 3, 5]))
        self.assertEqual(-1, binary_chop(0, [1, 3, 5]))
        self.assertEqual(-1, binary_chop(2, [1, 3, 5]))
        self.assertEqual(-1, binary_chop(4, [1, 3, 5]))
        self.assertEqual(-1, binary_chop(6, [1, 3, 5]))
        self.assertEqual(0,  binary_chop(1, [1, 3, 5, 7]))
        self.assertEqual(1,  binary_chop(3, [1, 3, 5, 7]))
        self.assertEqual(2,  binary_chop(5, [1, 3, 5, 7]))
        self.assertEqual(3,  binary_chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop(8, [1, 3, 5, 7]))

if __name__ == '__main__':
    unittest.main()
