def quiz_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))

import random
question_list = []
user_answer_list = []
answer_list = []
# sets up loop

keep_going = ""
while keep_going == "":

    # asks for the needed integers
    high = int(input("high?"))
    rounds = int(input("How many rounds?  "))
    rounds_played = 0
    won = 0
    loss = 0

    # stops game after user plays the amount of rounds they selected
    while rounds_played < rounds:
        round = quiz_statement("###  Round {} of {}  ###".format(rounds_played+1,rounds), "#")
        print()

        # generates random numbers
        one = random.randint(1, high)
        two = random.randint(1, high)
        # maths
        answer = one + two
        user_answer = int(input("{} + {} = ".format(one,two)))

        answer_list.append(answer)
        question_list.append("{} + {} = ".format(one,two))
        user_answer_list.append(user_answer)

        # compares users guess to answer
        if user_answer == answer:
            right = quiz_statement("(☞ﾟヮﾟ)☞ WOW! You got it right ☜(ﾟヮﾟ☜)   ", "*")
            print()
            rounds_played += 1
            won += 1
        else:
            lose = quiz_statement("(╯°□°）╯︵ ┻━┻ WRONG! the right answer was {} (╯°□°）╯︵ ┻━┻  ".format(answer), "-")
            print()
            rounds_played += 1
            loss += 1

            # prints users score after each question
        print("Right: {} \t | \t Wrong: {}".format(won, loss))
    listcount = 0
    print()
    print("***Results***")
    print()
    print("                   user answer        right answer")
    for item in question_list:
        print("question: ",item," ", user_answer_list[listcount],"                 ", answer_list[listcount])
        listcount += 1
    print()

    # loops game
    keep_going = input("Press <enter> to play again or any key to quit: ")
