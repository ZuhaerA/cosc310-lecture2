"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # TODO: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        #   if not item["available"]:   raise OutOfStockError(...)
        if qty < 1:
            raise ValueError("The quantity entered is less than 1")
        elif not item["available"]:
            raise OutOfStockError("The item is out of stock")
        else:
            for line in self.lines: 
                if line["id"] == item["id"]:
                    line["qty"] += qty
                    return
            
            #If there is no matching quantity, then it appends the item to the list
            line = item.copy()
            line["qty"] = qty
            self.lines.append(line) 

    def remove_item(self, item_id: int) -> None:
        # TODO: raise KeyError if the item is not in the cart
        if not any(line["id"] == item_id for line in self.lines):
            raise KeyError("This item is not in the cart")
        else:
            self.lines = [line for line in self.lines if line["id"] != item_id]

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    # TODO: demonstrate each rejection with try/except and a readable message.
    # Example:
    # try:
    #     cart.add_item(gyoza, 0)
    # except ValueError as e:
    #     print(f"Rejected: {e}")

