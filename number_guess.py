import random

user_inp = input("Type a number:")
if user_inp.isdigit():
    user_inp = int(user_inp)

    if user_inp <= 0:
        print("please enter number larger than 0 next time.")
        quit()
else:
    print("please enter number next time.")
    quit()

random_num = random.randint(0, user_inp)
print("The required number is ", random_num)
guesses = 0
while True:  # For repetitive guessing, a while loop will be initialized.
    guesses += 1
    user_guess = input("make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please rtype number next time.")
        continue

    if user_guess == random_num:
        print("You got it")

        break

    elif user_guess > random_num:
        print("You got it wrong. Your number is greater than guessing number.")
    else:
        print("You got it wrong.Your number is less than guessing number")

#And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
print("Congratulations!!! You got it in ", guesses, "guesses")
