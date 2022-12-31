import unittest
from maths import add, sub,  division 



class TestMathAdd(unittest.TestCase):

    def setUp(self) -> None:
        self.result = 0

    def test_add_with_integer(self):
        self.result = add(12, 20)
        self.assertEqual(self.result, 32)
        self.assertTrue(isinstance(self.result, int))

    def test_add_with_float(self):
        self.result = add(12.3, 10)
        self.assertEqual(self.result, 22.3)
        self.assertTrue(isinstance(self.result, float))

    def test_add_with_string(self):
        self.result = add('12', '3')
        self.assertEqual(self.result, 15)
        self.assertTrue(isinstance(self.result, int))

class TestMathSub(unittest.TestCase):

    def setUp(self) -> None:
        self.result = 0 

    def test_sub_with_string(self):
        self.result = sub('12','3')
        self.assertEqual(self.result, 9)

    def test_sub_with_float(self):
        self.result = sub(12.3, 10)
        self.assertEqual(self.result, 2.3000000000000007)

    def test_sub_with_integer(self):
        self.result = sub(10, 30)
        self.assertEqual(self.result, 40)

class TestMathDivision(unittest.TestCase):

    def setUp(self) -> None:
        self.result = 0 

    def test_division_with_string(self):
        self.result = division('12','3')
        self.assertEqual(self.result, 4)

    def test_division_with_float(self):
        self.result = division(12.3, 10)
        self.assertEqual(self.result, 1.0)

    def test_division_with_integer(self):
        self.result = division(10, 30)
        self.assertEqual(self.result, 0)


if __name__ == "__main__":
    unittest.main()