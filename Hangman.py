import random
import time

print('Welcome to Hangman Game')
time.sleep(1)
print('The game is about to start!')
time.sleep(1)


def main():
    global count, display, word, c_guess, length, endgame

    words_to_guess = ["jungle", "anime", "movie", "flower", "panther", "king", "heart", "light", "songs",
                      "flute","plants"]

    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = ''
    for i in range(length):
        display += '_'
    c_guess = []
    playgame = ''


def play():
    global endgame
    endgame = input('Do you want to quit? y=yes , n=no : ')
    while endgame not in ['Y', 'y', 'N', 'n']:
        endgame = input('Do you want to quit? y=yes , n=no')

    if endgame == 'Y' or endgame == 'y':
        print('Thanks For Playing! Visit Again')
        exit()
    elif endgame == 'N' or endgame == 'n':
        main()


def hangman():
    global count, display, word, c_guess, length
    chances = 5
    print('This is the hangaman word : ', display)
    guess = input('Enter your guess : ')
    guess = guess.strip()
    if len(guess.strip()) <= 0 or len(guess.strip()) > 1 or guess <= '9':
        print('Invalid Entry! Try a letter')
        hangman()

    elif guess in word:
        c_guess.append(guess)
        ind = word.find(guess)
        word = word[:ind] + '_' + word[ind + 1:]
        display = display[:ind] + guess + display[ind + 1:]
        print(display)

    elif guess in c_guess:
        print('Try another letter')

    else:

        count += 1

        if count == 1:
            time.sleep(1)
            print("   ______ \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")


        elif count == 2:
            time.sleep(1)
            print("   ______ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")


        elif count == 3:
            time.sleep(1)
            print("   ______ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |      | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   ______ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |      | \n"
                  "  |      O \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   ______ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |      | \n"
                  "  |      O \n"
                  "  |     /|\ \n"
                  "  |     / \ \n"
                  "  |         \n"
                  "__|__\n")
            print('Wrong Guess! You are hanged')
            print("The word was:", c_guess, word)
            play()

    if word == '_' * length:
        print('You have guessed all letters correctly!')
        play()

    if count < chances:
        hangman()


main()
hangman()