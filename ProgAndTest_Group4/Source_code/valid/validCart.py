class ValidCart:
    def Valid_quality(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        