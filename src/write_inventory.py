# file for writing inventory
def write_inventory(inventory):
    if len(inventory) > 0:
        print("These are your items")
        print()
        for index in range(len(inventory)):
            print(f"{index + 1} {inventory[index]}")
    else:
        print("You have no items!")
        
