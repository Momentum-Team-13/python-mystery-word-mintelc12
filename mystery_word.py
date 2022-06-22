import random

def play_game():
    answer = generate_word_for_game()
    print(f"answer: {answer}")
    print("_" * len(answer))

    guesses = []

    while len(guesses) < 8:
        guesses.append(guess_character())
    print(f"Your guesses: {guesses}")

    # check guesses list against answer
    # render new result
    new_list = [char for char in guesses if char in answer]
    print(new_list)


def generate_word_for_game():
    # open words.txt as read
    file = "words.txt"
    with open(file) as open_file:
        read_file = open_file.read()

    # Turn file into list of strings
    word_list = str.split(read_file)

    # Selet and return a random word from list
    index = random.randint(0, (len(word_list) - 1))
    answer = word_list[index]

    # converts random word into string
    answer_string = str(answer)

    # displays letters of random word in list and prints list
    list(answer_string)
    print(list(answer_string))

    # Appends correct letters to a list for user to see
    correct_letter_guessed = []
    letter = input("")
    for letter in list(answer_string):
        if any([letter in list(answer_string)]):
            correct_letter_guessed.append(letter)
            print(f"Your guess of {letter} is in the mystery word!")
        else:
            print(f"Sorry, {letter} is not in the mystery word.")
    print(f"Correct letters:{correct_letter_guessed}")

    # Appends incorrect letters to a list for user to see    
    incorrect_letter_guessed = []
    # for letter in answer_string:
    if letter not in answer_string:
            incorrect_letter_guessed.append(letter)
    print(f"Incorrect letters:{incorrect_letter_guessed}")
    
    return answer


def guess_character():
    guess = input("Guess a letter:\n")

    return guess



if __name__ == "__main__":
    play_game()
