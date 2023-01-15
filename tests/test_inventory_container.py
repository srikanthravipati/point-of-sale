from unittest.mock import MagicMock, patch

item_price_s = {"A": 25, "B": 40, "P": 30}

def test_set_inventory_price_and_discount_s():
    with patch("inventory_container.ItemInfo.set_price_and_discount", MagicMock()):
        from inventory_container import ItemInfo, set_inventory_price_and_discount_s

        set_inventory_price_and_discount_s(item_price_s)
        assert ItemInfo.set_price_and_discount.call_count == 3
