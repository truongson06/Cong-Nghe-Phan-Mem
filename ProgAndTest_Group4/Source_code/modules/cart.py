from modules.db import save_db
from valid.validCart import ValidCart
class CartManager:
    def __init__(self, db):
        self.db = db
        if "cart" not in db:
            db["cart"] = {}

    def add_to_cart(self, user):
        try:
            pid = int(input("Product ID: "))
            quantity = int(input("Quantity: "))
            ValidCart().Valid_quality(quantity)
            if quantity > self.db["products"][pid-1]["stock"]:
                raise ValueError("Not enough stock available.")
        except ValueError as e:
            print(f"Error: {e}")
            return
        except:
            print("Invalid input. Please try again.")
            return
        if user["email"] not in self.db["cart"]:
            self.db["cart"][user["email"]] = []

        self.db["cart"][user["email"]].append({
            "product_id": pid,
            "qty": quantity
        })
        print("Added to cart!")
        save_db(self.db)

    def view_cart(self, user):
        print("\n--- YOUR CART ---")
        cart = self.db["cart"].get(user["email"], [])
        for item in cart:
            print(f"Product {item['product_id']} - Qty: {item['qty']}")

    def remove_from_cart(self, user):
        try:
            pid = int(input("Product ID to remove: "))
        except:
            print("Invalid input. Please try again.")
            return
        if len(self.db["cart"].get(user["email"], [])) == 0:
            print("Cart is empty.")
            return
        cart = self.db["cart"].get(user["email"], [])
        new_cart = [item for item in cart if item["product_id"] != pid]
        self.db["cart"][user["email"]] = new_cart
        print("Item removed from cart.")
        save_db(self.db)
