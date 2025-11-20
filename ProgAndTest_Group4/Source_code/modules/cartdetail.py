class CartDetail:
    def __init__(self, product_id, quantity, unit_price):

        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal = quantity * unit_price

    def to_dict(self):
        """Returns the cart detail as a dictionary for storage."""
        return {
            "product_id": self.product_id,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "subtotal": self.subtotal
        }
