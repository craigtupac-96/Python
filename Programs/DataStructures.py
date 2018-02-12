# Author: Craig Lawlor
# C00184465
# A program to define data structures and use their operations

my_list = [1, 5, 27, 28]
my_set = {'banana', 'apple', 'pear', 'apple', 'pineapple'}     # unique data only (apple will be printed only once)
my_tuple = ('red', 'blue', 'green', 'black', 'yellow')         # tuples are immutable
my_dict = {'apple': 2.50, 'banana': 2.00, 'pear': 1.80, 'pineapple': 1.50}   # Keys and values

print("List: ", my_list)
print("Set: ", my_set)
print("Tuple: ", my_tuple)
print("Dictionary: ", my_dict)

# list functions ##########
# cmp(my_list, list2)     # compares elements of both lists
# len(my_list)            # gives total length of the list
# max(my_list)            # returns item from list with max value
# min(my_list)            # return item from list with min value
# a_list = list(my_tuple) # convert a tuple to a list

# list methods ##########
# my_list.append(47)       # appends obj to list
# my_list.count(47)        # Returns count of how many times obj occurs in list
# my_list.extend(another_list) # extend by adding another list
# my_list.index(27)        # returns the lowest index in list obj appears
# my_list.insert(index, obj)   # Inserts object obj into list at offset index
# my_list.pop()            # removes the last item
# my_list.remove(28)       # Removes object 28 from list
# my_list.reverse()        # reverses objects in list
# my_list.sort()           # sorts list objects

# set functions ############

# set methods ############
# my_set.update(t)	                # return set with elements added from t
# my_set.intersection_update(t)	    # return set keeping only elements also found in t
# my_set.difference_update(t)	        # return set after removing elements found in t
# my_set.symmetric_difference_update(t)	# return set with elements from my_list or t but not both
# my_set.add(x)	 	                # add element x to set
# my_set.remove(x)	 	            # remove x from set; raises KeyError if not present
# my_set.discard(x)	 	            # removes x from set if present
# my_set.pop()	 	                # remove and return an arbitrary element from set; raises KeyError if empty
# my_set.clear()        	        # remove all elements from set

# tuple functions #########  (immutable)
# cmp(my_tuple, tuple2)         # compare elements of both tuples
# len(my_tuple)                 # gives total length of tuple
# max(my_tuple)                 # return item from tuple with max value
# min(my_tuple)                 # return item from tuple with min value
# new_tuple = tuple(my_list)    # converts list into tuple

# tuple methods #########
# my_tuple.count('green')       # counts the number of times green appears
# my_tuple.index('green')       # returns the index position of green

# dictionary functions ########
# cmp(my_dict, dict2)          # compares elements of both dict
# len(my_dict)                 # gives total length of dict
# str(my_dict)                 # produces printable string representation of a dictioanry
# type(variable)               # returns type of passed variable

# dictionary methods ##########
# my_dict.clear()                         # removes all elements
# my_dict.copy()                          # returns a shallow copy
# my_dict.fromkeys()                      # Create a new dictionary with keys from seq and values set to value.
# my_dict.get(key, default=None)          # For key key, returns value or default if key not in dictionary
# my_dict.has_key(key)                    # Returns true if key in dictionary dict, false otherwise
# my_dict.items()                         # Returns a list of dict's (key, value) tuple pairs
# my_dict.keys()                          # Returns list of dictionary dict's keys
# my_dict.setdefault(key, default=None)   # Similar to get(), but will set dict[key]=default if key is not already in dict
# my_dict.update(dict2)                   # Adds dictionary dict2's key-values pairs to dict
# my_dict.values()                        # Returns list of dictionary dict's values










