import unittest

from unittest.mock import PropertyMock, patch

import numpy as np
from item_offer import Offer


class TestOffer(unittest.TestCase):
    def test_constructor(self):
        offer = Offer(False)
        self.assertEqual(offer.discount_running, False)
        self.assertEqual(offer.discount_n_items, np.iinfo(np.uint64()).max)
        self.assertEqual(offer.discount_value, 0.0)

    def test_set_discount(self):
        offer = Offer(True, 3, 3.0, -100.0)
        self.assertEqual(offer.discount_running, True)
        self.assertEqual(offer.discount_n_items, 3)
        offer.discount_value = 40.0
        self.assertEqual(offer.discount_value, 40.0)
        offer = Offer(True, 3, 1.0, 0.0)
        offer.discount_value = 25.0
        self.assertEqual(offer.discount_value, 25.0)

    def test_is_valid(self):
        offer = Offer(True, 3, 3.0, -100.0)
        with patch(
            "item_offer.Offer.discount_running", new_callable=PropertyMock
        ) as mock_discount_running:
            mock_discount_running.return_value = False
            assert not offer.is_discount_valid(3)
        assert offer.is_discount_valid(3)
        assert not offer.is_discount_valid(1)


if __name__ == "__main__":
    unittest.main()
