# An Auto Test for both methods in class called WeightHelper using Unittest Tests
import unittest
from WeightHelper import calculate_BMI, category_BMI


class TestWeightHelper(unittest.TestCase):
    def test_Calculate_BMI(self):
        test_input_bm = [
            ((70, 180), 21.6),
            ((90, 172), 30.42),
            ((50, 200), 12.50),
            (("Obese", "Obese"), "Obese"),
            ((70, 0), 0)
        ]

        for givens, answers in test_input_bm:
            if 0 in givens:
                # The AssertRaises Test Case for Calculate_BMI
                self.assertRaises(ValueError, calculate_BMI, *givens)
            elif not isinstance(givens[0], (int, float)):
                self.assertRaises(ValueError, calculate_BMI, *givens)
            elif not isinstance(givens[1], (int, float)):
                self.assertRaises(ValueError, calculate_BMI, *givens)
            elif not isinstance(answers, (int, float)):
                self.assertRaises(ValueError, calculate_BMI, answers, answers)
            else:
                # The Valid Test Case for Calculate_BMI
                self.assertEqual(calculate_BMI(*givens), answers)

    def test_Category_BMI(self):
        tests_category = [
            ((50, 200), "Underweight"),
            ((70, 180), "Normal weight"),
            ((90, 172), "Obese"),
            (("Obese", "Obese"), "Obese"),
            ((0, 0), "Underweight")
        ]

        for givens, answers in tests_category:
            if 0 in givens:
                # The AssertRaises Test Case for Category_BMI
                self.assertRaises(ValueError, category_BMI, *givens)
            elif not isinstance(givens[0], (int, float)):
                self.assertRaises(ValueError, category_BMI, *givens)
            elif not isinstance(givens[1], (int, float)):
                self.assertRaises(ValueError, category_BMI, *givens)
            else:
                # The Valid Test Case for Category_BMI
                self.assertEqual(category_BMI(*givens), answers)


if __name__ == "__name__":
    unittest.main()
