import sys

def print_lol(the_list, level = 0, indent = True, output = sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, level + 1, output)
		else:
			if indent == True:
				for i in range(level):
					print('\t', end='', file = output)
			print(each_item, file = output)