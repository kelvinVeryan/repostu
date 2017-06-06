
movies=["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam", "Eric Idle","Terry Jones"]]]

import sys;
print sys.path

"""	This is the "nester.py" module and it provides one function called print_lol()
		which prints lists that may or may not include nested lists. """


def print_lol(the_list):
	""" This function takes one positional argument called "the_list" , which 
			is any Python list (of - possibly - nested lists). Each data tem in the 
			provided list is (recursively) printed to the screen on it's own line."""
			
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)
			
print_lol(movies)