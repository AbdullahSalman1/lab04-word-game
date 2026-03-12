import unittest
from main import update_game_state

class TestHangmanGame(unittest.TestCase):
    def test_correct_guess(self):
        secret_word = "APPLE"
        guessed_letters = ["_", "_", "_", "_", "_"]
        guess = "A"
        lives = 6
        updated, new_lives = update_game_state(secret_word, guessed_letters.copy(), guess, lives)
        self.assertEqual(updated, ["A", "_", "_", "_", "_"])
        self.assertEqual(new_lives, 6)

    def test_incorrect_guess(self):
        secret_word = "APPLE"
        guessed_letters = ["_", "_", "_", "_", "_"]
        guess = "Z"
        lives = 6
        updated, new_lives = update_game_state(secret_word, guessed_letters.copy(), guess, lives)
        self.assertEqual(updated, ["_", "_", "_", "_", "_"])
        self.assertEqual(new_lives, 5)

    def test_multiple_occurrences(self):
        secret_word = "APPLE"
        guessed_letters = ["_", "_", "_", "_", "_"]
        guess = "P"
        lives = 6
        updated, new_lives = update_game_state(secret_word, guessed_letters.copy(), guess, lives)
        self.assertEqual(updated, ["_", "P", "P", "_", "_"])
        self.assertEqual(new_lives, 6)

    def test_repeated_guess(self):
        secret_word = "APPLE"
        guessed_letters = ["A", "_", "_", "_", "_"]
        guess = "A"
        lives = 6
        updated, new_lives = update_game_state(secret_word, guessed_letters.copy(), guess, lives)
        self.assertEqual(updated, ["A", "_", "_", "_", "_"])
        self.assertEqual(new_lives, 6)

    def test_case_sensitivity(self):
        secret_word = "APPLE"
        guessed_letters = ["_", "_", "_", "_", "_"]
        guess = "a"  # Lowercase guess
        lives = 6
        updated, new_lives = update_game_state(secret_word, guessed_letters.copy(), guess, lives)
        # Depending on your design, this may or may not match. Here, we expect no match.
        self.assertEqual(updated, ["_", "_", "_", "_", "_"])
        self.assertEqual(new_lives, 5)

if __name__ == "__main__":
    unittest.main()
