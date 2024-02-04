import random
import logo_art

Easy_level_attempts = 10
Hard_level_attempts = 5

def set_difficulty(level_chosen):
    if level_chosen == 'Easy':
        return Easy_level_attempts
    elif level_chosen == 'Hard':
        return Hard_level_attempts
    else:
        return None


def check_answer(guessed_number, answer, attempts):
    if int(guessed_number) < answer:
        print("Too low to guess!!")
    elif int(guessed_number) > answer:
        print("Too high to guess!!")
    else:
        print(f"Your guess is right {answer}!")
        return True  
    return False

def game():
    print(logo_art.logo)
    print("Let me guess a number between 1 to 50")
    answer = random.randint(1, 50)
    print(answer)
    level = input("Choose the level of difficulty! Type 'Easy' or 'Hard': ")

    attempts = set_difficulty(level)
    if attempts!= Easy_level_attempts and attempts!= Hard_level_attempts:
        print("You have entered wrong difficulty level... PLAY AGAIN!")
        return
    guessed_number = 0

    while attempts > 0 and not check_answer(guessed_number, answer, attempts):
        print(f"You have {attempts} chance(s) remaining to guess the number")
        guessed_number = int(input("Guess a number: "))
        attempts -= 1

    if attempts == 0:
        print(f"You are out of chances!! YOU LOSE! The answer was {answer}")
    else:
        print("Congratulations! You guessed the correct number!")

game()

















