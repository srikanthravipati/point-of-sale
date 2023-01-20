"""Holds item basic information."""


class BasicInfo:
    """Holds basic information of an item."""

    def __init__(self, name: str, price: float = 0.0):
        """Initialise an instance.

        Arguments:
            name: Name of the item.
            price: Price of the item.
        """
        self.name = name
        self.price = price

    def print(self) -> None:
        """To debug."""
        print(f"Name  : {self.name}")
        print(f"Price : {self.price} Pence")

    @property
    def name(self) -> str:
        """Get name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Set name.

        Arguments:
            value: Value for name
        """
        self.__name = value

    @property
    def price(self) -> float:
        """Get price."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Set price.

        Arguments:
            value: Value for price
        """
        self.__price = value
