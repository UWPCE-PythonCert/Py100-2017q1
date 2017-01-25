#!/home/vagrant/.virtualenvs/py100/bin/python
def print_grid(n):
	num=int((n-1)/2)
	print('+',end='')
	print('-' * num,end='')
	print('+',end='')
	print('-' * num + '+')
	for i in range(0,num):
		print('|' + ' ' * num + '|' + ' ' * num + '|')
	print('+',end='')
	print('-' * num,end='')
	print('+',end='')
	print('-' * num + '+')
	for i in range(0,num):
		print('|' + ' ' * num + '|' + ' ' * num + '|')
	print('+',end='')
	print('-' * num,end='')
	print('+',end='')
	print('-' * num + '+')
print_grid(15)
