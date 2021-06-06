import unittest

from item import Item, items_total, offer_eligible


class TestItem(unittest.TestCase):
    def test_constructor(self):
        item = Item()
        self.assertEqual(item.get_count(), 0)
        self.assertEqual(item.get_total(), 0.0)

    def test_increase_count(self):
        item = Item()
        item.increase_one_count()
        self.assertEqual(item.get_count(), 1)

    def test_increase_total(self):
        item = Item()
        item.increase_total_by_unit_price(25.0)
        self.assertEqual(item.get_total(), 25.0)

    def test_offer_eligible(self):
        self.assertFalse(offer_eligible(0, 3))
        self.assertFalse(offer_eligible(2, 3))
        self.assertTrue(offer_eligible(3, 3))
        self.assertFalse(offer_eligible(4, 3))
        self.assertTrue(offer_eligible(6, 3))

    def test_apply_offer(self):
        item = Item()
        item.increase_total_by_unit_price(25.0)
        item.apply_offer(5.0)
        self.assertEqual(item.get_total(), 20.0)

    def test_items_total(self):
        items = {"A": Item(), "B": Item()}
        for i in range(2):
            items["A"].increase_one_count()
            items["A"].increase_total_by_unit_price(10.0)
        self.assertEqual(items["A"].get_count(), 2)
        self.assertEqual(items["A"].get_total(), 20.0)
        items["B"].increase_one_count()
        items["B"].increase_total_by_unit_price(15.0)
        self.assertEqual(items["B"].get_count(), 1)
        self.assertEqual(items["B"].get_total(), 15.0)
        self.assertEqual(items_total(items), 35.0)


if __name__ == "__main__":
    unittest.main()
