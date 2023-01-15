from typing import Dict, List

from inventory_container import INVENTORY_ITEMS
from user_item import UserItem, user_items_total
from read_inventory import read_inventory

INVENTORY_FILE_NAME = "inventory.txt"

try:
    inventory_file = open(INVENTORY_FILE_NAME, "r")
    read_inventory(inventory_file, INVENTORY_ITEMS)
except FileNotFoundError:
    print(f"Inventory file {INVENTORY_FILE_NAME} is not found")
    raise


def set_inventory_price_and_discount_s(item_price_s: Dict[str, float]) -> None:
    """
    Take price for each item-code from item_price_s \n
    and set price and reduction for INVENTORY_ITEMS
    """
    for item_code in item_price_s:
        price = item_price_s[item_code]
        INVENTORY_ITEMS[item_code].set_price_and_discount(price)


def checkout(user_items: List[str], item_price_s: Dict[str, float]) -> float:
    """
    For each distinct item-code in user_items \n
    update items[item-code](: Item) __count and __total info
    :return: total
    """
    items: Dict[str, UserItem] = {}
    set_inventory_price_and_discount_s(item_price_s)

    for item_code in user_items:
        if item_code in INVENTORY_ITEMS:

            if item_code not in items:
                items[item_code] = UserItem()

            items[item_code].scan_item(INVENTORY_ITEMS[item_code])
        else:
            raise KeyError(f"Unexpected Item Code : {item_code}")

    total = user_items_total(items)
    return total


class Checkout:
    """
    Holds basket items count and total for each \n
    item-code available in the inventory
    """

    items: Dict[str, UserItem]

    def __init__(self, item_price_s: Dict[str, float]):
        self.items = {}
        set_inventory_price_and_discount_s(item_price_s)

    def scan_item(self, item_code: str):
        if item_code in INVENTORY_ITEMS:

            if item_code not in self.items:
                self.items[item_code] = UserItem()

            self.items[item_code].scan_item(INVENTORY_ITEMS[item_code])
        else:
            raise KeyError(f"Unexpected Item Code : {item_code}")

    def total(self) -> float:
        return user_items_total(self.items)
