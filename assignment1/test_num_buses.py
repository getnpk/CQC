import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_zero_case(self):
        """
        What if there are no one
        """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)


    def test_one_case(self):
        """
        0<n<50
        """
        self.assertEqual(a1.num_buses(10), 1)

    def test_50_case(self):
        """
        n = 50
        """
        self.assertEqual(a1.num_buses(50), 1)

    def test_general_one_case(self):
        """
        50<n<100
        """
        self.assertEqual(a1.num_buses(75), 2)

    def test_general_two_case(self):
        """
        n = 100
        """
        self.assertEqual(a1.num_buses(100), 2)

    def test_general_three_case(self):
        """
        n > 100
        """
        self.assertEqual(a1.num_buses(110), 3)    


if __name__ == '__main__':
    unittest.main(exit=False)
