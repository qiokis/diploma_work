import unittest
from handler.validator import Validator


class TestValidator(unittest.TestCase):

    valid = Validator()

    def test_validate(self):
        data = ((1, 2, 3),
                ("a", 1, 2),
                (-1, -2, -3),
                (2.3, 2.5),
                "3,6")
        expect = (True, False, True, True, True)
        for case, exp in zip(data, expect):
            self.assertTrue(case, exp)

    def test_replacer(self):
        self.assertTrue(self.valid.comma_replace({"a": "1,1", "b": "-2,3"}),
                        {"a": "1.1", "b": "-2.3"})