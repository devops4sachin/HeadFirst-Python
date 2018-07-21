try:
	with open('myfile.txt') as fh:
		content = fh.read()
	print(content)
except FileNotFoundError:
	print('File does not exist')
except PermissionError:
	print('Not valid permissions for file access')
except Exception as err:
	print('Some other error occured: ',str(err))
