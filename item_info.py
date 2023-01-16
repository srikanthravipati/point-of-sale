from numpy import uint64
from item_basic_info import BasicInfo
from item_offer import Offer


class ItemInfo(BasicInfo, Offer):
    """
    Holds BasicInfo and Offer for an item-code
    basic_info: BasicInfo
    offer: Offer
    """

    def __init__(
        self,
        name: str,
        price: float = 0.0,
        discount_running: bool = False,
        discount_n_items: uint64 = 0,
        discount_coeff_a: float = 0.0,
        discount_coeff_b: float = 0.0,
    ):
        BasicInfo.__init__(self, name, price)
        Offer.__init__(
            self, discount_running, discount_n_items, discount_coeff_a, discount_coeff_b
        )

    def print(self) -> None:
        print("\n")
        BasicInfo.print(self)
        Offer.print(self)

    def set_price_and_discount(self, price: float) -> None:
        self.price = price
        self.discount_value = super(ItemInfo, self).calculate_discount_value(price)
