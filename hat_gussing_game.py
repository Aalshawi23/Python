"""
Hat and Ball Guessing Game 🎩🎱
Author: Alaa
Description:
A simple Python console game where the player guesses which hat hides the ball.
This project demonstrates basic Python concepts: functions, lists, loops, conditionals, and user input.
"""

from random import shuffle


def shuffle_list(hats):
    """
    Shuffle the list of hats and return the randomized version.
    """
    shuffle(hats)
    return hats


def player_guess():
    """
    Ask the player to pick a hat number (0, 1, or 2).
    Keeps asking until a valid input is given.
    """
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number (0, 1, or 2): ")
    return int(guess)


def check_guess(hats, guess):
    """
    Check if the player's guess finds the ball.
    Print the result and reveal the hat positions.
    """
    if hats[guess] == 'O':
        print("\n🎉 Correct! You found the ball!")
    else:
        print("\n❌ Wrong guess! Try again next time.")
    print(f"The hats were: {hats}")


def play_game():
    """
    Main function that runs the Hat and Ball Guessing Game.
    Shuffles hats, asks for a guess, checks it, and lets the user play again.
    """
    print("🎩 Welcome to the Hat and Ball Guessing Game! 🎱")

    play_again = 'y'
    while play_again.lower() == 'y':
        hats = [' ', 'O', ' ']
        print("\nShuffling hats...\n")
        shuffled_hats = shuffle_list(hats)
        print("[ _ ] [ _ ] [ _ ]")  # visual placeholders before the guess

        guess = player_guess()
        check_guess(shuffled_hats, guess)

        play_again = input("\nPlay again? (y/n): ")

    print("\nThanks for playing! Goodbye 👋")


# Run the game when the file is executed directly
if __name__ == "__main__":
    play_game()
