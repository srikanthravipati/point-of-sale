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
    __reduction: float

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
        self.__reduction = 0.0

    def print(self) -> None:
        if self.__running:
            print(
                f"Offer reduction for {self.__n_items} "
                + f"is : {self.__reduction} Pence"
            )

    def is_running(self) -> bool:
        return self.__running

    def get_n_items(self) -> np.uint64:
        return self.__n_items

    def get_reduction(self) -> float:
        return self.__reduction

    def set_reduction(self, price: float):
        reduction = self.__coeffs[0] * price + self.__coeffs[1]
        assert reduction >= 0.0
        self.__reduction = reduction
