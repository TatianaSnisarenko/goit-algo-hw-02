import unittest
from task2 import is_palindrom


class TestIsPalindrome(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.data = {'І що сало? Ласощі': True,
                     'Уму - мінімуму!': True,
                     'Паліндром — і ні морд, ні лап': True,
                     'Аби ріці риба': True,
                     'Наперед здере пан': True,
                     'тв': False,
                     'три': False,
                     '   ': False,
                     '9009': True,
                     'pipi': False,
                     'ippi': True,
                     'madam': True,
                     'око': True}
        super().__init__(methodName)

    def test_palindrom(self):
        for text, result in self.data.items():
            for text, result in self.data.items():
                self.assertEqual(is_palindrom(text), result)


if __name__ == '__main__':
    unittest.main()
