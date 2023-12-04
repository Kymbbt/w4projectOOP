class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Income:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Property:
    def __init__(self, address):
        self.address = address
        self.expenses = []
        self.incomes = []
        self.roi = 0  

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_income(self, income):
        self.incomes.append(income)

    def calculate_roi(self):
        total_income = sum(income.amount for income in self.incomes)
        total_expense = sum(expense.amount for expense in self.expenses)
        self.roi = (total_income - total_expense) / total_expense * 100


class User:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)


def main():
    users = []

    while True:
        print("\n1. Add User\n2. Add Property\n3. Add Expense\n4. Add Income\n5. Calculate ROI\n6. Exit")
        choice = input("Pick a number : ")

        if choice == '1':
            name = input("Enter your name: ")
            user = User(name)
            users.append(user)
            print(f"User '{name}' added.")

        elif choice == '2':
            user_name = input("Enter your name: ")
            user = next((u for u in users if u.name == user_name), None)
            if user:
                address = input("Enter property address: ")
                property = Property(address)
                user.add_property(property)
                print(f"Property at '{address}' added for user '{user_name}'.")
            else:
                print(f"User '{user_name}' not found.")
                
        elif choice == '3':
            
            pass

        elif choice == '4':
           
            pass

        elif choice == '5':
        
            pass

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
