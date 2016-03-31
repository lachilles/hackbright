#Practice your lists, for-loops and functions in a file named yourlastname_animals.py.
#Inside this file, make a list of animals. You can call the list whatever you like, but animals would be a safe bet.
#Write a function called “k_animals” that takes a list. Inside this function, make a new empty list called k_list. Loop over the input list, and if you find a value that starts with the letter “k”, append it to k_list. At the end of the function, return k_list.
#Now call the function you just created, passing in the list of animals you made and saving the output to a new variable. Print that variable.

animals = ["tiger", "hippo", "lynx", "unicorn", "kangaroo"]

def k_animals(lst):
	k_list = []
	for s in lst: 
		if s[0] == "k":
			k_list.append(s)
	print k_list

new_animals = k_animals(animals) 

print new_animals
