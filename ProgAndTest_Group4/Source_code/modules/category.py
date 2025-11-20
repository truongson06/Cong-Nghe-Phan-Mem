from modules.db import save_db
class CategoryManager:
    def __init__(self, db):
        self.db = db
        if "categories" not in db:

            db["categories"] = []

    def add_category(self):
        """Adds a new category."""
        print("\n--- ADD CATEGORY ---")
        name = input("Category Name: ")
        description = input("Description (optional): ")

        cid = len(self.db["categories"]) + 1
        self.db["categories"].append({
            "id": cid,
            "name": name,
            "description": description
        })
        print(f"Category '{name}' added with ID: {cid}!")
        save_db(self.db)

    def view_categories(self):

        print("VIEW === CATEGORY LIST ===")
        if not self.db["categories"]:
            print("No categories found.")
            return

        for c in self.db["categories"]:
            print(f"[{c['id']}] {c['name']}")
            if c.get("description"):
                print(f"   Description: {c['description']}")
            print("-----------------------------------")

    def search_category(self):
        """Searches for categories by name."""
        key = input("Search keyword: ").lower()
        results = [c for c in self.db["categories"] if key in c["name"].lower()]
        for c in results:
            print(f"{c['id']} - {c['name']}")
