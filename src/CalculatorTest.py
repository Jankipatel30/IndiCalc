import unittest
from CsvReader import CsvReader
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('src/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('src/csv/Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('src/csv/Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('src/csv/Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, int(row['Result']))



    def test_square(self):
        test_data = CsvReader('src/csv/Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        test_data = CsvReader('src/csv/Square Root.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.square_root(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()