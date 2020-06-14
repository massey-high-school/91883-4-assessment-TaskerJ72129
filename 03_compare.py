import random

high = int(input("high?"))
one = random.randint(0, high)
two = random.randint(0, high)
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