"""Holds inventory container and related contents."""
from typing import Any, Dict

from json5 import load

from item_info import ItemInfo

INVENTORY_FILE = "inventory.json"
INVENTORY_ITEMS: Dict[str, ItemInfo] = {}


def set_inventory_price_and_discount_s(item_price_s: Dict[str, float]) -> None:
    """Set price and discount for INVENTORY_ITEMS.

    Arguments:
        item_price_s: Item prices (associated with item code)
    """
    for item_code in item_price_s:
        price = item_price_s[item_code]
        INVENTORY_ITEMS[item_code].set_price_and_discount(price)


def update_inventory(item_code: str, item_info: Any) -> None:
    """Update inventory for the given item (code).

    If the inventory information does not contain
    anything about DISCOUNT for an item or number
    of items as zero to avail discount that means
    there is no discount running for that particular
    item.

    Arguments:
        item_code: Item code
        item_info: Information about the item
    """
    name = item_info["NAME"]
    if "DISCOUNT" not in item_info or item_info["DISCOUNT"].get("N_ITEMS", 0) == 0:
        INVENTORY_ITEMS[item_code] = ItemInfo(name)
    else:
        discount = item_info["DISCOUNT"]
        INVENTORY_ITEMS[item_code] = ItemInfo(
            name,
            0.0,
            True,
            discount["N_ITEMS"],
            discount["COEFFS"][0],
            discount["COEFFS"][1],
        )


def read_inventory_file_and_update_inventory(inventory_file: str) -> None:
    """Read inventory file and update inventory.

    Arguments:
        inventory_file: File containing inventory information
    """
    with open(inventory_file) as inventory:
        inventory_dict = load(inventory)
        for item_code, item_info in inventory_dict.items():
            update_inventory(item_code, item_info)


# Read inventory file. Raise Error if the file could not be found.
try:
    read_inventory_file_and_update_inventory(INVENTORY_FILE)
except FileNotFoundError:
    raise FileNotFoundError(f"Inventory file {INVENTORY_FILE} is not found")
