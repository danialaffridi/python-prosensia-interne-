def add_expense(expenses):
    amount = float(input("Enter the amount: "))
    if amount <= 0:
        print("Amount must be positive.")
        return
    
    category = input("Enter the category (e.g., food, transportation, entertainment): ").lower()
    description = input("Enter a description for the expense: ")
    
    expense = {'amount': amount, 'category': category, 'description': description}
    expenses.append(expense)

def display_summary(expenses):
    summary = {}
    
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    
    for category, total in summary.items():
        print(f"Total spent on {category}: ${total:.2f}")

def main():
    expenses = []
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add a new expense")
        print("2. View summary of expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
   