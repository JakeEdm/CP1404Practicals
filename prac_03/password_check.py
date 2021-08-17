"""Jake Edmunds - CP1404 - Password Checker"""


# imports
# CONSTANTS

def main():
    """Creates a password"""
    password = get_valid_password()
    for char in password:
        print("*", end="")


def get_valid_password():
    """Gets a valid password"""
    password_requirements = "**********"
    password = input("Enter new password: ")
    while len(password) < len(password_requirements):
        print("Invalid password length")
        password = input("Enter new password: ")
    return password


main()
