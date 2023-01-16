from typing import Dict, List

from inventory_container import INVENTORY_ITEMS, set_inventory_price_and_discount_s
from item_info import ItemInfo
from user_item import UserItem, user_items_total


def update_user_items(
    item_code: str, user_items: Dict[str, UserItem], item_info: ItemInfo
) -> None:
    if item_code not in user_items:
        user_items[item_code] = UserItem()
    user_items[item_code].scan(item_info)


def item_scanned(item_code: str, user_items: Dict[str, UserItem]) -> None:
    if item_code in INVENTORY_ITEMS:
        update_user_items(item_code, user_items, INVENTORY_ITEMS[item_code])
    else:
        raise KeyError(f"Unexpected Item Code : {item_code}")


def checkout(user_item_codes: List[str], item_price_s: Dict[str, float]) -> float:
    """
    For each distinct item-code in user_items \n
    update items[item-code](: Item) __count and __total info
    :return: total
    """
    user_items: Dict[str, UserItem] = {}
    set_inventory_price_and_discount_s(item_price_s)

    for scanned_item_code in user_item_codes:
        item_scanned(scanned_item_code, user_items)

    total = user_items_total(user_items)
    return total


class Checkout:
    """Holds basket items count and total for each \n item-code available in
    the inventory."""

    def __init__(self, item_price_s: Dict[str, float]):
        self.user_items: Dict[str, UserItem] = {}
        set_inventory_price_and_discount_s(item_price_s)

    def update_user_items(self, item_code: str, item_info: ItemInfo) -> None:
        if item_code not in self.user_items:
            self.user_items[item_code] = UserItem()
        self.user_items[item_code].scan(item_info)

    def scan(self, item_code: str) -> None:
        if item_code in INVENTORY_ITEMS:
            self.update_user_items(item_code, INVENTORY_ITEMS[item_code])
        else:
            raise KeyError(f"Unexpected Item Code : {item_code}")

    def total(self) -> float:
        return user_items_total(self.user_items)
