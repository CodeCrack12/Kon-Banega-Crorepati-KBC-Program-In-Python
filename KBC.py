import random

questions = ["question1", "question2", "question3", "question4", "question5"]
select = random.choice(questions)
print("Round 1")
total_amount = 25000

def rounds():
    
    global total_amount
    if select == "question1":
        answer1 = int(input("\nWhich planet has 1/3 diamond?  \n1. Kepler-62 e\n2. Gliese 581 d\n3. 55"
                            " Cancri e\n4. Tau Ceti e*\nYour Answer: "))
        if answer1 == 3:
            print("You Earned 5000$ You Have: ", total_amount + 5000, "$")
            total_amount += 5000
        else:
            print("You lose 5000$ You Have :", total_amount - 5000, "$")
            total_amount -= 5000

    elif select == "question2":
        answer2 = int(input("\nHow old is the universe?  \n1. 10 Billion Years\n2. 14 "
                            "Billion Years\n3. 13 Billion Years\n4. 6 Billion Years\nYour Answer: "))
        if answer2 == 3:
            print("You Earned 5000$ You Have: ", total_amount + 5000, "$")
            total_amount += 5000
        else:
            print("You lose 5000$ You Have :", total_amount - 5000, "$")
            total_amount -= 5000

    elif select == "question3":
        answer3 = int(input("\nWhich of the following is mars' rover/rovers? \n1. Spirit\n2. Curiosity\n3. "
                            "Opportunity\n4. All\nYour Answer: "))
        if answer3 == 4:
            print("You Earned 5000$ You Have: ", total_amount + 5000, "$")
            total_amount += 5000
        else:
            print("You lose 5000$ You Have :", total_amount - 5000, "$")
            total_amount -= 5000

    elif select == "question4":
        answer4 = int(input("\nWhat percentage of C02 is present on mars?\n1. 2%\n2. 50% \n3. 95%\n4. Not Present\n"
                            "Your Answer: "))
        if answer4 == 3:
            print("You Earned 5000$ You Have: ", total_amount + 5000, "$")
            total_amount += 5000
        else:
            print("You lose 5000$ You Have :", total_amount - 5000, "$")
            total_amount -= 5000

    elif select == "question5":
        answer5 = int(
            input("\nWhich person in apollo 11 did not step on the moon?\n1. Neil Armstrong\n2. Micheal Collins"
                  "\n3. Buzz Aldrin\n4. All stepped\nYour Answer: "))
        if answer5 == 2:
            print("You Earned 5000$ You Have: ", total_amount + 5000, "$")
            total_amount += 5000
        else:
            print("You lose 5000$ You Have :", total_amount - 5000, "$")
            total_amount -= 5000


rounds()
questions.remove(select)
ques2 = questions.copy()
select = random.choice(ques2)
print("Round 2: ")
rounds()
ques2.remove(select)
ques3 = ques2.copy()
select = random.choice(ques3)
print("Round 3: ")
rounds()
ques3.remove(select)
ques4 = ques3.copy()
select = random.choice(ques4)
print("Round 4: ")
rounds()
ques4.remove(select)
ques5 = ques4.copy()
select = random.choice(ques5)
print("Round 5: ")
rounds()
