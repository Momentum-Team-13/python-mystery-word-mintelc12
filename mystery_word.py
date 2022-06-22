import random

def play_game():
    answer = generate_word_for_game()
    print(f"answer: {answer}")
    print("_" * len(answer))

    user_guesses_letter(answer)

    return answer
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
    word_to_guess = list("_" * len(answer_string))
    print(word_to_guess)
    while len(incorrect_letter_guessed) < 8 and "_" in word_to_guess:
        letter = guess_character()

        # for letter in list(answer_string):
        if any([letter in list(answer_string)]):
            correct_letter_guessed.append(letter)
            # Range goes from 0 to the length of object
            for letter_index in range(len(list(answer_string))):
                if list(answer_string)[letter_index] == letter:
                    # letter_index = list(answer_string).index(letter)
                    word_to_guess[letter_index] = letter
            print(word_to_guess)
            print(f"Your guess of {letter} is in the mystery word!")
            print(f"Correct letters:{correct_letter_guessed}")
        elif len(letter) > 1:
            print("Oops! Only guess one letter at a time!")
        else: 
            print(f"Sorry, {letter} is not in the mystery word. You have {7 - len(incorrect_letter_guessed)} guesses left.")
            
            # Appends incorrect letters to a list for user to see    
            incorrect_letter_guessed.append(letter)
            print(f"Incorrect letters:{incorrect_letter_guessed}")
    if len(incorrect_letter_guessed) == 8:
        print("Sorry, you lost!")
    else:
        print("Hooray! You won the game!")
    

def guess_character():
    guess = input("Guess a letter:\n")

    return guess



if __name__ == "__main__":
    play_game()
