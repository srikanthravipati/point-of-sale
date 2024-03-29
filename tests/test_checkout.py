from unittest import TestCase, main
from unittest.mock import MagicMock, patch

from pytest import approx

user_items = ["B", "A", "B", "P", "B"]
item_price_s = {"A": 25, "B": 40, "P": 30}


class TestCheckout(TestCase):
    # version 1.0
    def test_checkout(self):
        from checkout import checkout

        total = checkout(user_items, item_price_s)
        assert total == approx(155.0)
        # self.assertLessEqual(abs(total - 155.0), float_info.epsilon)

    # version 2.0 thorough testing
    def test_checkout_init(self):
        with patch("checkout.set_inventory_price_and_discount_s", MagicMock()):
            from checkout import Checkout, set_inventory_price_and_discount_s

            Checkout_ = Checkout(item_price_s)
            assert Checkout_.user_items == {}
            set_inventory_price_and_discount_s.assert_called_once_with(item_price_s)

    def test_Checkout_update_user_items(self):
        with patch("checkout.UserItem.scan", MagicMock()):
            from checkout import Checkout
            from item_info import ItemInfo

            _item_info = ItemInfo("A", 25.0, True, 3, 1.0, 0.0)
            Checkout_ = Checkout(item_price_s)
            assert Checkout_.user_items == {}
            Checkout_.update_user_items("A", _item_info)
            Checkout_.user_items["A"].scan.assert_called_once_with(_item_info)
            Checkout_.update_user_items("A", _item_info)
            assert Checkout_.user_items["A"].scan.call_count == 2
            Checkout_.user_items["A"].scan.assert_called_with(_item_info)

    def test_Checkout_scan_via_mock(self):
        with patch("checkout.ItemInfo.set_price_and_discount", MagicMock()), patch(
            "checkout.Checkout.update_user_items", MagicMock()
        ):
            from checkout import Checkout
            from inventory_container import INVENTORY_ITEMS
            from item_info import ItemInfo

            INVENTORY_ITEMS["A"] = ItemInfo("A", 25.0, True, 3, 1.0, 0.0)
            Checkout_ = Checkout(item_price_s)
            Checkout_.scan("A")
            Checkout_.update_user_items.assert_called_once_with(
                "A", INVENTORY_ITEMS["A"]
            )

    def test_checkout_total_via_mock(self):
        with patch("checkout.user_items_total", MagicMock()):
            from checkout import Checkout, user_items_total

            Checkout_ = Checkout(item_price_s)
            Checkout_.total()
            user_items_total.assert_called_once()

    def test_Checkout(self):
        from checkout import Checkout

        Checkout_ = Checkout(item_price_s)

        for item in user_items:
            Checkout_.scan(item)

        assert Checkout_.total() == approx(155.0)


if __name__ == "__main__":
    main()
