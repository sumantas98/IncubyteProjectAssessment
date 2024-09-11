import unittest
import calculate

class TestCalculatorNumbers(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calculate.addition(""), 0)

# This main function.
if __name__ == '__main__':
    unittest.main()