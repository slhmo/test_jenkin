import unittest

import main


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """this method gets called once first before running all tests"""
        pass

    @classmethod
    def tearDownClass(cls):
        """this method gets called once after all the test have been run"""
        pass

    def setUp(self):
        """this method gets called every time before a test is called"""
        pass

    def tearDown(self):
        """this method gets called every tima after a test is called"""
        pass

    def test_addition(self):
        """we will try to catch the edges (H-cases) by testing different possibilities"""
        self.assertIs(main.add(10, 11), 21)
        self.assertIs(main.add(-10, 11), 1)
        self.assertIs(main.add(10, -11), -1)

    def test_subtraction(self):
        self.assertEqual(main.subtract(20, 12), 8)
        self.assertEqual(main.subtract(2, 12), -10)
        self.assertEqual(main.subtract(20, -12), 32)

    def test_multiplication(self):
        self.assertEqual(main.multiply(20, 2, 1), 40)
        self.assertEqual(main.multiply(2, -2, 3), -12)
        self.assertEqual(main.multiply(-2, -12, 2), 48)
        self.assertEqual(main.multiply(0, -12, -3), 0)

    def test_division(self):
        self.assertEqual(main.divide(20, 2), 10)
        self.assertEqual(main.divide(2, -2), -1)
        self.assertEqual(main.divide(-12, -2), 6)
        self.assertEqual(main.divide(0, -12), 0)
        self.assertRaises(ValueError, main.divide, -12, 0) # we cant just give
        # arguments to the subtract function because it will raise an error
        # and break the implementation so we give the arguments to unittest,
        # to implement function safely


if __name__ == '__main__':
    unittest.main()