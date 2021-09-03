print("*********************************************HELLO THERE***************************************************")
print("**********************************WELCOME TO GUESSING THE NUMBER GAME*********************************")
import random
upper_number = input("Enter a number:- ")

def set_lives(num):
    if num > 0 and num < 11:
        number_of_lives = 10
    elif num > 10 and num < 21:
        number_of_lives = 15
    elif num > 20 and num < 31:
        number_of_lives = 20
    elif num > 30 and num < 41:
        number_of_lives = 25
    elif num > 40 and num < 51:
        number_of_lives = 30
    return number_of_lives


if upper_number.isdigit():
    upper_number = int(upper_number)
    if upper_number <= 0:
        print("Please enter a number larger than 0 next time.")
        quit()
    elif upper_number > 50:
        print("Please enter a number smaller than 50 next time.")
        quit()
else:
    print("Not a number! \nPlease type a number next time.")
    quit()

ran_num = random.randint(0, upper_number)
lives = set_lives(upper_number)
print("You have", lives, "lives")
guesses = 0
while True:
    guesses += 1
    lives -= 1
    guess = input("Make a guess:- ")
    if lives == 0:
        print("GAME OVER! \nBetter luck next time.")
        break
    else:
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please type a number next time.")
            continue
        if guess == ran_num:
            print("Correct!")
            print("you got it in", guesses, "guesses!")
            break
        elif guess > ran_num:
            print("You were above the number!                                                          Lives left: ", lives)
        else:
            print("You were below the number!                                                          Lives left: ", lives)