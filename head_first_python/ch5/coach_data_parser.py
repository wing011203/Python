def parse():
	'''
	try:
		with open('james.txt') as james_file:
			for line in james_file:
				print(line)

		with open('julie.txt') as julie_file:
			for line in julie_file:
				print(line)

		with open('mikey.txt') as mikey_file:
			for line in mikey_file:
				print(line)

		with open('sarah.txt') as sarah_file:
			for line in sarah_file:
				print(line)
	except IOError as err:
		print("IO Error: " + str(err))
	except ValueError as err:
		print("Value Error: " + str(err))
	'''
	top(uniqueContent(sortList(formatContent(loadFile('james.txt')))), 3)
	top(uniqueContent(sortList(formatContent(loadFile('julie.txt')))), 3)
	top(uniqueContent(sortList(formatContent(loadFile('mikey.txt')))), 3)
	top(uniqueContent(sortList(formatContent(loadFile('sarah.txt')))), 3)


def top(data, n):
	if len(data) < n:
		print('The length of list is larger than', n)
		return None
	print("Top", n, "result:")
	print(data[:n])
	return data[:n]

def sortList(data):
	result = sorted(data)
	print('Sorted Value: ')
	print(result)
	return result

def uniqueContent(data):
	#result = set(data)
	result = []
	for value in data:
		if not value in result:
			result.append(value)
	print('Unique Value:')
	print(result)
	return result

def formatContent(content):
	#print("Original Value:")
	#print(content, end='')
	result = []
	for value in content.split(','):
		if value.find('-') > -1:
			result.append(value.replace('-', ':').strip())
		elif value.find('.') > -1:
			result.append(value.replace('.', ':').strip())
		else:
			result.append(value.strip())
	print("Formatted Value:")
	print(result)
	return result


def loadFile(fileName):
	print("The content from", fileName, ':')
	result = ''
	try:
		with open(fileName) as f:
			for line in f:
				print(line, end='')
				result += line
				# formatContent(line)
	except IOError as err:
		print("IO Error: " + str(err))
	except ValueError as err:
		print("Value Error: " + str(err))
	except:
		print("Unknown Error.")

	return result



if __name__ == '__main__':
	parse()