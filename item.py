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
    for user picked items an item-code \n
    __count: numpy.uint64 \n
    __total: float \n
    """

    __count: np.uint64
    __total: float

    def __init__(self):
        self.__count = np.uint64(0)
        self.__total = 0.0

    def get_count(self) -> np.uint64:
        return self.__count

    def get_total(self) -> float:
        return self.__total

    def print(self) -> None:
        print(f"Count : {self.__count}")
        print(f"Total : {self.__total}")

    def increase_one_count(self) -> None:
        self.__count += np.uint64(1)

    def increase_total_by_unit_price(self, price: float) -> None:
        self.__total += price

    def apply_offer(self, reduction: float) -> None:
        self.__total -= reduction

    def scan_item(self, basic_info: BasicInfo, offer: Offer) -> None:
        self.increase_one_count()
        self.increase_total_by_unit_price(basic_info.get_price())

        if offer.is_running():
            if offer_eligible(self.__count, offer.get_n_items()):
                self.apply_offer(offer.get_reduction())


def items_total(items: Dict[str, Item]) -> float:
    total = 0.0
    for item_code in items:
        total += items[item_code].get_total()
    return total
