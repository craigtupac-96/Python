# First Program
from datetime import datetime
from random import randrange
from time import sleep

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for _i in range(5):

    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        # Do this if true
        print('This minute seems a little odd')
    else:
        # Do this if false
        print('Not an odd number')

    how_long = randrange(1, 30)
    sleep(how_long)