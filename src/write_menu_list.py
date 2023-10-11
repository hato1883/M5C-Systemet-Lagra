# file for menu inputs
def write_menu_list(choices):
    print("Select an action")
    print()
    for choice in choices:
        (option, desc) = choice
        print(f"  {option}) {desc}")
    return None
        
