# imports the randomness
import random

# statement generator function
def quiz_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))

# checks that input is above 0 and is an integer
def intcheck(question,low):
    while True:
        try:
            response = int(input(question))
            if response < low:
                print("Please enter a whole number above 0")
                continue
            return response
        except ValueError:
            print("Please enter a whole number above 0")

# loops game
keep_going = ""
while keep_going == "":
    print()
    print("welcome to quiz quest\n"
          "\n"
          "this is an addition game\n"
          "you can choose how hard you make it with what number you choose for high\n"
          "you can also choose how many rounds you want to play\n"
          "have fun")
    print()
    # starts all the lists that are used later
    question_list = []
    user_answer_list = []
    answer_list = []
    righ_wrong_list = []
    right_list = []
    wrong_list = []

    # asks for the needed integers
    print()
    high = intcheck("high?", 1)

    rounds = intcheck("How many rounds?  ", 1)
    rounds_played = 0
    won = 0
    loss = 0

    # stops game after user plays the amount of rounds they selected
    while rounds_played < rounds:
        round = quiz_statement("###  Round {} of {}  ###".format(rounds_played + 1, rounds), "#")
        print()

        # generates random numbers
        one = random.randint(1, high)
        two = random.randint(1, high)
        # maths
        answer = one + two
        user_answer = intcheck("{} + {} = ".format(one, two), 1)

        answer_list.append(answer)
        question_list.append("{} + {} = ".format(one, two))
        user_answer_list.append(user_answer)

        # compares users guess to answer
        if user_answer == answer:
            right = quiz_statement("(☞ﾟヮﾟ)☞ WOW! You got it right ☜(ﾟヮﾟ☜)   ", "*")
            print()
            rounds_played += 1
            won += 1
            righ_wrong_list.append("right")
            right_list.append("1")
        else:
            lose = quiz_statement("(╯°□°）╯︵ ┻━┻ WRONG! the right answer was {} (╯°□°）╯︵ ┻━┻  ".format(answer), "-")
            print()
            rounds_played += 1
            loss += 1
            righ_wrong_list.append("wrong")
            wrong_list.append("1")
            # prints users score after each question
        print("Right: {} \t | \t Wrong: {}".format(won, loss))
        sum_roundcount = 0
    print()
    print("***Results***")
    print()

    for item in question_list:
        print("question: ", item, "  user answer:", user_answer_list[sum_roundcount], "            right answer:",
              answer_list[sum_roundcount], "            Right/Wrong:", righ_wrong_list[sum_roundcount])
        sum_roundcount += 1
    print()
    percent_right = ((len(right_list)) / ((len(right_list)) + (len(wrong_list)))) * 100
    print("you got {:.2f}% right".format(percent_right))
    # loops game

    keep_going = input("Press <enter> to play again or any key to quit: ")
