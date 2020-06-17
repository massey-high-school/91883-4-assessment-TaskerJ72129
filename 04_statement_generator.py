# quiz quest component 4 - statement generator

def quiz_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))

answer = 10
rounds = int(input("How many rounds?  "))
# Main routine
# happy pointing
print()
right = quiz_statement("(☞ﾟヮﾟ)☞ WOW! You got it right ☜(ﾟヮﾟ☜)   ", "*")
# hashtags
print()
start_round = quiz_statement("###  Round 1 of {}  ###".format(rounds), "#")
# table flip
print()
lose = quiz_statement("(╯°□°）╯︵ ┻━┻ WRONG! the answer was {} (╯°□°）╯︵ ┻━┻  ".format(answer),   "-")