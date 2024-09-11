import unittest
import calculate

class TestCalculatorNumbers(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calculate.addition(""), 0)
        self.assertEqual(calculate.addition("abcd"), 0)
        self.assertEqual(calculate.addition("*jauyw#$"), 0)

    def test_single_number(self):
        self.assertEqual(calculate.addition("1"), 1)
    def test_twice_number(self):
        self.assertEqual(calculate.addition("2,2"), 4)



# This main function.
if __name__ == '__main__':
    unittest.main()