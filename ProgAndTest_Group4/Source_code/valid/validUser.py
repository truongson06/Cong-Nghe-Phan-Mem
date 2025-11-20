import re
class ValidUser:
    def Valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format.")
    def has_email(self, email, db):
        for user in db["users"]:
            if user["email"] == email:
                raise ValueError("Email already in use.")
            