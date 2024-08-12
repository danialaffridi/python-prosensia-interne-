def add_product(inventory):
    product_name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    
    product = {
        "name": product_name,
        "id": product_id,
        "quantity": quantity,
        "price": price
    }
    
    inventory.append(product)
    print("Product added successfully!")

def view_inventory(inventory):
    if not inventory:
        print("No products available in inventory.")
        return
    
    print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Price':<10}")
    for product in inventory:
        print(f"{product['id']:<10} {product['name']:<20} {product['quantity']:<10} {product['price']:<10.2f}")

def update_product_quantity(inventory):
    product_id = input("Enter the product ID to update: ")
    for product in inventory:
        if product['id'] == product_id:
            new_quantity = int(input("Enter the new quantity: "))
            product['quantity'] = new_quantity
            print("Product quantity updated successfully!")
            return
    
    print("Product ID not found.")

def remove_product(inventory):
    product_id = input("Enter the product ID to remove: ")
    for product in inventory:
        if product['id'] == product_id:
            inventory.remove(product)
            print("Product removed successfully!")
            return
    
    print("Product ID not found.")

def main():
    inventory = []
    
    while True:
        print("\nInventory Management System")
        print("1. Add a New Product")
        print("2. View Inventory")
        print("3. Update Product Quantity")
        print("4. Remove a Product")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            update_product_quantity(inventory)
        elif choice == '4':
            remove_product(inventory)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
