import math
import random

ASCII_ENGLISH_ALPHABET = range(97, 123)
WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    count_of_letter = 0
    for i in range(0, len(secret_word)):
        for j in range(0, len(letters_guessed)):
            if letters_guessed[j] == secret_word[i]:
                count_of_letter += 1
                break
    if count_of_letter == len(secret_word):
        return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    user_row = list('_' * len(secret_word))
    for i in range(0, len(secret_word)):
        for j in range(0, len(letters_guessed)):
            if letters_guessed[j] == secret_word[i]:
                user_row[i] = secret_word[i]
                break
    return ' '.join(user_row)

def get_available_letters(letters_guessed):
    list_of_letters = list(map(chr, ASCII_ENGLISH_ALPHABET))
    for letter in letters_guessed:
        for alphabet_letter in list_of_letters:
            if alphabet_letter == letter:
                list_of_letters.remove(alphabet_letter)
    return ''.join(list_of_letters)

def check_user_input(user_input):
    if len(user_input) != 1:
        return False
    if not user_input.isalpha():
        return False
    if ord(user_input) not in ASCII_ENGLISH_ALPHABET:
        return False
    return True

def match_with_gaps(my_word, other_word):
    my_word = ''.join(my_word.split(' '))

    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if (my_word[i] != '_') and (my_word[i] != other_word[i]):
            return False
    return True

def show_possible_matches(my_word):
    matches = []
    for word in WordList:
        if match_with_gaps(my_word, word):
            matches.append(word)
    return ' '.join(matches)

def hangman(secret_word):
    print(ord('a'))
    letters_guessed = []
    warnings = 3
    score = 0
    guesses = math.ceil(len(secret_word))
    while True:
        print('You have ' + str(warnings) + ' warnings left')
        print('You have ' + str(guesses) + ' guesses left')
        print('Available letters: ' + get_available_letters(letters_guessed))
        user_input = input('Please guess a letter: ')
        if user_input == '*' and len(letters_guessed) >= 2:
            print("Possible words: " + show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        elif not check_user_input(user_input):
            warnings -= 1
            print('Oops, that is not valid letter. You have ' + str(warnings) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
        elif user_input in get_guessed_word(secret_word, letters_guessed):
            warnings -= 1
            print('Oops! You have already guessed this letter. You have ' + str(warnings) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
        else:
            guesses -= 1
            score += 1
            letters_guessed.append(user_input)
            if is_word_guessed(secret_word, letters_guessed):
                print('Congratulations, you won! Your total score is: ' + str(score))
                break
            elif user_input in secret_word:
                print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! This letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed))

        if warnings == 0 and not check_user_input(user_input):
            print('Sorry, you ran out of warnings. The word was: ' + secret_word)
            break
        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was: ' + secret_word)
            break
        print('-------------------------------------------------------------')

WordList = load_words()

if __name__ == "__main__":
    secret_word = choose_word(WordList)
    hangman(secret_word)