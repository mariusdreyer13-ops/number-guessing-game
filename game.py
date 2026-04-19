import random

def get_difficulty():
    print("Choose difficulty:")
    print("  1. Easy   (1-50)")
    print("  2. Medium (1-100)")
    print("  3. Hard   (1-200)")
    choice = input("Enter 1, 2 or 3: ")
    return {"1": 50, "2": 100, "3": 200}.get(choice, 100)

def play():
    limit = get_difficulty()
    number = random.randint(1, limit)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {limit}. Good luck!\n")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"\nCorrect! You got it in {attempts} attempts.")
            again = input("Play again? (y/n): ")
            if again.lower() == "y":
                play()
            break

print("Welcome to the Number Guessing Game!")
if __name__ == "__main__":
    play()
