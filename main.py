import random
import string
import array

def word_iterator(guess, secret_word, guessed_letters, index=0):
    """
    Recursively updates guessed_letters with guess if it matches
    the character at the current index in secret_word.
    """
    if index >= len(secret_word):
        return
    if secret_word[index] == guess and guessed_letters[index] == "_":
        guessed_letters[index] = guess
    word_iterator(guess, secret_word, guessed_letters, index + 1)


def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """
    Updates the game state after a guess.
    Reveals guessed letters or decrements lives if guess is incorrect.
    Returns updated guessed_letters and lives.
    """
    if guess in secret_word:
        word_iterator(guess, secret_word, guessed_letters)
        print(f"Good job! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"Oops! '{guess}' is NOT in the word.")
    return guessed_letters, lives


def get_random_word(words_list: list[str]) -> str:
    """Returns a random word from the provided list."""
    return random.choice(words_list)


def game_loop(secret_word: str, guessed_letters: list[str], lives: int,auto_play):
    """
    Main game loop:
    - Ends if word is guessed or lives run out.
    - Prompts user for guesses and updates state.
    Returns True if player wins, False otherwise.
    """
    # Welcome and initial visualization
    print("Welcome to Hangman!")
    print(" ".join(guessed_letters))
    print(f"Lives remaining: {lives}")
    print("="*30)

    return recursive_game(secret_word, guessed_letters, lives,auto_play)

auto_play_letters = []
original_array =['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def recursive_game(secret_word: str, guessed_letters: list[str], lives: int,auto_play):
    """
    Recursive version of the game loop.
    """

    # Check final game state
    if "_" not in guessed_letters:
        print(f"Congratulations! You guessed the word: {secret_word}")
        return True

    if lives <= 0:
        print(f"Game Over! The word was: {secret_word}")
        return False

    # Prompt user for a guess
    if auto_play==0:
        guess = input("Guess a letter: ").strip().upper()
    elif auto_play == 1:
        # while 1:
            
            guess = random.choice(original_array)
            
            original_array.remove(guess)
            guess = guess.strip().upper()
            # if guess in auto_play_letters:
            #    continue
            # else :
            #    auto_play_letters.append(guess)
            #    break


               
       
       
    if not guess or len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter (A-Z).")
        return recursive_game(secret_word, guessed_letters, lives,auto_play)

    # Update game state based on guess
    guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)

    # Show current progress
    print(" ".join(guessed_letters))
    print(f"Lives remaining: {lives}")
    print("="*30)

    return recursive_game(secret_word, guessed_letters, lives,auto_play)


# Entry point: initializes game and starts main loop
if __name__ == "__main__":
    auto_play_letters = []
    words_list = [
        "APPLE", "BANANA", "ORANGE", "MANGO", "PINEAPPLE", "GRAPE", "CHERRY",
        "STRAWBERRY", "BLUEBERRY", "WATERMELON", "PEACH", "PLUM", "KIWI",
        "LEMON", "LIME", "COCONUT", "PAPAYA", "FIG", "POMEGRANATE", "GUAVA",
        "RASPBERRY", "BLACKBERRY", "MELON", "APRICOT", "NECTARINE", "TANGERINE",
        "PASSIONFRUIT", "DRAGONFRUIT", "DATE", "OLIVE"
    ]
    auto_play = int(input("Enter 1 for auto play else enter 0 : "))
    

    secret_word = get_random_word(words_list)
    guessed_letters = ["_" for _ in range(len(secret_word))]
    lives = 6
    game_loop(secret_word, guessed_letters, lives,auto_play)