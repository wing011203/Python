import glob
class DataParser():
	def __init__(self, name, dob, recs):
		self.name = name
		self.dob = dob
		self.recs = recs

	def getResult(self):
		print("Name:", self.name)
		print("Date of Birth:", self.dob)
		#print("Records:", self.recs)
		#return self.formatContent()
		return self.sortList(self.uniqueContent(self.formatContent()))

	def sortList(self,data):
		result = sorted(data)
		print('Sorted Value: ')
		print(result)
		return result

	def uniqueContent(self,data):
		#result = set(data)
		result = []
		for value in data:
			if not value in result:
				result.append(value)
		print('Unique Value:')
		print(result)
		return result

	def formatContent(self):
		#print("Original Value:")
		#print(content, end='')
		result = []
		for value in self.recs.split(','):
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
	except IOError as err:
		print("IO Error: " + str(err))
	except ValueError as err:
		print("Value Error: " + str(err))
	except:
		print("Unknown Error.")

	return result



if __name__ == '__main__':
	files = glob.glob('*.txt')
	for file in files:
		value = loadFile(file)
		temp = value.split(',', 2)
		parser = DataParser(temp[0], temp[1], temp[2])
		print("File:", file)
		print("Result:", parser.getResult()[:3])
