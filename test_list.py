import unittest


def delete_element(list1):
    list1.remove(list1[-4])
    return list1


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_illia_kripaka_fi_94_2(self):
        self.assertEqual(2*[1, 3, 5], [1, 3, 5, 1, 3, 5])

    def test_andrii_kutsenko_fi_94(self):
        list1 = [4, 5, 7, 3, 8, 6, 3, 9]
        self.assertEqual(delete_element(list1), [4, 5, 7, 3, 6, 3, 9])


if __name__ == '__main__':
    unittest.main()
