#3. create a guessing game where the user has to guess a number between 1 and 10. Use a while loop to keep asking until the correct number (e.g 7) is guessed

secret_number = 6  # Set a secret number
guess_count = 0  # Initialize the number of guesses made
guess_limit = 3  # Set the maximum number of guesses allowed

while guess_count < guess_limit:  # Loop through until guess limit reached
    guess = int(input("Guess: "))  # Ask users to enter their guess
    guess_count += 1  # Increment the guess count
# Check if user guess matches the secret number
    if guess == secret_number:
# When user matches secret number, the guess stop and display winning message
        print("YOU WON!")
        break
# calculate and display a message when user exceed maximum guess limit
else:
    print("YOU FAILED!")