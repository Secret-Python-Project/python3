def introduce_game():
    #Set game conditions
    minimum = 1
    maximum = 1000

    print ("Welcome")
    # Add a delay nof one second
    print ("Think of a number between " + str(minimum) + " and " + str(maximum))
    print ("I will try and guess it...\n")
    return minimum , maximum

def get_inital_guess(minimum, maximum):
    print(minimum)
    guess = (minimum + maximum )/ 2
    return guess

def start_guessing(guess):
    print ("Is your number: " + str(guess))
    answer = input("Please type yes, higher or lower \n")
    return answer

def won_game():
    print("Yes, I won! \n")

def check_guess(answer):
    if answer == "yes":
        won_game()

    elif answer == "higher":
        print("OK, I'll guess a higher number...")

    elif answer == "lower":
        print("OK, I'll guess a lower number...")

    else:
        print("Please type a valid answer..")
        start_guessing(guess)
    return guess

minimum, maximum = introduce_game()
guess = get_inital_guess(minimum, maximum)
answer = start_guessing(guess)
check_guess(answer)