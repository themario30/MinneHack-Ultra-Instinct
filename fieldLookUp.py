def fileLine(var):
	
	with open("fields/primarytypeofinjury.txt", "r") as file:
		for num, line in enumerate(file):
			if var == num:
				print(line)
		
		
		
	file.closed

