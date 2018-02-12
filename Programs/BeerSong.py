# Beer Bottle Song
counter = 99
the_string = '%s bottles of beer on the wall\n%s bottles of beer. \n' \
             'Take one down and pass it around\n%s bottles of beer on the wall\n'

while counter > -1:               # don't forget colon
        if counter > 1:
            print(the_string % (counter, counter, counter - 1))
        elif counter == 1:
            print('1 more bottle of beer on the wall.\none more bottle of beer.\n'
                  'Take one down and pass it around\n0 bottles of beer on the wall\n')
        elif counter == 0:
            print('No more bottles of beer on the wall.\nno more bottles of beer.'
                  '\nGo to the store and buy some more,\n99 bottles of beer on the wall.')
        counter = counter - 1