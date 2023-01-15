from typing import Dict

import numpy as np

from item_info import ItemInfo


class Item:
    """
    Holds number of items and total price \n
    for user picked items of an item-code \n
    __count: numpy.uint64 \n
    __total: float \n
    """

    __count: np.uint64
    __total: float

    def __init__(self):
        self.__count = np.uint64(0)
        self.__total = 0.0

    def print(self) -> None:
        print(f"Count : {self.__count}")
        print(f"Total : {self.__total}")

    @property
    def count(self) -> np.uint64:
        return self.__count

    def incr_count_by_one(self):
        self.__count += np.uint64(1)

    @property
    def total(self) -> float:
        return self.__total

    @total.setter
    def total(self, value: float) -> None:
        self.__total = value

    def add_item_price_to_total(self, unit_price):
        self.total += unit_price

    def apply_discount(self, discount: float) -> None:
        self.total -= discount

    def scan_item(self, item_info: ItemInfo) -> None:
        self.incr_count_by_one()
        self.add_item_price_to_total(item_info.price)
        if item_info.is_valid(self.count):
            self.apply_discount(item_info.discount)


def items_total(items: Dict[str, Item]) -> float:
    total = 0.0
    for item_code in items:
        total += items[item_code].total
    return total
