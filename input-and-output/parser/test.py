import unittest
import parsers

class TestIntegerParser(unittest.TestCase):

    def test_parse_to_integer_float_arg(self):
        result = parsers.parse_to_integer(12.0)
        self.assertEqual(result, 12)

    def test_parse_to_integer_int_arg(self):
        result = parsers.parse_to_integer(12)
        self.assertEqual(result, 12)

    def test_parse_to_integer_string_arg(self):
        result = parsers.parse_to_integer('12')
        self.assertEqual(result, 12)


class TestFloatParser(unittest.TestCase):

    def test_parse_to_float_int_arg(self):
        result = parsers.parse_to_float(12)
        self.assertEqual(result, 12.0)

    def test_parse_to_float_str_arg(self):
        result = parsers.parse_to_float('12')
        self.assertEqual(result, 12)

    def test_parse_to_float_float_arg(self):
        result = parsers.parse_to_float(12.0)
        self.assertEqual(result, 12.0)

class TestStringParser(unittest.TestCase):

    def test_parse_to_string_int_arg(self):
        result = parsers.parse_to_string(12)
        self.assertEqual(result, '12')
        self.assertTrue(isinstance(result, str))
        self.assertFalse(isinstance(result, int))

    def test_parse_to_string_float_arg(self):
        result = parsers.parse_to_string(12.0)
        self.assertEqual(result, '12.0')
        self.assertTrue(isinstance(result, str))
        self.assertFalse(isinstance(result, float)) 


if __name__ == "__main__":
    unittest.main()