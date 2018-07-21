class ConnectionError(Exception):
	pass

try:
	raise ConnectionError('Whoops, custom error')
except ConnectionError as err:
	print('Got: ', str(err))
