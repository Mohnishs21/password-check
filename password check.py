import re

def check_password_strength(password):
    # Check password length
    if len(password) < 12:
        print("Password must be at least 12 characters long.")
        return False

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False

    # Check for at least one number
    if not re.search(r"[0-9]", password):
        print("Password must contain at least one number.")
        return False

    # Check for at least one special character
    if not re.search(r"[^a-zA-Z0-9]", password):
        print("Password must contain at least one special character.")
        return False

    # Password meets all criteria
    print("Password strength: Strong")
    return True

# Get password input from user
password = input("Enter your password: ")

# Check password strength
check_password_strength(password)
