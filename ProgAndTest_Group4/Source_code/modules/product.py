from modules.db import save_db
from valid.validProduct import ValidProduct
class ProductManager:
    def __init__(self, db):
        self.db = db

    def view_products(self):
      print("\n=== PRODUCT LIST ===")
      for p in self.db["products"]:
        print(f"[{p['id']}] {p['name']}")
        print(f"    Price: {p['price']} VND")
        print(f"    Stock: {p['stock']}")
        if 'description' in p:
            print(f"    Description: {p['description']}")
        print("-----------------------------------")



    def search_product(self):
        key = input("Search keyword: ").lower()
        results = [p for p in self.db["products"] if key in p["name"].lower()]
        for p in results:
            print(f"{p['id']} - {p['name']} - ${p['price']}")

    def add_product(self):
        print("\n--- ADD PRODUCT ---")
        try:
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            description = input("Description: ")
            pid = len(self.db["products"]) + 1
            ValidProduct().Valid_price(price)
            ValidProduct().Valid_stock(stock)
        except ValueError as e:
            print(f"Error: {e}")
            return
        except:
            print("Invalid input. Please try again.")
            return
        self.db["products"].append({
            "id": pid,
            "name": name,
            "price": price,
            "stock": stock,
            "description": description
        })

        print("Product added successfully!")

        save_db(self.db)

    def update_product(self):
        pid = int(input("Product ID to update: "))
        for p in self.db["products"]:
            if p["id"] == pid:
                try:
                    p["name"] = input("New name: ")
                    p["price"] = float(input("New price: "))
                    p["stock"] = int(input("New stock: "))
                    ValidProduct().Valid_price(p["price"])
                    ValidProduct().Valid_stock(p["stock"])
                except ValueError as e:
                    print(f"Error: {e}")
                    return
                except:
                    print("Invalid input. Please try again.")
                    return
                print("Product updated.")
                save_db(self.db) 
                return
        print("Product not found.")
        save_db(self.db)   
    def view_product_detail(self):
        try:
            pid = int(input("Enter Product ID to view details: "))
        except:
            print("Invalid input. Please try again.")
            return
        for p in self.db["products"]:
            if p["id"] == pid:
                print(f"Product ID: {p['id']}")
                print(f"Name: {p['name']}")
                print(f"Price: {p['price']} VND")
                print(f"Stock: {p['stock']}")
                if 'description' in p:
                    print(f"Description: {p['description']}")
                return
        print("Product not found.")
