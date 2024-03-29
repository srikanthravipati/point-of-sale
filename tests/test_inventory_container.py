from unittest.mock import MagicMock, patch


def test_set_inventory_price_and_discount_s():
    with patch("inventory_container.ItemInfo.set_price_and_discount", MagicMock()):
        from inventory_container import ItemInfo, set_inventory_price_and_discount_s

        item_price_s = {"A": 25, "B": 40, "P": 30}
        set_inventory_price_and_discount_s(item_price_s)
        assert ItemInfo.set_price_and_discount.call_count == 3


def test_update_inventory():
    with patch("inventory_container.ItemInfo.__init__", MagicMock(return_value=None)):
        from inventory_container import ItemInfo, update_inventory

        item_a = {"A": {"NAME": "Apple"}}
        update_inventory("A", item_a["A"])
        ItemInfo.__init__.assert_called_once_with("Apple")

        item_p = {"P": {"NAME": "Pear", "Discount": None}}
        update_inventory("P", item_p["P"])
        assert ItemInfo.__init__.call_count == 2
        ItemInfo.__init__.assert_called_with("Pear")

        item_b = {
            "B": {"NAME": "Banana", "DISCOUNT": {"N_ITEMS": 3, "COEFFS": [3.0, -100.0]}}
        }
        update_inventory("B", item_b["B"])
        assert ItemInfo.__init__.call_count == 3
        ItemInfo.__init__.assert_called_with("Banana", 0.0, True, 3, 3.0, -100.0)


def test_read_inventory_file():
    with patch(
        "inventory_container.load", MagicMock(return_value={"A": 1, "B": 2})
    ), patch("inventory_container.update_inventory", MagicMock()):
        from inventory_container import (
            load,
            read_inventory_file_and_update_inventory,
            update_inventory,
        )

        read_inventory_file_and_update_inventory("inventory.json")
        load.assert_called_once()
        assert update_inventory.call_count == 2
        update_inventory.assert_called_with("B", 2)
