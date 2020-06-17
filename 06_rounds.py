import random

keep_going = ""
while keep_going == "":
    high = int(input("high?"))
    rounds = int(input("How many rounds?  "))  # check with integer checker in due course
    rounds_played = 0

    while rounds_played < rounds:
        print("Round {}".format(rounds_played + 1))
        print()

        one = random.randint(1, high)
        two = random.randint(1, high)
        answer = one + two
        print(one)
        print(two)
        print(answer)
        user_answer = int(input("{} + {} = ".format(one,two)))
        if user_answer == answer:
            print("WOW! you got it right")
            rounds_played += 1
        else:
            print("WRONG!")
            rounds_played += 1
    keep_going = input("Press <enter> to play again or any key to quit: ")


print("You have gotten  to the end of the game")