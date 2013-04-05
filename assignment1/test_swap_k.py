import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_null_case(self):
        """
        empty list passed with arg k = 0
        """
        num = []
        k = 0
        num_expected = []

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

    def test_one_case(self):
        """
        single element list passed with arg k = 0
        """
        num = [1]
        k = 0
        num_expected = [1]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

    def test_one_case_two(self):
        """
        single element list passed with arg k = 1
        """
        num = [1]
        k = 1
        num_expected = [1]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

    def test_two_case(self):
        """
        two element list passed with arg k = 1
        """
        num = [1,2]
        k = 1
        num_expected = [2,1]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

    def test_two_case_two(self):
        """
        two element list passed with arg k = 0
        """
        num = [1,2]
        k = 0
        num_expected = [1,2]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

    def test_three_case(self):
        """
        three element list passed with arg k = 0
        """
        num = [1,2,3]
        k = 0
        num_expected = [1,2,3]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)


    def test_three_case_two(self):
        """
        three element list passed with arg k = 1
        """
        num = [1,2,3]
        k = 1
        num_expected = [3,2,1]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

    def test_general_even(self):
        """
        four element general list passed with arg k = 1
        """
        num = [1,2,3,4]
        k = 1
        num_expected = [4,2,3,1]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

    def test_general_even_two(self):
        """
        four element general list passed with arg k = 2
        """
        num = [1,2,3,4]
        k = 2
        num_expected = [3,4,1,2]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

    def test_general_odd(self):
        """
        five element general list passed with arg k = 2
        """
        num = [1,2,3,4,5]
        k = 2
        num_expected = [4,5,3,1,2]

        a1.swap_k(num,k)
        self.assertEqual(num, num_expected)

if __name__ == '__main__':
    unittest.main(exit=False)
