"""
ENTERPRISE RANDOM PASSWORD GENERATOR
"""
import secrets # secret password choice i.e secrets.choice()
import string # for string manulipation i.e .join(lists)
""" 
secret.choice()
We won't use random.choice() beacuse it relies on Mersenne Twister (deterministic random password generator)
it is often seeded by predictable system time, an attacker who knows the seed can perfectly calculate and 
predict the generated password 

"""
username = None 
password = None

def create_account(): #1st function
    print("\n============ Create new account ==================\n")
    global username # tells interpreter : don't create a local variable
    username = str(input("Enter username : "))
    while True:
        try:
            length = int(input("Enter the length of password : "))
        except ValueError:
            print("Invalid input!! Enter a number")
            continue

        if(length<8 or length>=60):
            print("Enter length more than equal to 8 and less than equal to 60")    
            continue
        break

    password_generator(length)
     
def password_generator(lenPass):
    global password
    sums = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = "".join(secrets.choice(sums) for i in range(lenPass) )
        print("Password : ",password)
        choice = input("Keep this password (y/n)").lower()
        if(choice == 'y'):
            break

    while True:
        confirm_password =  str(input("Confirm password : "))
        if (password == confirm_password) :
            print("Password Matched!! \nAccount created successfully!!")
            break
        else:
            print("Doesn't matched! \nTry again!!")
    
def display_userDetails(): # 2nd function
    print("\n=========== Account Details =====================\n")
    print("Username : ",username)
    print("Password : ",password)

def exit_program():#3rd function
    print("\n==================  To Exit =====================\n")
    print("Exiting......\n") 

def invalid():
    print("\n====================== invalid ======================\n")
    print("Invalid input!!")
    print("Enter the correct number again!!")  


while True:
    print("┌─────────────────────────────────────────┐")
    print("│         CHOOSE AN OPTION                │")
    print("├─────────────────────────────────────────┤")
    print("│  [1] Create Account                     │")
    print("│  [2] Display your account details        │")
    print("│  [3] Exit program                       │")
    print("└─────────────────────────────────────────┘\n")
    
    while True:
        try:
            option = int(input("Enter option number : "))
            break
        except ValueError:
            print("Invalid input!! please enter a number")
          
    if (option == 1):
        create_account()
    elif (option == 2):
        display_userDetails()
    elif (option == 3):
        exit_program()
        break
    else:
        invalid()
        
    print("\n===================================================\n")
    
