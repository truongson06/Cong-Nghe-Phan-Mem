from modules.report import ReportManager
from modules.db import save_db
class AdminManager:
    def __init__(self, db):
        self.db = db
        self.report_manager = ReportManager(db)

    def admin_menu(self, product_manager, user_manager, order_manager,category_manager):
        while True:
            print("\n--- ADMIN MENU ---")
            print("1. View users")
            print("2. Add product")
            print("3. Update product")
            print("4. View orders")
            print("5. Generate report")
            print("6. View reports")
            print("7. Export report")
            print("8. Add category")
            print("9. View categories")
            print("10. Search categories")
            print("0. Exit")

            c = input("Choose: ")

            if c == "1":
                for u in self.db["users"]:
                    print(u)
            elif c == "2":
                product_manager.add_product()
                save_db(self.db)
            elif c == "3":
                product_manager.update_product()
                save_db(self.db)
            elif c == "4":
                for o in self.db["orders"]:
                    print(o)
            elif c == "5":
                self.report_manager.generate_report()
                save_db(self.db)
            elif c == "6":
                self.report_manager.view_reports()
            elif c == "7":
                rid = int(input("Report ID: "))
                self.report_manager.export_report(rid)
            elif c == "8":
                category_manager.add_category()
                save_db(self.db)
            elif c == "9":
                category_manager.view_categories()
            elif c == "10":
                category_manager.search_category()
            elif c == "0":
                break
