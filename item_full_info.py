from item_basic_info import BasicInfo
from item_offer import Offer


class FullInfo:
    """
    Holds BasicInfo and Offer for an item-code
    basic_info: BasicInfo
    offer: Offer
    """

    basic_info: BasicInfo
    offer: Offer

    def __init__(self, basic_info: BasicInfo, offer: Offer):
        self.basic_info = basic_info
        self.offer = offer

    def print(self) -> None:
        print("\n")
        self.basic_info.print()
        self.offer.print()

    def set_price_and_discount(self, price: float) -> None:
        self.basic_info.price = price
        self.offer.discount = self.offer.calculate_discount(price)
