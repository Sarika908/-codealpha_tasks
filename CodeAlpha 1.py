import random
def choose_word():
    """Chooses a random word from a list."""
    word_list = ["apple", "banana", "orange", "grape", "watermelon", "mango", "pineapple", "strawberry", "kiwi", "blueberry"]  # You can expand this list
    return random.choice(word_list)
def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and others as underscores."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "  
        else:
            displayed_word += "_ "
    return displayed_word
def play_hangman():
    """Plays the Hangman game."""
    word_to_guess = choose_word()
    guessed_letters = set()  
    incorrect_guesses = 0
    max_incorrect_guesses = 6  
    print("Welcome to Hangman!")
    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:  
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            incorrect_guesses += 1
            print("Incorrect guess.")

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

        if incorrect_guesses >= max_incorrect_guesses:
            print("\nGame over! You ran out of guesses. The word was:", word_to_guess)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
      play_hangman()  
    else:
      print("Thanks for playing!")
if __name__ == "__main__":
    play_hangman()