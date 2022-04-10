# Guess the number using python 
n= 18
number_of_guesses =1
print("the nunber of guesses is limited to only 9 times")
while(number_of_guesses<=9):
  guess_number = int(input("Guess the number \n"))
  if guess_number<18:
    print("you enter the less number please enter the greater number \n")
  elif guess_number>18:
    print("you Enter the Greater number please Enter the less number \n")
  else:
    print("You won \n")
    break
  print(number_of_guesses, "no of guesses he took to finish.")
  print(9-number_of_guesses, "no of guesses left")
  number_of_guesses = number_of_guesses +1
  if (number_of_guesses>9):
    print("Game is over, Sorry you lost the game")