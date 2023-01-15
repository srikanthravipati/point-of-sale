import numpy as np

UINT64_MAX = np.iinfo(np.uint64).max


class Offer:
    """Holds offer related information for an item-code \n
    __running: bool \n
    __n_items: numpy.uint64 (Offer eligibility freq) \n
    __coeffs: np.ndarray (Coeffs that gives reduction as a fn of price) \n
    __reduction: float (__coeffs[0] * price + __coeffs[1])
    """

    __running: bool
    __n_items: np.uint64
    __coeffs: np.ndarray
    __discount: float

    def __init__(
        self,
        running: bool = False,
        n_items: np.uint64 = UINT64_MAX,
        coeff_a: float = 0.0,
        coeff_b: float = 0.0,
    ):
        self.__running = running
        self.__n_items = n_items
        self.__coeffs = np.array([coeff_a, coeff_b])
        self.__discount = 0.0

    def print(self) -> None:
        if self.__running:
            print(
                f"Offer reduction for {self.__n_items} "
                + f"is : {self.__reduction} Pence"
            )

    @property 
    def running(self) -> bool:
        return self.__running

    @property
    def n_items(self) -> np.uint64:
        return self.__n_items

    @property
    def discount(self) -> float:
        return self.__discount

    def calculate_discount(self, price: float) -> float:
        if self.running:
            return self.__coeffs[0] * price + self.__coeffs[1]
        else:
            return 0.0

    @discount.setter
    def discount(self, value: float) -> float:
        self.__discount = value

    def is_valid(self, n_items: np.uint64) -> bool:
        if self.running:
            if n_items <= 0:
                return False
            else:
                return n_items % self.n_items == 0
        else:
            return False
