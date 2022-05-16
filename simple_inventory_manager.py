"""Simple Inventory Manager."""

def add_item(item_name, quantity):
    """Add an item to the inventory."""
    global items
    if item_name not in items:
        items[item_name] = 0
    items[item_name] += quantity

def print_inventory():
    """Print the current inventory."""
    for item, quantity in items.items():
        print(f"{item}: {quantity}")

items = {}
if __name__ == "__main__":
    while True:
        print("1. Add item\n2. Print inventory\n3. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item_name, quantity)
        elif choice == "2":
            print_inventory()
        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")
