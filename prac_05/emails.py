"""E-mails"""


# imports
# CONSTANTS

def main():
    """Stores user emails and names in a dictionary"""
    user_details = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        if not is_name_correct(name):
            name = input("Name: ")
        user_details[email] = name
        email = input("Email: ")

    for key, value in user_details.items():
        print(f'{value} ({key})')


def get_name_from_email(email):
    """Extracts potential name from email"""
    prefix = email.split("@")[0]
    phrases = prefix.split(".")
    name = " ".join(phrases).title()
    return name


def is_name_correct(name):
    """Checks if extracted name is correct"""
    choice = input("Is your name {} (Y/N)?".format(name)).upper()
    if choice == "Y" or choice == "":
        return True


main()
