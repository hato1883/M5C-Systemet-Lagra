from write_menu_list import write_menu_list

# file for menu inputs
def menu_input(choices):
    write_menu_list(choices)
    while True:
        print()
        user_choice = input("Option: ").lower()
        for choice in choices:
            (option, desc) = choice
            if user_choice == option:
                return user_choice
            pass
        print("Invalid option!")
    return None

if __name__ == "__main__":
    opt = menu_input([('l', "Är du en vinnare?")])
    print(opt)
