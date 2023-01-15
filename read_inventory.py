from typing import Dict

import numpy as np

from item_basic_info import BasicInfo
from item_info import ItemInfo
from item_offer import Offer

UINT64_MAX = np.iinfo(np.uint64).max


def read_inventory(inventory_file, inventory_items: Dict[str, ItemInfo]):
    """
    Read information for every item-code in the inventory \n
    and add it to the inventory_items \n
    :return: updated inventory_items
    """

    EXPECTED_N_COL = 5

    line = inventory_file.readline()

    while True:
        line = inventory_file.readline()
        if not line:
            break
        split_line = line.split()
        n_col = len(split_line)

        if n_col > 0:
            if n_col != EXPECTED_N_COL:
                raise Exception(
                    "Inventory data is expected to have "
                    + f"{EXPECTED_N_COL}, not {n_col}"
                )
            item_code = split_line[0]
            item_name = split_line[1]
            offer_n_items = np.uint64(split_line[2])

            offer_running = False
            if offer_n_items > 0:
                offer_running = True
            else:
                offer_n_items = UINT64_MAX

            offer_coeff_a = float(split_line[3])
            offer_coeff_b = float(split_line[4])

            inventory_items[item_code] = ItemInfo(
                item_name,
                0.0,
                offer_running,
                offer_n_items,
                offer_coeff_a,
                offer_coeff_b,
            )
