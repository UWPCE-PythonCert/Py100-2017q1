#!/usr/bin/env python3
def seq1():
	sequence = ['one','two','three','four','five']
	print(sequence[-1:] + sequence[1:-1] + sequence[:1])
def seq2():
	sequence = [1,2,3,4,5]
	print(sequence[::2])
def seq3():
	sequence = ['one','two','three','four','five','six','seven','eight','nine','ten']
	sequence2 = sequence[1:-4]
	print(sequence2[::2])	
def seq4():
	sequence = [1,2,3,4,5]
	print(sequence[::-1])
def seq5():
	sequence = ['one','two','three','four','five','six','seven','eight','nine',]
	athird = len(sequence)/3
	middle = athird * 2
	last = athird * 3
	first = athird
	print(sequence[int(first):] + sequence[:int(first)])
seq1()
seq2()
seq3()
seq4()
seq5()
