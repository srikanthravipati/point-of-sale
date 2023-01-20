"""Holds information about user item."""
from typing import Dict

import numpy as np

from item_info import ItemInfo


class UserItem:
    """Holds no of items and total price after discount per item type."""

    def __init__(self):
        """Initialize an instance."""
        self.__count = np.uint64(0)
        self.__total = 0.0

    def print(self) -> None:
        """To debug."""
        print(f"Count : {self.__count}")
        print(f"Total : {self.__total}")

    @property
    def count(self) -> np.uint64:
        """Get item count."""
        return self.__count

    def incr_count_by_one(self):
        """Increase item count by one."""
        self.__count += np.uint64(1)

    @property
    def total(self) -> float:
        """Get total price."""
        return self.__total

    @total.setter
    def total(self, value: float) -> None:
        """Set total price.

        Arguments:
            value: value for total
        """
        self.__total = value

    def add_item_price_to_total(self, unit_price):
        """Update total by unit item price.

        Arguments:
            unit_price: One item price
        """
        self.total += unit_price

    def apply_discount(self, discount_value: float) -> None:
        """Subtract discount value from total.

        Arguments:
            discount_value: Discount amount
        """
        self.total -= discount_value

    def scan(self, item_info: ItemInfo) -> None:
        """To upon an item scan.

        | Increase item count by one
        | Add unit item price to total
        | Apply (calculate and subtract) discount, if valid, from total

        Arguments:
            item_info: Information about the scanned item
        """
        self.incr_count_by_one()
        self.add_item_price_to_total(item_info.price)
        if item_info.is_discount_valid(self.count):
            self.apply_discount(item_info.discount_value)


def user_items_total(user_items: Dict[str, UserItem]) -> float:
    """Compute total price.

    by summing total price of different item types.

    Arguments:
        user_items: User items scanned
    """
    total = 0.0
    for user_item in user_items.values():
        total += user_item.total
    return total
