import numpy as np
from numpy import float64, polyval
from numpy.typing import NDArray

UINT64_MAX = np.iinfo(np.uint64).max


class Offer:
    """Holds offer related information for an item-code \n
    __discount_running: bool \n
    __discount_n_items: numpy.uint64 (Offer eligibility freq) \n
    __discount_coeffs: np.ndarray (Coeffs that gives reduction as a fn of price) \n
    __discount_value: float (__coeffs[0] * price + __coeffs[1])
    """

    def __init__(
        self,
        discount_running: bool = False,
        discount_n_items: np.uint64 = UINT64_MAX,
        discount_coeff_a: float = 0.0,
        discount_coeff_b: float = 0.0,
    ):
        self.__discount_running = discount_running
        self.__discount_n_items = discount_n_items
        self.__discount_coeffs = np.array([discount_coeff_a, discount_coeff_b])
        self.__discount_value = 0.0

    def print(self) -> None:
        if self.__discount_running:
            print(
                f"Offer discount for {self.__discount_n_items} "
                + f"is : {self.__discount_value} Pence"
            )

    @property
    def discount_running(self) -> bool:
        return self.__discount_running

    @property
    def discount_n_items(self) -> np.uint64:
        return self.__discount_n_items

    @property
    def discount_coeffs(self) -> NDArray[float64]:
        return self.__discount_coeffs

    @property
    def discount_value(self) -> float:
        return self.__discount_value

    def calculate_discount_value(self, price: float) -> float:
        if self.discount_running:
            return polyval(self.discount_coeffs, price)
        else:
            return 0.0

    @discount_value.setter
    def discount_value(self, value: float) -> float:
        self.__discount_value = value

    def is_discount_valid(self, n_items: np.uint64) -> bool:
        if not self.discount_running or (self.discount_running and n_items <= 0):
            return False
        else:
            return n_items % self.discount_n_items == 0
