import unittest
import functions

class TestIsEven(unittest.TestCase):

    def setUp(self):
        self.number = 0 

    def test_is_even_with_string(self):
        self.number = '12'
        self.assertTrue(functions.is_even(self.number), True)

    def test_is_even_with_float(self):
        self.number = 12.0
        self.assertTrue(functions.is_even(self.number), True)

    def test_is_even_with_integer(self):
        self.number = 12
        self.assertTrue(function.is_even(self.number), True)

    def test_is_even_with_integer_failure(self):
        self.number = 13 
        self.assertFalse(function.is_even(self.number), False)



class TestDeposite(unittes.TestCase):

    def setUp(self):
        self.balance = 0
        self.amount = 0 

    def test_deposite_success(self):
        self.balance = 1500
        self.amount = 500 
        self.assertEqual(function.deposite(self.balance, self.amount), 2000)

    def test_deposite_with_negative_amount(self):
        self.balance = 200
        self.amount = -20
        self.assertEqual(functions.deposite(self.balance, self.amount), 200)

    def test_deposite_with_negative_balance(self):
        self.balance = -50 
        self.amount  = 50
        self.assertEqual(self.functions.deposite(self.balance, self.amount), 50)