option = 1
total_expense = 0 #global variable

expenses = [] # list of tuples

def add_expense():
    global total_expense
    print("================== Add new expense ================\n ")
    while True:
        try:
            category = str(input("Enter the category of expense : "))
            amount = int(input("Enter the expense amount : "))
            expenses.append((category, amount)) # ---> new tuple added to list
            total_expense += amount
            break
        except ValueError:
            print("Invalid input!! please enter a number")

def display():
    print("==================== Display =======================\n")
    if not expenses:
        print("No expenses yet.")
        return
    for category, amount in expenses :
        print(f"  *  {category} :{amount}")
    print("\nTotal expense : ",total_expense)

def exit_program():
    print("\n==================  To Exit =====================\n")
    print("Exiting......\n") 


def invalid():
    print("====================== invalid ======================\n")
    print("Invalid input!!")
    print("Enter the correct number again!!")  

while True:
    print("┌─────────────────────────────────────────┐")
    print("│         CHOOSE AN OPTION                │")
    print("├─────────────────────────────────────────┤")
    print("│  [1] Add expense amount                 │")
    print("│  [2] Display total spents               │")
    print("│  [3] Exit program                       │")
    print("└─────────────────────────────────────────┘\n")

    while True:
        try:
            option = int(input("Enter option number : "))
            break
        except ValueError:
            print("Invalid input!! please enter a number")
      
    if (option == 1):
        add_expense()
    elif (option == 2):
        display()
    elif (option == 3):
        exit_program()
        break
    else:
        invalid()
    
    print("===================================================\n")
