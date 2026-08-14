finalscore = 0

print("====================================================================")
print("              Welcome to General Knowledge Quiz")
print("====================================================================\n")

# Q1's section
print("--------------- Question 1 ------------------ ")
answer1 = str(input("What has hands but can't clap? \nAnswer : "))
correct_answer1 = "clock"
answer1 = answer1.strip().lower()
if answer1 == correct_answer1 :
    print("Correct Answer!!")
    finalscore += 1
else :
    print("Wrong Answer!!")

# Q2's section
print("--------------- Question 2 ------------------ ")
answer2 = str(input("Which is the largest ocean in the world?  \nAnswer : "))
answer2 = answer2.strip().lower()
correct_answer2 = "pacific ocean"
if answer2 == correct_answer2 :
    print("Correct Answer!!")
    finalscore += 1
else :
    print("Wrong Answer!!")

# Q3's section
print("--------------- Question 3 ------------------ ")
answer3 = str(input("First person to walk on the moon? \nAnswer : "))
answer3 = answer3.strip().lower()
correct_answer3 = "armstrong"
if answer3 == correct_answer3 :
    print("Correct Answer!!")
    finalscore += 1
else :
    print("Wrong Answer!!")

print("====================================================================")
print(f"                   \nFinal score : {finalscore}/3")
print("                       Quiz Ended!!")
print("====================================================================\n")
