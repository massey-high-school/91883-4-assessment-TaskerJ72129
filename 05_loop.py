import random

keep_going = ""
while keep_going == "":

    high = int(input("high?"))
    one = random.randint(1, high)
    two = random.randint(1, high)
    answer = one + two
    print(one)
    print(two)
    print(answer)
    ("{} + {} = ".format(one,two))
    user_answer = int(input("{} + {} = ".format(one,two)))
    if user_answer == answer:
        print("WOW! you got it right")
    else:
        print("WRONG!")

    keep_going = input("Press <enter> to play again or any key to quit: ")
