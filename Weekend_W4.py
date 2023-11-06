class User():
    def __init__(self, username):
        self.username = username
        self.properties = {}

    def add_properties(self, property_name, property):
        self.properties[property_name] = property

class Property:
    def __init__(self, name):
        self.name = name
        self.expenses = {}
        self.incomes = {}
        self.investments = {}

    def add_expense(self, expense_name, amount):
        self.expenses[expense_name] = amount
    
    def add_income(self, income_name, amount):
        self.incomes[income_name] = amount 

    def total_investment(self, investment_name, amount):
        self.investments[investment_name] = amount

    def calculate_roi(self):
        total_expenses = sum(self.expenses.values())
        total_income = sum(self.incomes.values())
        total_investments = sum(self.investments.values())
        roi = (total_income - total_expenses) / total_investments
        return roi

def driver():
    user_names = {}
    current_user = None

    while True:
        what_do = input("\nWELCOME TO MY CALCULATOR \n What would you like to do ?\n Add User\n Change User\n Add Property \n Add Income to Property\n Add Expense to Property\n Add Investment to Property\n Calculate ROI\n Quit \n  \n").lower()

        if what_do == "add user":
            name_user = input("Please enter a username: ")
            user_names[name_user] = User(name_user)
            current_user = name_user
            print(f"{name_user} has been created")

        elif what_do == "change user":
            change_user = input("What user do you want to change to ? ")
            if change_user in user_names:
                current_user = change_user
                print(f"Changed user to: {change_user}")
            else:
                print("User with that name does not exists, please try again! ")

        elif what_do == "add property":
            if current_user:
                property_name = input("Please enter the name of your property: ")
                user = user_names.get(current_user)
                if user:
                    property = Property(property_name)
                    user.add_properties(property_name, property)
                    print(f"Property {property_name} added to {current_user}.")

            else:
                print("Please make sure to creat an user first. ")


        elif what_do == "add income to property" or what_do == "add income":
            if current_user:
                property_name = input("Enter your property name: ")
                income_name = input("Please enter the name of the income: ")
                income_amount = float(input("What is the amount of this income ? "))
                user = user_names.get(current_user)
                if user:
                    property = user.properties.get(property_name)
                    if property:
                        property.add_income(income_name, income_amount)
                        print(f"Income {income_name} added to {property_name}.")
                    else:
                        print(f"Property {property_name} not in your account. ")
            else:
                print("Please make sure to creat an user first. ")

        
        elif what_do == "add expense to property" or what_do == "add expense":
            if current_user:
                property_name = input("Enter your property name: ")
                expense_name = input("Please enter the name of the expense: ")
                expense_amount = float(input("What is the amount of this expense ? "))
                user = user_names.get(current_user)
                if user:
                    property = user.properties.get(property_name)
                    if property:
                        property.add_expense(expense_name, expense_amount)
                        print(f"Expense {expense_name} added to {property_name}. ")
                    else:
                        print(f"Property {property_name} not in your account. ")
            else:
                print("Please make sure to creat an user first. ")

        
        elif what_do == "add investment to property" or what_do == "add investment":
            if current_user:
                property_name = input("Enter your property name: ")
                investment_name = input("Please enter the name of the investment: ")
                investment_amount = float(input("What is the amount of this investment ? "))
                user = user_names.get(current_user)
                if user:
                    property = user.properties.get(property_name)
                    if property:
                        property.total_investment(investment_name, investment_amount)
                        print(f"Income {investment_name} added to {property_name}.")
                    else:
                        print(f"Property {property_name} not in your account. ")
            else:
                print("Please make sure to creat an user first. ")
        

        elif what_do == "calculate roi" or what_do == "calculate":
            if current_user:
                property_name = input("Enter property name: ")
                user = user_names.get(current_user)
                if user:
                    property = user.properties.get(property_name)
                    if property:
                        roi = property.calculate_roi()
                        print(f"ROI for {property_name} is: {roi * 100}%")
                    else:
                        print(f"Property {property_name} not found. ")
            else:
                print("Please make sure to creat an user first. ")
            

        elif what_do == "quit" or "bye":
            print("Thanks for using this calculator we wish the best on your investments! ")
            break

driver()





              
        

        