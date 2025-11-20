from modules.db import save_db

class ReportManager:
    def __init__(self, db):
        self.db = db
        if "reports" not in db:
            db["reports"] = []

    def generate_report(self):
        total_orders = len(self.db["orders"])
        total_revenue = sum(order["total"] for order in self.db["orders"])

        low_stock = [
            p for p in self.db["products"]
            if p["stock"] < 5
        ]

        report = {
            "report_id": len(self.db["reports"]) + 1,
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "low_stock_products": [p["id"] for p in low_stock]
        }

        self.db["reports"].append(report)
        print("\n--- REPORT GENERATED ---")
        print(report)
        save_db(self.db)
        
    def view_reports(self):
        print("\n=== ALL REPORTS ===")
        for r in self.db["reports"]:
            print(r)

    def export_report(self, report_id):
        for r in self.db["reports"]:
            if r["report_id"] == report_id:
                with open(f"report_{report_id}.txt", "w") as f:
                    f.write(str(r))
                print(f"Report exported to report_{report_id}.txt")
                return
        print("Report not found")
