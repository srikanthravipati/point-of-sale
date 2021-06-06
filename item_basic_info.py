class BasicInfo:
    """
    Holds basic information of an item-code \n
    __name: str \n
    __price: float
    """

    __name: str
    __price: float

    def __init__(self, name: str, price: float = 0.0):
        self.__name = name
        self.__price = price

    def print(self) -> None:
        print(f"Name  : {self.__name}")
        print(f"Price : {self.__price} Pence")

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price: float) -> None:
        self.__price = price
