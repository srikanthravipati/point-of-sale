from typing import Dict, List

from item import Item, items_total
from item_full_info import FullInfo
from read_inventory import read_inventory

inventory_file = open("Inventory.txt", "r")

INVENTORY_ITEMS: Dict[str, FullInfo] = {}
read_inventory(inventory_file, INVENTORY_ITEMS)


def set_inventory_price_and_reduction_s(item_price_s: Dict[str, float]) -> None:
    """
    Take price for each item-code from item_price_s \n
    and set price and reduction for INVENTORY_ITEMS
    """
    for item_code in item_price_s:
        price = item_price_s[item_code]
        INVENTORY_ITEMS[item_code].set_price_and_reduction(price)


def checkout(user_items: List[str], item_price_s: Dict[str, float]) -> float:
    """
    For each distinct item-code in user_items \n
    update items[item-code](: Item) __count and __total info
    :return: total
    """
    items: Dict[str, Item] = {}
    set_inventory_price_and_reduction_s(item_price_s)

    for item_code in user_items:
        if item_code in INVENTORY_ITEMS:

            if item_code not in items:
                items[item_code] = Item()

            items[item_code].scan_item(
                INVENTORY_ITEMS[item_code].basic_info, INVENTORY_ITEMS[item_code].offer
            )
        else:
            raise KeyError(f"Unexpected Item Code : {item_code}")

    total = items_total(items)
    return total


class Checkout:
    items: Dict[str, Item]

    def __init__(self, item_price_s: Dict[str, float]):
        self.items = {}
        set_inventory_price_and_reduction_s(item_price_s)

    def scan_item(self, item_code):
        if item_code in INVENTORY_ITEMS:

            if item_code not in self.items:
                self.items[item_code] = Item()

            self.items[item_code].scan_item(
                INVENTORY_ITEMS[item_code].basic_info, INVENTORY_ITEMS[item_code].offer
            )
        else:
            raise KeyError(f"Unexpected Item Code : {item_code}")

    def total(self) -> float:
        return items_total(self.items)
