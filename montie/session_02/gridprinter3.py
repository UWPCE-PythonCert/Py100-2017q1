#!/home/vagrant/.virtualenvs/py100/bin/python
def print_grid(num,size):
	lineupspace=size-1
	for i in range(0,num):
		for i in range(0,num):	
			print('+'+'-'*size,end='')
		print('+')
		for i in range(0,size):
			for i in range(0,num):
				print('|',' '*lineupspace,end='')
			print('|')
	
	for i in range(0,num):	
		print('+'+'-'*size,end='')
	print('+')
print_grid(4,9)
