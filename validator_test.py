import unittest
from validator import Validator

class ValidatorTests(unittest.TestCase):
    def test_is_valid_single_pair_brackets(self):
        validator = Validator('()')
        self.assertTrue(validator._is_valid('My test text ( with brackets ) '))
        self.assertFalse(validator._is_valid('()sldmfsl;j('))

        validator = Validator('[]')
        self.assertTrue(validator._is_valid('My test text [ with brackets ] '))
        self.assertFalse(validator._is_valid('[]]cxcvsd$[]'))

        validator = Validator('{}')
        self.assertTrue(validator._is_valid('My test text { with brackets } '))
        self.assertFalse(validator._is_valid('{}cjlfsdla9*#}'))

        validator = Validator('<>')
        self.assertTrue(validator._is_valid('My test text < with brackets > '))
        self.assertFalse(validator._is_valid('>><klfshkjho**&<'))

    def test_is_valid_many_pairs_brackets(self):
        validator = Validator('()[]{}<>')
        self.assertTrue(validator._is_valid('My test text [{<( with brackets )>}] '))
        self.assertFalse(validator._is_valid('()}{[]>>)'))

    def test_incompatinble_type_of_input(self):
        validator = Validator('()')
        with self.assertRaises(TypeError):
            validator._is_valid(42)



if __name__ == '__main__':
    unittest.main()
