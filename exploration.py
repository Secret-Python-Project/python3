def main():
  minimum = 1
  maximum = 1000

  introduce_game(minimum, maximum)
  guess = make_guess(minimum, maximum)
  answer = get_user_answer(guess)
  process_guess(answer, guess, minimum, maximum) # Order matters
  # Scope Matters

def introduce_game(minimum, maximum):
  print ("Welcome")
  # Add a delay of one second
  print ("Think of a number between " + str(minimum) + " and " + str(maximum))
  print ("I will try and guess it...\n")
  return

def make_guess(minimum, maximum):
  return int((minimum + maximum )/ 2)

def get_user_answer(guess):
  print("Is your number: " + str(guess) + "?")
  answer = input("Please type yes, higher or lower \n")
  return answer

def process_guess(answer, guess, minimum, maximum): # reduce to 2 params max
  if answer == "yes":
    game_won()

  elif answer == "higher":
    print("OK, I'll guess a higher number...")
    minimum = guess
    new_guess = make_guess(minimum, maximum)
    answer = get_user_answer(new_guess)
    process_guess(answer, new_guess, minimum, maximum)

  elif answer == "lower":
    print("OK, I'll guess a lower number...")
    maximum = guess
    new_guess = make_guess(minimum, maximum)
    answer = get_user_answer(new_guess)
    process_guess(answer, new_guess, minimum, maximum)

  else:
    print("Please type a valid answer..")
    answer = get_user_answer(guess)
    process_guess(answer, guess, minimum, maximum)

def game_won():
  print("Yes, I won!\n")

#Good luck explaining this one Mikey - "It's Magical" -Sam 2018 :D
if __name__ == "__main__":
  main()