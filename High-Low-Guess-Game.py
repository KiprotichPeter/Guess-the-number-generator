import random #This will import random.
value = random.randint(1,100) #Generate a number between 1 and 100.
guess_num = int(input("Guess a number between 1 and 100?-->")) #Player must Guess a number between 1 and 100.
while value:
    if guess_num < value: #If the user guess number it less than the random number the it will print too low.
        print("Too low!")
        guess_num = int(input("Guess again?--> "))
    elif guess_num > value: #If the user guess number it more than the random number the it will print too High.
        print("Too High!")
        guess_num = int(input("Guess again?-->"))
    else:
         guess_num == value #If the user guess number is equal to the random number then it will print the guess number.
         print(f"Yes! {guess_num} was the number")
         play_again = input("Play again? Y to play again and N to stop playing ") #It will ask ask you if you want ot play again or quit.
         if play_again == "N": # If the user input is N. It will quit the game.
             print("Thanks for playing")
             break
         elif play_again == "Y": #If the user input if Y, then you will have a chance to play again.
            value = random.randint(-1,101) #Generate a random number between 1 and 100.
            guess_num = int(input("What is your guess: "))
         else:
             print("Thanks for playing")
