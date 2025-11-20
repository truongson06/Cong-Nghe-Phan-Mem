import json
def save_db(db):
    with open("database.json", "w") as f:
        json.dump(db, f, indent=4)