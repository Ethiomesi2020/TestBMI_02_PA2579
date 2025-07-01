# An Auto Test for both methods in class called WeightHelper using Unittest Tests
import unittest
from hypothesis import given, strategies as st
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
                self.assertAlmostEqual(calculate_BMI(*givens), answers, places=2)

    @given(
        weight=st.floats(min_value=0.1, max_value=500, allow_nan=False, allow_infinity=False),
        height=st.floats(min_value=0.1, max_value=300, allow_nan=False, allow_infinity=False)
    )
    def test_Calculate_BMI_hypothesis(self, weight, height):
        result = calculate_BMI(weight, height)
        self.assertIsInstance(result, (int, float))
        self.assertGreater(result, 0)

    @given(
        weight=st.one_of(st.text(), st.none(), st.lists(st.integers()), st.dictionaries(st.text(), st.integers())),
        height=st.floats(min_value=0.1, max_value=300)
    )
    def test_Calculate_BMI_invalid_weight(self, weight, height):
        self.assertRaises(ValueError, calculate_BMI, weight, height)

    @given(
        weight=st.floats(min_value=0.1, max_value=500),
        height=st.one_of(st.text(), st.none(), st.lists(st.integers()), st.dictionaries(st.text(), st.integers()))
    )
    def test_Calculate_BMI_invalid_height(self, weight, height):
        self.assertRaises(ValueError, calculate_BMI, weight, height)

    @given(
        weight=st.floats(min_value=0.1, max_value=500),
        height=st.floats(max_value=0, allow_nan=False, allow_infinity=False)
    )
    def test_Calculate_BMI_zero_or_negative_height(self, weight, height):
        self.assertRaises(ValueError, calculate_BMI, weight, height)

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

    @given(
        weight=st.floats(min_value=0.1, max_value=500, allow_nan=False, allow_infinity=False),
        height=st.floats(min_value=0.1, max_value=300, allow_nan=False, allow_infinity=False)
    )
    def test_Category_BMI_hypothesis(self, weight, height):
        result = category_BMI(weight, height)
        self.assertIsInstance(result, str)
        self.assertIn(result, {"Underweight", "Normal weight", "Overweight", "Obese"})

    @given(
        weight=st.one_of(st.text(), st.none(), st.lists(st.integers()), st.dictionaries(st.text(), st.integers())),
        height=st.floats(min_value=0.1, max_value=300)
    )
    def test_Category_BMI_invalid_weight(self, weight, height):
        self.assertRaises(ValueError, category_BMI, weight, height)

    @given(
        weight=st.floats(min_value=0.1, max_value=500),
        height=st.one_of(st.text(), st.none(), st.lists(st.integers()), st.dictionaries(st.text(), st.integers()))
    )
    def test_Category_BMI_invalid_height(self, weight, height):
        self.assertRaises(ValueError, category_BMI, weight, height)

    @given(
        weight=st.floats(min_value=0.1, max_value=500),
        height=st.floats(max_value=0, allow_nan=False, allow_infinity=False)
    )
    def test_Category_BMI_zero_or_negative_height(self, weight, height):
        self.assertRaises(ValueError, category_BMI, weight, height)


if __name__ == "__name__":
    unittest.main()
