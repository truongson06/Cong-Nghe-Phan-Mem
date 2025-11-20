from modules.order_detail import OrderDetail
from modules.db import save_db

class OrderManager:
    def __init__(self, db):
        self.db = db

    def checkout(self, user, cart_manager):
        """Create an order from the user's cart, reduce stock and clear the cart."""
        print("\n--- CHECKOUT ---")
        email = user["email"]

        cart = self.db.get("cart", {}).get(email, [])
        if not cart:
            print("Cart is empty!")
            return

        order_id = len(self.db.get("orders", [])) + 1
        order_items = []
        total = 0

        for item in cart:
            pid = item.get("product_id")
            qty = item.get("qty", 0)

            # find product
            prod = next((p for p in self.db.get("products", []) if p.get("id") == pid), None)
            if not prod:
                print(f"Product id {pid} not found, skipping item.")
                continue

            unit_price = prod.get("price", 0)
            subtotal = qty * unit_price

            od = OrderDetail(
                order_id=order_id,
                product_id=pid,
                quantity=qty,
                unit_price=unit_price
            )
            order_items.append(od.to_dict())
            total += subtotal

            # reduce stock if available
            if "stock" in prod:
                prod["stock"] = max(0, prod.get("stock", 0) - qty)

        order = {
            "order_id": order_id,
            "user": email,
            "items": order_items,
            "total": total
        }

        # ensure orders list exists
        if "orders" not in self.db:
            self.db["orders"] = []
        self.db["orders"].append(order)

        # clear cart
        if "cart" not in self.db:
            self.db["cart"] = {}
        self.db["cart"][email] = []

        print(f"Order created successfully! Total = {total}")
        save_db(self.db)

    def view_order_history(self, user):
        """Print the order history for a given user. Handles different order key formats."""
        print("\n--- ORDER HISTORY ---")
        orders = self.db.get("orders", [])
        found = False
        for o in orders:
            # support either 'user' key and 'order_id' or legacy 'id'
            if o.get("user") == user.get("email"):
                oid = o.get("order_id") or o.get("id")
                total = o.get("total")
                print(f"Order {oid} - Total: {total}")
                found = True

        if not found:
            print("No orders found for this user.")
