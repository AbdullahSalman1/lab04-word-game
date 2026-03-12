states of games :

                 Start game
                 Randomly pickup the word
                 Ask user to start guessing the word
                 Checking whether using uesses correct or wrong
                 Checking if user runs out of lives
                 Checking lives and score 

variables required :
                  Lives
                  CorrectGuesses
                  WrongGuesses
                  Win 
                  Lose

Rules and Invariants: 
                   If user gets out of turns then the game over and user loses
                   If user guessed the correct word then he wins
                   Letter should be placed in this right position
                   Total number of words remain same


Bugs and Edge cases:
                   Dealing with duplicate letters


Copilot Suggestions:

App states :

               The states i think i missed while copilot gave me are :
               Displaying the Word: The game displays the word with underscores for each letter.
               Displaying Incorrect Guesses: The game displays the incorrect guesses made by the player.
               Checking the Guess: The game checks if the player's guess is correct and updates the display accordingly.


Variables :
             Chances
             GuessedLetters

Rules and invariants :
                      Word Selection: The game selects a word for the player to guess. This word should be chosen randomly from a predefined list of words or generated dynamically.
                       

                       The player enters a guess, which is validated and processed. The guess should be a single letter.


Possible bugs and errors :

                        Invalid Guess Validation: The game may not properly validate the player's guess, allowing invalid inputs or multiple letters to be entered.



                        Incorrect Guess Checking: The game may not correctly check if the player's guess is correct or incorrect, leading to incorrect updates in the display or the number of guesses.

                        Display Updates: The game may not correctly update the display of the word, leading to incorrect visual feedback for the player.



Did copilt overcomplicate or underspecify ?

                                   I think sometimes it overcomplicates the things and make it more complex
                                   but mostly it helps us in tackling the problems we face

Does that help in any way ? 


                        Copilot really helps when it comes to edge cases or debugging.
                        It can help us thinking beyond the scene and solving the problem with 
                        a different approach

                        
                   










