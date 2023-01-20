"""Holds information about item offer."""
import numpy as np
from numpy import float64, polyval
from numpy.typing import NDArray

UINT64_MAX = np.iinfo(np.uint64).max


class Offer:
    """Holds information about multibuy offer."""

    def __init__(
        self,
        discount_running: bool = False,
        discount_n_items: np.uint64 = UINT64_MAX,
        discount_coeff_a: float = 0.0,
        discount_coeff_b: float = 0.0,
    ):
        """Initialise an instance.

        Discount calculation is casted as `discount = coeff_a * price + coeff_b`

        Arguments:
            discount_running: True if there is multibuy offer, False otherwise
            discount_n_items: No. of items user needs to buy for discount to be valid
            discount_coeff_a: One of the coefficients to calculate discount
            discount_coeff_b: One of the coefficients to calculate discount
        """
        self.__discount_running = discount_running
        self.__discount_n_items = discount_n_items
        self.__discount_coeffs = np.array([discount_coeff_a, discount_coeff_b])
        self.__discount_value = 0.0

    def print(self) -> None:
        """To debug."""
        if self.__discount_running:
            print(
                f"Offer discount for {self.__discount_n_items} "
                + f"is : {self.__discount_value} Pence"
            )

    @property
    def discount_running(self) -> bool:
        """Get discount_running."""
        return self.__discount_running

    @property
    def discount_n_items(self) -> np.uint64:
        """Get number of items to avail discount."""
        return self.__discount_n_items

    @property
    def discount_coeffs(self) -> NDArray[float64]:
        """Get coeffs to calculate discount."""
        return self.__discount_coeffs

    @property
    def discount_value(self) -> float:
        """Get discount."""
        return self.__discount_value

    @discount_value.setter
    def discount_value(self, value: float) -> None:
        """Set discount.

        Arguments:
            value: Value for discount.
        """
        self.__discount_value = value

    def calculate_discount_value(self, price: float) -> float:
        """Calculate discount.

        `discount = coeff_a * price + coeff_b`

        Arguments:
            price: Item price
        """
        if self.discount_running:
            return polyval(self.discount_coeffs, price)
        else:
            return 0.0

    def is_discount_valid(self, n_items: np.uint64) -> bool:
        """Check if discount is valid or not.

        Arguments:
            n_items: Number of items added to the cart
        """
        if not self.discount_running or (self.discount_running and n_items <= 0):
            return False
        else:
            return n_items % self.discount_n_items == 0
