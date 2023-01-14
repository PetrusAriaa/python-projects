from random import randint

print("=== GUESS THE NUMBER BETWEEN 1 TO 99!!! ===")
my_number = randint(1, 100)

for count in range(10):
    try:
        guess = int(input(">>> Insert your guess: "))
        if guess == my_number:
            print("You guessed it!")
            break
        elif guess < my_number:
            print("Too low!")
        elif guess > my_number:
            print("Too high!")
    except ValueError:
        print("Invalid input!")
        continue
