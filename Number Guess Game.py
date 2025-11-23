import random

while True:
    # User chooses upper limit
    upper_limit = int(input("Choose the maximum number (e.g., 50, 100, 500): "))
    comp_choice = random.randint(1, upper_limit)
    
    attempt = 0

    print(f"\nGuess the number between 1 and {upper_limit}!")

    user_choice = int(input("Enter your guess: "))

    while user_choice != comp_choice:
        attempt += 1

        if user_choice < comp_choice:
            print("Your guess is smaller than the actual number.")
        elif user_choice > comp_choice:
            print("Your guess is greater than the actual number.")

        user_choice = int(input("Guess again: "))

    attempt += 1

    print(f"\n🎉 Congratulations! You guessed it right.")
    print(f"📌 The number was: {comp_choice}")
    print(f"🔢 Total attempts: {attempt}\n")

    # Play Again Option
    play_again = input("Do you want to play again? (Y/N): ")

    if play_again.lower() != "y":
        print("\nThanks for playing! Goodbye 👋")
        break

    print("\n----------------------------------------\n")
