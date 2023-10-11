from menu_input import menu_input
from enter_credentials import enter_credentials
from valid_login import valid_login
from welcome_user import welcome_user
from retrive_inventory import retrive_inventory
from write_inventory import write_inventory
from add_to_inventory import add_to_inventory


def build_users():
    users = {}
    users["jackie"] = ("chan", ["nunchucks", "black belt"])
    users["clint"] = ("eastwood", ["revolver", "kompass"])
    return users


# init users
users = build_users()

# Main loop
while True:
    print("Welcome to Lagra™")
    print()

    # Print main menu and get choice
    main_menu_choice = menu_input( [ ('l', "Log in"), ('q', "Quit") ] )
    print()
    
    # Check option
    match main_menu_choice:

        case 'l': # Log in

            # Get credentials
            credentials = enter_credentials()
            print()

            # Check if login fails
            if not valid_login(credentials, users):
                print("Invalid username or password")
                print()
                continue # Failed repeat main men choices

            # Login suceeded
            (username, password) = credentials

            # Welcome user
            welcome_user(username)
            print()

            # Get inventory and print it
            inventory = retrive_inventory(username, users)
            write_inventory(inventory)
            print()

            # Session Menu   
            while True:
                # Print session menu and get choice
                session_choice = menu_input( [ ('a', "Add item"), ('l', "List items"), ('q', "Log out") ] )
                print()

                # Evaluate choice
                match session_choice:

                    case 'a': # Add item
                        item = input("Add item: ")
                        print()
                        add_to_inventory(item, inventory)

                        write_inventory(inventory)
                        print()
                        pass

                    case 'l': # List items
                        write_inventory(inventory)
                        print()

                    case 'q': # Log out
                        print(f"Goodbye {username}, your items: {inventory}")
                        print()
                        break # break Session menu (will then restart main menu)
                pass
            pass
        
        case 'q': # Quit
            break
    pass
pass
