while True:
	str_in = input()

	if str_in == 'END':
		break
	else:
		L = len(str_in)
		for i in range(L):
			print(str_in[L - (i + 1)], end = '')
		print('')
