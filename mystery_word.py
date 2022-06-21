import random

def play_game():
    answer = generate_word_for_game()
    print(f"answer: {answer}")
    print("_" * len(answer))

    guesses = []

    while len(guesses) <= 8:
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
    return answer

def guess_character():
    guess = input("Guess a letter:\n")
    return guess

if __name__ == "__main__":
    play_game()
