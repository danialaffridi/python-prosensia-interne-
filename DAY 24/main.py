def add_product(inventory, name, price, quantity):
    for product in inventory:
        if product['name'].lower() == name.lower():
            print(f"Product '{name}' already exists in inventory.")
            return
    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    print(f"Product '{name}' added to inventory.")

def update_quantity(inventory, name, quantity):
    for product in inventory:
        if product['name'].lower() == name.lower():
            product['quantity'] += quantity
            print(f"Quantity for '{name}' updated to {product['quantity']}.")
            return
    print(f"Product '{name}' not found in inventory.")

def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for product in inventory:
        print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
    print()

def main():
    inventory = []
    
    while True:
        print("Inventory Management System")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. View Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(inventory, name, price, quantity)
        
        elif choice == '2':
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity to add: "))
            update_quantity(inventory, name, quantity)
        
        elif choice == '3':
            display_inventory(inventory)
        
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
