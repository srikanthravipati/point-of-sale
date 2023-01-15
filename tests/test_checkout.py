import unittest
from sys import float_info

from checkout import Checkout, checkout

user_items = ["B", "A", "B", "P", "B"]
item_price_s = {"A": 25, "B": 40, "P": 30}


class TestCheckout(unittest.TestCase):
    # version 1.0
    def test_checkout(self):
        total = checkout(user_items, item_price_s)
        self.assertLessEqual(abs(total - 155.0), float_info.epsilon)

    # version 2.0
    def test_Checkout(self):
        Checkout_ = Checkout(item_price_s)

        for item in user_items:
            Checkout_.scan(item)

        self.assertLessEqual(abs(Checkout_.total() - 155.0), float_info.epsilon)


if __name__ == "__main__":
    unittest.main()
