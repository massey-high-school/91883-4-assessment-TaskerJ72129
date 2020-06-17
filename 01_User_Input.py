def intcheck(question, low = None):

    # sets up error messages

    error = "Please enter an integer"
    error2 = "please enter an integer above 0"
    while True:

        try:
            response = int(input(question))
            # Checks response is not too low
            if low is None:
                print(error)
                continue
            elif low == 0:
                print(error2)
            return response

        except ValueError:
            print(error)
            continue

# Main routine
# Main routine

lowest = 0
high = intcheck("High Number", lowest)
rounds = intcheck("Rounds: ", lowest)
user_answer = intcheck("Guess: ", lowest)

