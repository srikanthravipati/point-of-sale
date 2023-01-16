class BasicInfo:
    """
    Holds basic information of an item-code \n
    __name: str \n
    __price: float
    """

    __name: str
    __price: float

    def __init__(self, name: str, price: float = 0.0):
        self.name = name
        self.price = price

    def print(self) -> None:
        print(f"Name  : {self.name}")
        print(f"Price : {self.price} Pence")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        self.__price = value
