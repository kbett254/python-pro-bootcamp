import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo)
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

placeholder = ["_"] * len(chosen_word)
print(" ".join(placeholder))

lives = len(stages) - 1
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            placeholder[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose. The word was " + chosen_word)
    print(stages[lives])
    print(" ".join(placeholder))

    if "_" not in placeholder:
        game_over = True
        print("You win!")


