animals = ["tiger", "hippo", "lynx", "unicorn", "kangaroo"]

def k_animals(lst):
	k_list = []
	for s in lst: 
		if s[0] == "k":
			k_list.append(s)
	print k_list

new_animals = k_animals(animals) 

print new_animals
