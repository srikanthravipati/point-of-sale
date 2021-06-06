from sys import float_info

from checkout import Checkout, checkout

user_items = ["B", "A", "B", "P", "B"]
item_price_s = {"A": 25, "B": 40, "P": 30}

# version 1.0
total = checkout(user_items, item_price_s)

assert abs(total - 155.0) < float_info.epsilon

# version 2.0
Checkout_ = Checkout(item_price_s)

for item in user_items:
    Checkout_.scan_item(item)

assert abs(Checkout_.total() - 155.0) < float_info.epsilon
