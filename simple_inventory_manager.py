"""Simple inventory manager."""
import collections

def update_inventory(item, quantity):
    """Update the inventory with the given item and quantity."""
    global INVENTORY
    if item in INVENTORY:
        INVENTORY[item] += quantity
    else:
        INVENTORY[item] = quantity

INVENTORY = collections.defaultdict(int)

if __name__ == "__main__":
    while True:
        print("1. Add item\n2. Remove item\n3. Check inventory")
        choice = input("Choose an option: ")
        if choice == '1':
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            update_inventory(item, quantity)
        elif choice == '2':
            item = input("Enter the item name: ")
            if item in INVENTORY:
                del INVENTORY[item]
                print(f"Item '{item}' removed.")
            else:
                print(f"Item '{item}' not found.")
        elif choice == '3':
            for item, quantity in INVENTORY.items():
                print(f"{item}: {quantity}")
        else:
            print("Invalid option. Please try again.")
