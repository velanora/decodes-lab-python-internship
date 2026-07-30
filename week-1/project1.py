"""
This is an interactive command-line Python program designed to manage daily to-do tasks.It allows 
users to personalize their list by name, append new tasks, view all current entries, and 
exit safely through a looping menu interface.
"""
#initalize list and loop variable
tasks = [] #List of tasks for user
iterate = 'y' 

# Get user name
name = str(input("Enter your name : ")) 
print(f"\n********* Welcome to {name}'s To do list **********\n")

# function to append the entered task into the list of TO DO tasks
def append_task():
    print("\n=============== To append a task ===============\n")
    entered_task = str(input("Enter your task : "))
    tasks.append(entered_task)
    print("Current TO DO list : ",tasks,"\n")

# function to display the list of TO DO tasks
def display():
    print("\n=============== To view all the tasks ===========\n")
    print(f"============== {name}'s TO DO list ==============")
    for i in range(0,len(tasks)):
       print("    *",{tasks[i]}) 

    # function for exiting the program
def exit():
    print("\n==================  To Exit =====================\n")
    print("Exiting......\n")
    iterate = 'n'

# function for Invalid input
def invalid():
    print("Invalid input!!")
    print("Enter the correct number again!!") 

while iterate == 'y':
    # Menu of options
    print("┌─────────────────────────────────────────┐")
    print("│         CHOOSE AN OPTION                │")
    print("├─────────────────────────────────────────┤")
    print("│  [1] Append a task                      │")
    print("│  [2] View all tasks                     │")
    print("│  [3] Exit program                       │")
    print("└─────────────────────────────────────────┘\n")
    option = int(input("Enter option number : "))

    if(option == 1):
        append_task()
    elif(option == 2):
        display()
    elif(option == 3):
        exit()  
    else:
        invalid()

    print("\n=====================================================\n")

        
    
