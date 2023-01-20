"""Holds item information."""
from numpy import uint64

from item_basic_info import BasicInfo
from item_offer import Offer


class ItemInfo(BasicInfo, Offer):
    """Inherit BasicInfo and Offer."""

    def __init__(
        self,
        name: str,
        price: float = 0.0,
        discount_running: bool = False,
        discount_n_items: uint64 = 0,
        discount_coeff_a: float = 0.0,
        discount_coeff_b: float = 0.0,
    ):
        """Initialise an instance.

        Arguments:
            name: Name of the item.
            price: Price of the item.
            discount_running: True if there is multibuy offer, False otherwise
            discount_n_items: No. of items user needs to buy for discount to be valid
            discount_coeff_a: One of the coefficients to calculate discount
            discount_coeff_b: One of the coefficients to calculate discount
        """
        BasicInfo.__init__(self, name, price)
        Offer.__init__(
            self, discount_running, discount_n_items, discount_coeff_a, discount_coeff_b
        )

    def print(self) -> None:
        """To debug."""
        print("\n")
        BasicInfo.print(self)
        Offer.print(self)

    def set_price_and_discount(self, price: float) -> None:
        """Interface to set an item price and discount.

        Arguments:
            price: Item price
        """
        self.price = price
        self.discount_value = super(ItemInfo, self).calculate_discount_value(price)
