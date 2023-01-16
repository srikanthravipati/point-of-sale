from unittest import TestCase, main
from unittest.mock import MagicMock, patch


class TestItemInfo(TestCase):
    def test_constructor(self):
        with patch("item_info.BasicInfo.__init__", MagicMock(return_value=None)), patch(
            "item_info.Offer.__init__", MagicMock(return_value=None)
        ):
            from item_info import BasicInfo, ItemInfo, Offer

            item_info = ItemInfo("Test", 2.0, True, 2, 1.0, 2.0)
            BasicInfo.__init__.assert_called_once_with(item_info, "Test", 2.0)
            Offer.__init__.assert_called_once_with(item_info, True, 2, 1.0, 2.0)

    def test_print(self):
        with patch("item_info.BasicInfo.print", MagicMock()), patch(
            "item_info.Offer.print", MagicMock()
        ):
            from item_info import BasicInfo, ItemInfo, Offer

            item_info = ItemInfo("Test")
            item_info.print()
            BasicInfo.print.assert_called_once_with(item_info)
            Offer.print.assert_called_once_with(item_info)

    def test_set_price_and_discount(self):
        with patch("item_info.BasicInfo.price", MagicMock()), patch(
            "item_info.Offer.calculate_discount_value", MagicMock(return_value=3.0)
        ):
            from item_info import ItemInfo

            item_info = ItemInfo("Test")
            item_info.set_price_and_discount(1.0)
            assert item_info.price == 1.0
            assert item_info.discount_value == 3.0


if __name__ == "__main__":
    main()
