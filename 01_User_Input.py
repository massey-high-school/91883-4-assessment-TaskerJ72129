def intcheck(question, low = None):

    # sets up error messages
    if low is 0:
        error = "Please enter an integer above 0"
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))
            # Checks response is not too low
            if low is None:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# Main routine

lowest = 0
high = intcheck("High Number", lowest)
rounds = intcheck("Rounds: ", lowest)
user_answer = intcheck("Guess: ", lowest)

