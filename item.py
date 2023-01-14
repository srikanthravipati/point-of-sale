from typing import Dict

import numpy as np

from item_basic_info import BasicInfo
from item_offer import Offer


def offer_eligible(user_n_items: np.uint64, offer_n_items: np.uint64) -> bool:
    if user_n_items <= 0:
        offer_eligible_ = False
    else:
        offer_eligible_ = np.mod(user_n_items, offer_n_items) == 0
    return offer_eligible_


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

    def scan_item(self, basic_info: BasicInfo, offer: Offer) -> None:
        self.incr_count_by_one()
        self.add_item_price_to_total(basic_info.price)

        if offer.running:
            if offer_eligible(self.count, offer.n_items):
                self.apply_discount(offer.discount)


def items_total(items: Dict[str, Item]) -> float:
    total = 0.0
    for item_code in items:
        total += items[item_code].total
    return total
