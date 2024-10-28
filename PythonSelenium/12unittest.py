import unittest
from parameterized import parameterized
'''
Create a test class that inherits from unittest.TestCase.
Define methods that start with test_ to indicate they are test cases.

Assertions
unittest provides a variety of assertion methods to check for conditions:

assertEqual(a, b)
assertNotEqual(a, b)
assertTrue(x)
assertFalse(x)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a, b)
assertNotIn(a, b)

'''

#python -m unittest discover -s tests -p "*.py"


class TestSample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
    #method
    def setUp(self):
        self.value = 10

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.shared_resource = 'resource'

    @classmethod
    def tearDownClass(cls):
        pass  # Cleanup class-level resources

    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(3 - 1, 2)

    @unittest.skip("Skip this test")
    def test_skip(self):
        pass

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2)  # This will not count as a failure

    def test_raises_exception(self):
        with self.assertRaises(ValueError):
            raise ValueError("An error occurred")



    @parameterized.expand([
            (1, 2, 3),
            (2, 3, 5)
        ])
    def test_add(self, a, b, expected):
            self.assertEqual(a + b, expected)



