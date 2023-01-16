from typing import Any, Dict

from json5 import load

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


INVENTORY_FILE_NAME = "inventory.json"

def update_inventory(item_code: str, item_info: Any) -> None:
    name = item_info['NAME']
    if 'DISCOUNT' not in item_info or item_info['DISCOUNT'].get('N_ITEMS', 0) == 0:
        INVENTORY_ITEMS[item_code] = ItemInfo(name)
    else:
        discount = item_info['DISCOUNT']
        INVENTORY_ITEMS[item_code] = ItemInfo(name, 0.0, True, discount['N_ITEMS'], discount['COEFFS'][0], discount['COEFFS'][1])


try:
    with open(INVENTORY_FILE_NAME) as inventory:
        inventory_dict = load(inventory)
        for item_code, item_info in inventory_dict.items():
            update_inventory(item_code, item_info)
except FileNotFoundError:
    print(f"Inventory file {INVENTORY_FILE_NAME} is not found")
    raise