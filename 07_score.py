import random
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
        print("Round {}".format(rounds_played + 1))
        print()

        # generates random numbers
        one = random.randint(1, high)
        two = random.randint(1, high)
        # maths
        answer = one + two
        print(one)
        print(two)
        print(answer)
        user_answer = int(input("{} + {} = ".format(one,two)))

        # compares users guess to answer
        if user_answer == answer:
            print("WOW! you got it right")
            rounds_played += 1
            won += 1
        else:
            print("WRONG!")
            rounds_played += 1
            loss += 1

            # prints users score after each question
        print("Right: {} \t | \t Wrong: {}".format(won, loss))

    # loops game
    keep_going = input("Press <enter> to play again or any key to quit: ")


print("You have gotten  to the end of the game")