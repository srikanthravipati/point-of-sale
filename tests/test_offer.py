import unittest

import numpy as np
from item_offer import Offer


class TestOffer(unittest.TestCase):
    def test_constructor(self):
        offer = Offer(False)
        self.assertEqual(offer.is_running(), False)
        self.assertEqual(offer.get_n_items(), np.iinfo(np.uint64()).max)
        self.assertEqual(offer.get_reduction(), 0.0)

    def test_set_reduction(self):
        offer = Offer(True, 3, 3.0, -100.0)
        self.assertEqual(offer.is_running(), True)
        self.assertEqual(offer.get_n_items(), 3)
        offer.set_reduction(40.0)
        self.assertEqual(offer.get_reduction(), 20.0)
        offer = Offer(True, 3, 1.0, 0.0)
        offer.set_reduction(25.0)
        self.assertEqual(offer.get_reduction(), 25.0)


if __name__ == "__main__":
    unittest.main()
