from write_menu_list import write_menu_list

# file for menu inputs
def valid_login(credentials, users):
    (username, password) = credentials
    try:
        (stored_password, inventory) = users[username]
    except:
        return False
    return password == stored_password

