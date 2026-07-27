tasks = []
iterate = 'y'
name = str(input("Enter your name : "))
print(f"\n********* Welcome to {name}'s To do list **********\n")
while iterate == 'y':
    print("┌─────────────────────────────────────────┐")
    print("│         CHOOSE AN OPTION                │")
    print("├─────────────────────────────────────────┤")
    print("│  [1] Append a task                      │")
    print("│  [2] View all tasks                     │")
    print("│  [3] Exit program                       │")
    print("└─────────────────────────────────────────┘\n")
    option = int(input("Enter option number : "))

    if(option == 1):
        print("\n=============== To append a task ===============\n")
        app_task = str(input("Enter your task : "))
        tasks.append(app_task)
        print("Current TO DO list : ",tasks,"\n")
        print("==================================================\n")
    elif(option == 2):
        print("\n=============== To view all the tasks ===========\n")

        print(f"============== {name}'s TO DO list ==============")
        for i in range(0,len(tasks)):
            print("    *",{tasks[i]})
        print("===================================================\n")   
    elif(option == 3):
        print("\n==================  To Exit =====================\n")
        print("Exiting......\n")
        iterate = 'n'
        print("===================================================\n")  
    else:
        print("Invalid input !! \nTry again!!\n")

