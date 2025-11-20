from modules.user import UserManager
from modules.product import ProductManager
from modules.cart import CartManager
from modules.order import OrderManager
from modules.staff import StaffManager
from modules.admin import AdminManager
from modules.category import CategoryManager
import json

def load_db():
    try:
        with open("database.json", "r") as f:
            db = json.load(f)
    except:
        db = {
            "users": [],
            "products": [],
            "orders": [],
            "cart": {}
        }

    if not db["products"]:
        db["products"] = [
            {"id": 1, "name": "iPhone 14 Pro Max", "price": 28990000, "stock": 10},
            {"id": 2, "name": "Samsung Galaxy S23 Ultra", "price": 25990000, "stock": 8},
            {"id": 3, "name": "MacBook Air M2", "price": 28990000, "stock": 5},
            {"id": 4, "name": "Chuột Logitech G102", "price": 390000, "stock": 25},
            {"id": 5, "name": "Tai nghe Sony WH-1000XM4", "price": 4990000, "stock": 12}
        ]
        print("Sample products loaded!")

    return db


def save_db(db):
    with open("database.json", "w") as f:
        json.dump(db, f, indent=4)

def main():
    db = load_db()
    user_manager = UserManager(db)
    product_manager = ProductManager(db)
    cart_manager = CartManager(db)
    order_manager = OrderManager(db)
    staff_manager = StaffManager(db)
    admin_manager = AdminManager(db)
    category_manager = CategoryManager(db)


    while True:
        try:
            print("\n=== MINI E-COMMERCE SYSTEM ===")
            print("1. Customer")
            print("2. Admin")
            print("3. Staff")
            print("0. Exit")

            choice = input("Choose role: ")

            if choice == "1":
                user_manager.customer_menu(product_manager, cart_manager, order_manager)
            elif choice == "2":
                admin_manager.admin_menu(product_manager, user_manager, order_manager, category_manager)
            elif choice == "3":
                staff_manager.staff_menu(order_manager, product_manager)
            elif choice == "0":
                print("Thank you for using our system!")
                break
            else:
                print("Invalid choice. Please try again.")

            save_db(db)
        except Exception as e:
            print(f"Error: {e}")
            save_db(db)

if __name__ == "__main__":
    main()
