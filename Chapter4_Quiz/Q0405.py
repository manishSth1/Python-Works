# Determine the grade

score = float(input("Enter your score in percentage (%): "))               # asks user to input their score in percentage

if score >= 90:
    print("Your grade is A. Excellent work, Congratulations topper!!")     # checks if the score is 90% and above 90%
else:
    if score >= 80 and score < 90:                                         # checks if the score is 80% to 90% 
        print("Your grade is B. Amazing, Your hard work paid off.")
    else:
        if score >= 70 and score < 80:                                     # checks if the score is 70% to 80%
            print("Your grade is C. Good Job, Keep doing better.")
        else:
            if score >= 60 and score < 70:                                 # checks if the score is 60% to 70%
                print("Your grade is D. Your result is satisfactory.")
            else:
                print("Your grade is F. Sorry, you failed the exam. Work hard next time!!")   # checks if the score is below 60%

