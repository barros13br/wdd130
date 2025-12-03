key_word = "samsung"
tries = 1

print("Welcome to the word guessing game!")
print()
print("Your hint is: ", end="")
for key_word_index in range(len(key_word)):
    hide_key_word = key_word[key_word_index]
    print("_ ", end="")

print()
guess = input(f"The word has {len(key_word)} letters. What is your guess? ")



while guess != key_word:
    tries + 1
    while len(guess) != len(key_word):
        print()
        print("Sorry, the guess must have the same number of letters as the secret word.")
        guess = input(f"Remember, the word has {len(key_word)} letters. What is your guess? ")
        print("Your hint is: ", end="")
        tries + 1
    for letter_key_word_index in range(len(guess)):
        letter = key_word[letter_key_word_index]
        if guess[letter_key_word_index] == letter:
            print(f"{guess[letter_key_word_index].upper()} ", end="")
        elif guess[letter_key_word_index] in key_word:
            print(f"{guess[letter_key_word_index].lower()} ", end="")
        else:
            print("_ ", end="")
    guess = input(f"Enter you guess again: ")

print("Congratulations! You guessed it!")
print(f"It took you {tries} guesses.")