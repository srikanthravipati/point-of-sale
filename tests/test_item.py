import unittest

from user_item import UserItem, user_items_total


class TestItem(unittest.TestCase):
    def test_constructor(self):
        item = UserItem()
        self.assertEqual(item.count, 0)
        self.assertEqual(item.total, 0.0)

    def test_increase_count(self):
        item = UserItem()
        item.incr_count_by_one()
        self.assertEqual(item.count, 1)

    def test_increase_total(self):
        item = UserItem()
        item.add_item_price_to_total(25.0)
        self.assertEqual(item.total, 25.0)

    def test_apply_offer(self):
        item = UserItem()
        item.add_item_price_to_total(25.0)
        item.apply_discount(5.0)
        self.assertEqual(item.total, 20.0)

    def test_items_total(self):
        items = {"A": UserItem(), "B": UserItem()}
        for i in range(2):
            items["A"].incr_count_by_one()
            items["A"].add_item_price_to_total(10.0)
        self.assertEqual(items["A"].count, 2)
        self.assertEqual(items["A"].total, 20.0)
        items["B"].incr_count_by_one()
        items["B"].add_item_price_to_total(15.0)
        self.assertEqual(items["B"].count, 1)
        self.assertEqual(items["B"].total, 15.0)
        self.assertEqual(user_items_total(items), 35.0)


if __name__ == "__main__":
    unittest.main()
