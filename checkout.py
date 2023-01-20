"""Holds checkout and related contents."""
from typing import Dict, List

from inventory_container import INVENTORY_ITEMS, set_inventory_price_and_discount_s
from item_info import ItemInfo
from user_item import UserItem, user_items_total


def update_user_items(
    item_code: str, user_items: Dict[str, UserItem], item_info: ItemInfo
) -> None:
    """Include currently scanned item to user items.

    Arguments:
        item_code: Scanned item code
        user_items: Already scanned user items
        item_info: Information about the scanned item
    """
    if item_code not in user_items:
        user_items[item_code] = UserItem()
    user_items[item_code].scan(item_info)


def item_scanned(item_code: str, user_items: Dict[str, UserItem]) -> None:
    """To do upon an item scan by user.

    Update user items if the scanned item code is valid,
    raise Error otherwise.

    Arguments:
        item_code: Code of the current scanned item
        user_items: Already scanned user items

    Raises:
        KeyError: If the scanned item code is not in the inventory
    """
    if item_code in INVENTORY_ITEMS:
        update_user_items(item_code, user_items, INVENTORY_ITEMS[item_code])
    else:
        raise KeyError(f"Unexpected Item Code : {item_code}")


def checkout(user_item_codes: List[str], item_price_s: Dict[str, float]) -> float:
    """Add each scanned item to the user items and update accordingly.

    Arguments:
        user_item_codes: Codes of the items that user picked
        item_price_s: Item prices (associated with item_code)

    Return:
        Total price user need to pay after accounting for the discounts.
    """
    user_items: Dict[str, UserItem] = {}
    set_inventory_price_and_discount_s(item_price_s)

    for scanned_item_code in user_item_codes:
        item_scanned(scanned_item_code, user_items)

    total = user_items_total(user_items)
    return total


class Checkout:
    """Manages user checkout process."""

    def __init__(self, item_price_s: Dict[str, float]):
        """Set inventory price and discount and initialise user_items.

        Arguments:
            item_price_s: Item prices (associated with item_code)
        """
        self.user_items: Dict[str, UserItem] = {}
        set_inventory_price_and_discount_s(item_price_s)

    def update_user_items(self, item_code: str, item_info: ItemInfo) -> None:
        """Update user items to include scanned item.

        Arguments:
            item_code: Scanned item code
            item_info: Information about the scanned item
        """
        if item_code not in self.user_items:
            self.user_items[item_code] = UserItem()
        self.user_items[item_code].scan(item_info)

    def scan(self, item_code: str) -> None:
        """To do upon an item scan by user.

        Update user items if the scanned item code is valid,
        raise Error otherwise.

        Arguments:
            item_code: Code of the current scanned item

        Raises:
           KeyError: If the scanned item code is not in the inventory
        """
        if item_code in INVENTORY_ITEMS:
            self.update_user_items(item_code, INVENTORY_ITEMS[item_code])
        else:
            raise KeyError(f"Unexpected Item Code : {item_code}")

    def total(self) -> float:
        """Total price user has to pay after discount."""
        return user_items_total(self.user_items)
