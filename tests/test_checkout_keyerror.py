import unittest

from checkout import Checkout, checkout


class TestBasicInfo(unittest.TestCase):
    def test_checkout_exception(self):
        self.assertRaises(KeyError, checkout, ["D"], {"A": 25})

    def test_Checkout_exception(self):
        Checkout_ = Checkout({"A": 25})
        self.assertRaises(KeyError, Checkout_.scan_item, "C")


if __name__ == "__main__":
    unittest.main()
