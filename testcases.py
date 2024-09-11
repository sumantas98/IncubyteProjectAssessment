import unittest
import calculate

class TestCalculatorNumbers(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calculate.addition(""), 0)
        self.assertEqual(calculate.addition("k"),0)

    def test_single_number(self):
        self.assertEqual(calculate.addition("1"), 1)

# This main function.
if __name__ == '__main__':
    unittest.main()