import time

def make_state(minimum, maximum):
  return (make_guess(minimum, maximum), minimum, maximum)

def run_game():
  minimum = 1
  maximum = 1000
  state = make_state(minimum, maximum)

  introduce_game(state)
  answer = get_user_answer(state)
  process_guess(answer, state) # Order matters

def introduce_game(state):
  _, minimum, maximum = state # un-pack tuple
  print ("Welcome")
  time.sleep(1)
  print ("Think of a number between " + str(minimum) + " and " + str(maximum))
  print ("I will try and guess it...\n")
  return

def get_user_answer(guess):
  print("Is your number: " + str(guess) + "?")
  answer = input("Please type yes, higher or lower \n")
  return answer

def process_guess(answer, state): # reduce to 2 params max
  guess, minimum, maximum = state
  if answer == "yes":
    game_won()
  elif answer == "higher":
    guess_higher(answer, guess, minimum, maximum)
  elif answer == "lower":
    guess_lower(answer, guess, minimum, maximum)
  else:
    ask_again(answer, guess, minimum, maximum)

def game_won():
  print("Yes, I won!\n")

def make_guess(minimum, maximum):
  return int((minimum + maximum )/ 2)

def guess_higher(answer, state):
  print("OK, I'll guess a higher number...")
  guess,minimum,maximum = state
  minimum = guess
  state = guess,minimum,maximum
  next_guess(answer, state)

def guess_lower(answer, state):
  print("OK, I'll guess a lower number...")
  guess,minimum,maximum = state
  maximum = guess
  state = guess,minimum,maximum
  next_guess(answer, state)

def next_guess(answer, state):
  new_guess = make_guess(minimum, maximum)
  answer = get_user_answer(new_guess)
  state = make_state(minimum, maximum)
  process_guess(answer, state)

def ask_again(answer, state):
  print("Please type a valid answer..")
  answer = get_user_answer(guess)
  state = make_state(minimum, maximum)
  process_guess(answer, state)

# Calling from the terminal sets the calling module name as "__main__"
# Because this code is at indentaion level 0 it is run first
# We check if the calling module is "__main__" then run run_game()
# All the def(initions) above are defined but not run
# run_game() must be defined before it can be called
# ... so must all the other functions that run_game() calls