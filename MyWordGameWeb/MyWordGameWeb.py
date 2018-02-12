#
# Author: Craig Lawlor
# C00184465
#
from flask import Flask, render_template, request, session
from collections import Counter
import os.path
import random
import time
import pickle


scriptpath = os.path.dirname(__file__)  # had trouble opening the txt file
filename = os.path.join(scriptpath, 'dictionary.txt')
words = [line.strip().lower() for line in open(filename)]  # makes list of the dictionary


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           the_title='Word Game')


@app.route('/game')
def game():
    source_word = ""
    session['error_list'] = []
    # generating a word with at least 7 letters
    while len(source_word) <= 7:
        source_word = random.choice(words)
    session['source_word'] = source_word
    session['source_dict'] = dict(Counter(Counter(source_word)))# i like this (nesting counters)
    session['start_time'] = time.time()
    return render_template('game.html',
                           the_title='Word Game',
                           the_source=source_word)


def main(user_words):
    user_words = [item.lower() for item in user_words]
    session['user_words'] = user_words
    within_counter = 0
    source_word = session.get('source_word')
    start_time = session.get('start_time')
    lose = False
    session['win'] = False
    if len(user_words) != 7:
        session.get('error_list').append("The number of words entered was " + str(len(user_words)) + " not 7")
        lose = True
    for item in user_words:
        if item == source_word:
            lose = True
            session.get('error_list').append(item + " = source word")
        if item not in words:
            session.get('error_list').append(item + " not found in dictionary")
            lose = True
        if not word_length(item):
            lose = True
        if within(item):
            within_counter += 1
    if dup_check(user_words):
        session.get('error_list').append('Duplicates were found')
        lose = True
    if within_counter != 7:
        lose = True
        # verdict
    if lose:
        session['win'] = False
    else:
        session['win'] = True
        end_time = time.time()
        session['total_time'] = end_time - start_time


# word length checker
def word_length(the_word):
    if len(session.get('source_word')) >= len(the_word) >= 3:
        return True
    elif len(the_word) < 3:
        session.get('error_list').append(the_word + " is too short")
        return False


# to see if the user word is within the source word
def within(the_word):
    word_dict = dict(Counter(Counter(the_word)))
    letter = True
    for key in word_dict:
        if key in session.get('source_dict'):
            if word_dict.get(key) > session.get('source_dict').get(key):
                session.get('error_list').append(the_word + " has too many " + key)
                return False
        else:
            letter = False
            session.get('error_list').append(key + " not found in " + session.get('source_word'))
    if letter:
        return True


# check for duplicates within the list
def dup_check(the_list):
    the_set = set(the_list)
    if len(the_set) < len(the_list):
        return True
    else:
        return False


# adding the player to the leaderboard
def add_to_leaderboard(player_name):
    player_time = session.get('total_time')
    temp_tup = (player_time, player_name)
    read = open(os.path.join(scriptpath, 'Leaderboard.pkl'), 'rb')
    score = pickle.load(read)
    score.append(temp_tup)
    score.sort()
    read.close()
    output = open(os.path.join(scriptpath, 'Leaderboard.pkl'), 'wb')
    pickle.dump(score, output)
    output.close()


# printing the leaderboard
def print_leaderboard(player_name):
    player_time = session.get('total_time')
    printit = open(os.path.join(scriptpath, 'Leaderboard.pkl'), 'rb')
    leader = pickle.load(printit)
    print("Top 10:")
    leader_list = []
    for i, item in enumerate(leader[:10]):
        print(i + 1, item)
        leader_list.append(item)
    printit.close()
    session['leader_list'] = leader_list
    temp_tup = (player_time, player_name)
    for i, item in enumerate(leader):
        if item == temp_tup:
            position = i + 1
    session['position'] = position
    if position > 10:
        print("\nYour position is: ", position, " better luck next time")
    else:
        print("\nYour position is: ", position, " well done")


@app.route('/processform', methods=['GET', 'POST'])
def form_process():
    if request.method == 'POST':
        user_input = request.form['user_input']
        user_words = list(user_input.split(' '))
        main(user_words)
        session['count'] = 0
        if session.get('win'):
            return render_template('winner.html',
                                   the_title='Congratulations',
                                   the_time=session.get('total_time'))
        elif not session.get('win'):
            return render_template('loser.html',
                                   the_title='Unlucky',
                                   user_words=session.get('user_words'),
                                   error_list=session.get('error_list'))
    return 'Please use GET or POST.'


@app.route('/Win', methods=['GET', 'POST'])
def winner():
    if session.get('count') == 0:
        if request.method == 'POST':
            name = request.form['name']
            # sending the current players time and name
            add_to_leaderboard(name)
            print_leaderboard(name)
            session['count'] = 1
    return render_template('leaderboard.html',
                           the_title='Leaderboard',
                           the_leaderboard=session.get('leader_list'),
                           the_time=session.get('total_time'),
                           the_position=session.get('position'))


if __name__ == '__main__':
    app.secret_key = 'youwillneverguess'
    app.run(debug=True)
