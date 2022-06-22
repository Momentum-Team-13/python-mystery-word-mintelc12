import random

def play_game():
    answer = generate_word_for_game()
    print(f"answer: {answer}")
    print("_" * len(answer))

    user_guesses_letter(answer)

    # check guesses list against answer
    # render new result


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

    return answer_string

def user_guesses_letter(answer_string):
    # Appends correct letters to a list for user to see

    correct_letter_guessed = []
    incorrect_letter_guessed = []
    while len(incorrect_letter_guessed) < 8:
        letter = guess_character()

        # for letter in list(answer_string):
        if any([letter in list(answer_string)]):
            correct_letter_guessed.append(letter)
            print(f"Your guess of {letter} is in the mystery word!")
            print(f"Correct letters:{correct_letter_guessed}")
        else: 
            print(f"Sorry, {letter} is not in the mystery word.")
            
            # Appends incorrect letters to a list for user to see    
            incorrect_letter_guessed.append(letter)
            print(f"Incorrect letters:{incorrect_letter_guessed}")
    
def guess_character():
    guess = input("Guess a letter:\n")

    return guess



if __name__ == "__main__":
    play_game()
