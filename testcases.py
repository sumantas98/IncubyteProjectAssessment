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
    def test_multiple_number_with_comma(self):
        self.assertEqual(calculate.addition("2,2,0"), 4)
        self.assertEqual(calculate.addition("2,2,3"), 7)
        self.assertEqual(calculate.addition("2,1,5,7"), 15)
        self.assertEqual(calculate.addition("8,2,1"), 11)



# This main function.
if __name__ == '__main__':
    unittest.main()