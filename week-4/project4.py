print("====================================================================")
print("              Welcome to General Knowledge Quiz")
print("====================================================================\n")
finalScore = 0
# Q1's section
print("--------------- Question 1 ------------------ ")
answer1 = str(input("What has hands but can't clap? \nAnswer : "))
correct_answer1 = "clock"
answer1 = answer1.strip().lower()
if answer1 == correct_answer1 :
    print("Correct Answer!!")
    finalScore += 1
else :
    print("Wrong Answer!!")

# Q2's section
print("--------------- Question 2 ------------------ ")
answer2 = str(input("Which is the largest ocean in the world?  \nAnswer : "))
answer2 = answer2.strip().lower()
correct_answers2 = ["pacific ocean", "pacific"] # tuple for acceptable answers2
if answer2 in correct_answers2 :
    print("Correct Answer!!")
    finalScore += 1
else :
    print("Wrong Answer!!")

# Q3's section
print("--------------- Question 3 ------------------ ")
answer3 = str(input("First person to walk on the moon? \nAnswer : "))
answer3 = answer3.strip().lower()
correct_answers3 = ["neil armstrong","armstrong"] # tuple for acceptable answers3
if answer3 in correct_answers3 :
    print("Correct Answer!!")
    finalScore += 1
else :
    print("Wrong Answer!!")

print("====================================================================")
print(f"                   \nFinal score : {finalScore}/3")
print("                       Quiz Ended!!")
print("====================================================================\n")
