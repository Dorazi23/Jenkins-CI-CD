import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test case for the Calculator class."""

    def setUp(self):
        """Set up a new Calculator instance before each test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calculator.subtract(3, 2), 1)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-1, 1), -1)
        self.assertEqual(self.calculator.divide(-1, -1), 1)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Test division by zero."""
        with self.assertRaises(ValueError):
            self.calculator.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
