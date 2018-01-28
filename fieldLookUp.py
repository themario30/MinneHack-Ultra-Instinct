def fileLine(name, var):
	fileName = 'fields/' + name
        mode = 'r'
	with open(fileName, mode) as file:
		for num, line in enumerate(file):
			if var == num:
				print(line)
		
	file.closed

