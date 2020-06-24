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

# Main routine
# Main routine

lowest = 0
high = intcheck("Highest Number:", 1)
max = high*2
rounds = intcheck("Rounds: ", 1)
user_answer = intcheck("Guess: ",1)

