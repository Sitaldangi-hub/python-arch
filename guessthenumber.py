import random


def computer_number(number_range2):
    computer_number = random.randint(1, number_range2)
    return computer_number



def main():

    number_range = int(input("pick your range of number form 1 to ___: "))
    com_holder = computer_number(number_range)
    life_left = True
    level = int(input("pick your level: \n "
                      "For hard level type 1 \n "
                      "For hard level type 2 \n"
                       "For Hard level type 3 \n"))
    def choose_your_level(level1):
        if level1 == 1:
            return  10
        elif level1 == 2:
            return 8

        elif level1 == 3:
            return life == 5

    life = choose_your_level(level)

    print(life)
    while life_left or life == 0:
        user_guess = int(input(f"Guess the number from 1 to {number_range}: "))

        if user_guess == com_holder:
            life_left = False
            print(f"You win! with {life} left.")
        elif user_guess > com_holder:
           print("Lower")
           life -= 1
           print(f"Life {life} left.")
        elif user_guess < com_holder:
            print("Higher")
            life -= 1
            print(f"Life {life} left.")
        else:
            print("Not valid, guess again")
            print(f"Life {life} left.")



main()