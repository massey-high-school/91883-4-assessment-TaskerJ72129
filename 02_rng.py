import random

HIGH = int(input("High?"))

for item in range(1, 20):
    secret = random.randint(0, HIGH)
    print(secret, end="\t")