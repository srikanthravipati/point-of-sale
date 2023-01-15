from typing import Dict

from item_info import ItemInfo

INVENTORY_ITEMS: Dict[str, ItemInfo] = {}

def set_inventory_price_and_discount_s(item_price_s: Dict[str, float]) -> None:
    """
    Take price for each item-code from item_price_s \n
    and set price and reduction for INVENTORY_ITEMS
    """
    for item_code in item_price_s:
        price = item_price_s[item_code]
        INVENTORY_ITEMS[item_code].set_price_and_discount(price)