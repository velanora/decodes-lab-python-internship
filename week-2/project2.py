option = 1
total_expense = 0

def add_expense():
    global total_expense
    print("================== Add new expense ================\n ")
    while True:
        try:
            new_expense = int(input("Enter the expense amount : "))
            total_expense += new_expense
            break
        except ValueError:
            print("Invalid input!! please enter a number")

def display():
    print("==================== Display =======================\n")
    print("Total expense : ",total_expense)

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
