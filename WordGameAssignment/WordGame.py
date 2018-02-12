#
# Author: Craig Lawlor
# C00184465
#
# A program to make a word game where the user is given a source word.
# The user must then attempt to enter 7 words made up of letters
# within the source word. The user words must be greater than 3 in
# length. The user word also cannot be the source word
import random
import time
from collections import Counter
import pickle
# makes list of the dictionary
words = [line.strip().lower() for line in open('dictionary.txt')]
play = True

while play:
    source_word = ""
    start_time = time.time()
    lose = False

    # check for duplicates within the list
    def dup_check(the_list):
        the_set = set(the_list)
        if len(the_set) < len(the_list):
            return True
        else:
            return False

    # word length checker
    def word_length(the_word):
        if len(source_word) >= len(the_word) >= 3:
            return True
        elif len(the_word) > 7:
            print(the_word, " is too long")
            return False
        elif len(the_word) < 3:
            print(the_word, " is too short")
            return False

    # to see if the user word is within the source word
    def within(the_word):
        word_dict = dict(Counter(Counter(the_word)))
        letter = True
        for key in word_dict:
            if key in source_dict:
                if word_dict.get(key) > source_dict.get(key):
                    print(the_word, " has too many", key)
                    return False
            else:
                letter = False
                print(key, "not found in ", source_word)
        if letter:
            return True

    # to calculate the time taken
    def calculate_time(fin_time):
        total = fin_time - start_time
        return total

    # adding the player to the leaderboard
    def add_to_leaderboard(player_time, player_name):
        temp_tup = (player_time, player_name)
        read = open('Leaderboard.pkl', 'rb')
        score = pickle.load(read)
        score.append(temp_tup)
        score.sort()
        read.close()

        output = open('Leaderboard.pkl', 'wb')
        pickle.dump(score, output)
        output.close()

    # printing the leaderboard
    def print_leaderboard(player_time, player_name):
        printit = open('Leaderboard.pkl', 'rb')
        leader = pickle.load(printit)
        print("Top 10:")
        for i, item in enumerate(leader[:10]):
            print(i + 1, item)
        printit.close()
        temp_tup = (player_time, player_name)
        for i, item in enumerate(leader):
            if item == temp_tup:
                position = i + 1
        if position > 10:
            print("\nYour position is: ", position, " better luck next time")
        else:
            print("\nYour position is: ", position, " well done")

    # generating a word with at least 7 letters
    while len(source_word) <= 7:
        source_word = random.choice(words)
    # i like this (nesting counters)
    source_dict = dict(Counter(Counter(source_word)))

    # instructions for user
    print("\nEnter 7 words, 3 letters or more.\n"
          "From letters in the source word.\n"
          "Your word cannot be the source word.\n"
          "*Do not enter a space after last word\n"
          "\nSource word: ", source_word)

    # user input. beginning of checking
    user_words = list(input("Enter 7 words: \n").split(' '))
    # make user input lowercase
    user_words = [item.lower() for item in user_words]
    within_counter = 0
    if len(user_words) != 7:
        print("The number of words entered was", len(user_words), " not 7")
        lose = True
    for item in user_words:
        if item == source_word:
            lose = True
            print(item, " = source_word")
        if item not in words:
            print(item, "not found in dictionary")
            lose = True
        if not word_length(item):
            lose = True
        if within(item):
            within_counter += 1
    if dup_check(user_words):
        print("Duplicates were found")
        lose = True
    if within_counter != 7:
        lose = True

    # verdict
    if lose:
        print("You lose")
    else:
        print("You win")
        end_time = time.time()
        total_time = end_time - start_time
        name = input('Enter your name: \n')
        # sending the current players time and name
        add_to_leaderboard(total_time, name)
        print_leaderboard(total_time, name)

    again = input('Would you like to play again? (y/n) \n')
    if again == 'y':
        play = True
    elif again == 'n':
        play = False
