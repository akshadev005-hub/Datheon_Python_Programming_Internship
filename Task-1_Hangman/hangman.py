
import random
import os

# ASCII Hangman stages (0 to 6 incorrect guesses)
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

MAX_ATTEMPTS = 6


# Load words from words.txt
def load_words():
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "words.txt"
    )

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = [
                word.strip().lower()
                for word in file
                if word.strip().isalpha()
            ]

        if not words:
            raise ValueError("The word list is empty.")

        return words

    except FileNotFoundError:
        print("Error: words.txt file not found!")
        print("Please place words.txt in the same folder as hangman.py.")
        raise SystemExit


# Display the hidden word
def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


# Main Hangman game
def play_hangman():

    word_list = load_words()
    secret_word = random.choice(word_list)

    guessed_letters = set()
    wrong_guesses = set()

    attempts_left = MAX_ATTEMPTS

    print("\n================================")
    print("       HANGMAN WORD GAME")
    print("================================")
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect attempts.")
    print("--------------------------------")

    while attempts_left > 0:

        print(HANGMAN_STAGES[len(wrong_guesses)])

        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Incorrect guesses:", ", ".join(sorted(wrong_guesses)) or "None")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")
        print("Attempts remaining:", attempts_left)

        # Check for victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("The secret word was:", secret_word)
            print("You won the game!")
            return

        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabet.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You have already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Check the guessed letter
        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses.add(guess)
            attempts_left -= 1
            print("Wrong guess!")

    # Game over
    print(HANGMAN_STAGES[MAX_ATTEMPTS])
    print("\n================================")
    print("           GAME OVER")
    print("================================")
    print("You have used all 6 attempts.")
    print("The correct word was:", secret_word)
    print("Better luck next time!")


# Run the game
if __name__ == "__main__":
    play_hangman()
