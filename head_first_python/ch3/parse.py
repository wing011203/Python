def parseContent():
	man = []
	other = []
	#result = []

	try:
		for line in open('sketch.txt'):
			try:
				(role, content) = line.split(":", 1)
				# print (role, end = '')
				# print(' says: ', end = '')
				# print(content, end = '')
				# result.append(role + ' said: ' + content)
				if (role.strip() == 'Man'):
					man.append(content.strip())
				elif (role.strip() == 'Other Man'):
					other.append(content.strip())
				
			except:
				pass
	except:
		print('File Error!')

	print('man count:', len(man))
	
	print ('other count:', len(other))
	man_data = open('man-data', 'w')
	other_data = open('other-data', 'w')
	import nester
	#print('man content:')
	nester.print_lol(man, output = man_data)
	#print('other content:')
	nester.print_lol(other, output = other_data)
	
	#import nester
	#nester.print_lol(result)


if __name__ == '__main__':
	parseContent()