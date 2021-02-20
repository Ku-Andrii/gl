import unittest


def delete_element(list1):
    list1.remove(list1[-4])
    return list1


def rem_last_element(list):
    list.remove(list[-1])
    return list


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_Yegor_Panasuk_FI94(self):
        list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(rem_last_element(list), [1, 2, 3, 4, 5])

    def test_michael_medved_fi93(self):
        self.assertEqual(len([] + ['f']), len('f'))

    def test_illia_kripaka_fi_94_2(self):
        self.assertEqual(2 * [1, 3, 5], [1, 3, 5, 1, 3, 5])

    def test_kostiantyn_baievskyi_fi_93(self):
        self.assertEqual([1, 2, 3] + [4, 5, 6], [1, 2, 3, 4, 5, 6])

    def test_andrii_kutsenko_fi_94(self):
        list1 = [4, 5, 7, 3, 8, 6, 3, 9]
        self.assertEqual(delete_element(list1), [4, 5, 7, 3, 6, 3, 9])
        
    def test_1_olia_futurska_fi94(self):
        listo1 = [1, 2, 3, 4, 5, 6, 7]
        listo2 = [1, 2, 3, 4, 6, 6, 7]
        self.assertIsNot(listo1[4], listo2[4])


if __name__ == '__main__':
    unittest.main()
