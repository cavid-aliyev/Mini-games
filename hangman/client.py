from hangman.game import Game
from hangman.game_status import GameStatus


def char_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

letters_count = len(word)

print(f"The word consists of {letters_count} letters.")
print("Try to guess the word letter by letter.")

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input("Pick a letter.\n")
    state = game.guess_letter(letter)

    print(char_list_to_str(state))

    print(f"Remaining tries = {game.remaining_tires}")
    print(f'Tried letters {char_list_to_str(game.tried_letters)}')

if game.game_status == GameStatus.LOST:
    print("Ypu are hanged!")
    print(f"the word was : {game.word}")
else:
    print("Congratulations You won!")
