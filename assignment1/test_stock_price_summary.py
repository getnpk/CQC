import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_null_case(self):
        """
        null list passed
        """
        self.assertEqual(a1.stock_price_summary([]),(0,0))

    def test_zero_single_case(self):
        """
        a single element list and of value 0 is passed
        """
        self.assertEqual(a1.stock_price_summary([0]),(0,0))

    def test_single_positive_element_case(self):
        """
        a single positive element
        """
        self.assertEqual(a1.stock_price_summary([1.0]),(1.0,0))
        
    def test_single_negative_element_case(self):
        """
        a single negative element
        """
        self.assertEqual(a1.stock_price_summary([-1.0]),(0,-1.0))

    def test_two_negative_positive_element_case(self):
        """
        two elements in list, one negative and one positive.
        """
        self.assertEqual(a1.stock_price_summary([1.0, -1.0]),(1.0,-1.0))


    def test_two_negative_zero_element_case(self):
        """
        two elements in list, one negative and one zero
        """
        self.assertEqual(a1.stock_price_summary([0, -1.0]),(0,-1.0))


    def test_two_zero_positive_element_case(self):
        """
        two elements in list, one zero and one positive.
        """
        self.assertEqual(a1.stock_price_summary([1.0, 0]),(1.0,0))


    def test_general_case_more_positive(self):
        """
        combiation of more positive elements
        """
        self.assertEqual(a1.stock_price_summary([1.0, -1.0, 1.0]),(2.0,-1.0))
        
    def test_general_case_more_negative(self):
        """
        combiation of more negative elements
        """
        self.assertEqual(a1.stock_price_summary([1.0, -1.0, -1.0]),(1.0,-2.0))


if __name__ == '__main__':
    unittest.main(exit=False)
