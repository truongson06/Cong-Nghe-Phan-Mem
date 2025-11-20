class ValidProduct:
    def Valid_price(self, price):
        if price < 0:
            raise ValueError("Price must be greater than zero.")
    def Valid_stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative.")