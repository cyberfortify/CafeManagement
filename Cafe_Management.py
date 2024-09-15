# Function to display the menu
def display_menu():
    print("\n__________________________")
    print("Here is the Menu: ")
    print("--------------------------")
    for item, price in menu.items():
        print(f'{item}: Rs{price}')
    print("__________________________")

# Function to take an order
def give_order():
    order_1 = input("Aap kya order karna chahte ho? : ")
    if order_1 in menu:
        quantity = int(input(f"How many {order_1}s would you like to order? "))
        orders[order_1] = orders.get(order_1, 0) + quantity
        
        another_order = input("Kya aap kuch aur order karna chahte ho? (Yes/No):  ").lower()
        if another_order == "yes":
            order_2 = input("Aap aur kya lena pasand karoge?: ")
            if order_2 in menu:
                quantity = int(input(f"How many {order_2}s would you like to order? "))
                orders[order_2] = orders.get(order_2, 0) + quantity
                print(f"Successfully ordered {quantity} {order_2}(s).")
        else:
            print("Thank You")       
                           
    else:
        print("Sorry, this item is not available.")

# Function to calculate the bill
def calculate_bill():
    if not orders:
        print("You haven't ordered anything yet!")
    else:
        print("\n__________________________")
        print("Your Order Summary: ")
        print("--------------------------")
        total_bill = 0
        for item, quantity in orders.items():
            price = menu[item] * quantity
            total_bill += price
            print(f"{item} (x{quantity}): \tRs {price}")
        print("--------------------------")
        print(f"Total Bill: \tRs {total_bill}")
        print("__________________________\n")

# Order Menu
menu = {
    'Cappuccino': 165,
    'Velvet Coffee': 420,
    'Cold Coffee': 250,
    'Chocolate Shake': 420,
    'Sandwich': 165,
    'Bread Sticks': 150,
    'Veg Burger': 330,
    'Veg Pizza': 160,
    'Cheesecake': 160,
    'Brownie': 450,
    'Choco Fudge': 160,
    'Vanilla Scoop': 350,
    'Strawberry Cake': 340,
    'Berry Cheesecake': 180,
}

# To store the orders
orders = {}

# Greeting user
print("Welcome to Aadi's Restaurant :) ")

while True:
    print("\n1. View Menu \n2. Order Item \n3. View Order Bill \n4. Exit")
    
    try:
        # User choice
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            display_menu()
        elif choice == 2:
            give_order()
        elif choice == 3:
            calculate_bill()
        elif choice == 4:
            print("Thank you for visiting Aadi's Restaurant! Have a nice day!")
            break 
        else:
            print("Invalid choice! Please select a valid option.")
    
    except ValueError:
        print("Please enter a valid number!")
