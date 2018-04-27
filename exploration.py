def main():
	minimum, maximum = introduce_game()
	guess = get_inital_guess(minimum, maximum)
	answer = start_guessing(guess)
	processing_guess(answer, guess)
	

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
    
    guess = (minimum + maximum )/ 2
    return int(guess)

def start_guessing(guess):
    print ("Is your number: " + str(guess))
    answer = input("Please type yes, higher or lower \n")
    return answer

def processing_guess(answer, guess):
    if answer == "yes":
		game_won()

    elif answer == "higher":
		print("OK, I'll guess a higher number...")
		minimum = guess
		start_guessing(guess)

    elif answer == "lower":
		print("OK, I'll guess a lower number...")
		maximum = guess
		start_guessing(guess)

    else:
		print("Please type a valid answer..")
		start_guessing(guess)

	return guess, minimum, maximum

def game_won():
    print("Yes, I won! \n")
    break

#Good luck explaining this one Mikey - "It's Magical" -Sam 2018 :D
if __name__ == "__main__":
  main()