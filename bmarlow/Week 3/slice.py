def main():
	s = getstring()
	firstlastswap(s)
	removeeveryother(s)
	firstlastfoureveryother(s)
	reverse(s)
	middlelastfirst(s)

def getstring():
	s = input('Please enter some data for slicing!\n')
	if len(s) < 10:
		print('Please enter at least 10 characters for slicing\n')
		getstring()
	return s


def firstlastswap(s):
	print('sequence with first and last items exchanged')
	stemp = s[0:-1]
	s = s[-1] + stemp + s[0]
	print(s)

def removeeveryother(s):
	print('sequence with every other item removed')
	s = s[::2]
	print(s)

def firstlastfoureveryother(s):
	print('sequence with the first and last four removed and every other character of the remaining stirng removed')
	s = s[3:-4:2]
	print(s)

def reverse(s):
	print('sequence printed in reverse')
	s = s[::-1]
	print(s)

def middlelastfirst(s):
	print('sequence printed in order of middle third, last third, first third')
	length = len(s)
	print(length)
	third = int(length/3)
	third2x = int(third*2)
	first = s[:third]
	middle = s[third:third2x]
	last = s[third2x:]
	s = middle + last + first
	print(s)

if __name__ == '__main__':
	main()