#3. create a guessing game where the user has to guess a number between 1 and 10. Use a while loop to keep asking until the correct number (e.g 7) is guessed

secret_number = 6
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("YOU WON!")
        break
else:
    print("YOU FAILED!")