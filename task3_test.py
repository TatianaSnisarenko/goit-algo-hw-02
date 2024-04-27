import unittest
from task3 import Stack, is_symmetrical


class TestIsSymmetrical(unittest.TestCase):

    def test_is_symmetrical(self):
        self.assertTrue(is_symmetrical('( ){[ 1 ]( 1 + 3 )( ){ }}'))
        self.assertTrue(is_symmetrical('({[()]})'))
        self.assertTrue(is_symmetrical('[()]'))
        self.assertTrue(is_symmetrical('{}'))
        self.assertTrue(is_symmetrical('()'))

    def test_not_symmetrical(self):
        self.assertFalse(is_symmetrical('( 23 ( 2 - 3);'))
        self.assertFalse(is_symmetrical('( 11 }'))
        self.assertFalse(is_symmetrical('( }'))

    def test_empty_string(self):
        self.assertFalse(is_symmetrical(''))

    def test_single_bracket(self):
        self.assertFalse(is_symmetrical('('))
        self.assertFalse(is_symmetrical(')'))
        self.assertFalse(is_symmetrical('['))
        self.assertFalse(is_symmetrical(']'))
        self.assertFalse(is_symmetrical('{'))
        self.assertFalse(is_symmetrical('}'))


if __name__ == '__main__':
    unittest.main()
