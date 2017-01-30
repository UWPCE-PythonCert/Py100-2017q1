for i in range(1,101):
	
#attempt number 1 (which worked)
	'''
	if i % 3 == 0 and i % 5 == 0:
		print('FizzBuzz')
	elif i % 3 == 0:
		print('Fizz')
	elif i % 5 == 0:
		print('Buzz')
	else:
		print(i)
	'''

#attempt number two, which is a bit neater
	count = ''
	if i % 3 == 0:
		count += 'Fizz'
	if i % 5 == 0:
		count += 'Buzz'
	if count == '':
		count = i
	print(count)