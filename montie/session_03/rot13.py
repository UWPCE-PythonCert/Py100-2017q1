#!/usr/bin/env python3
	def rot13(text):
		table = str.maketrans("abcdefghijklmnopqrstuvwxyz","nopqrstuvwxyzabcdefghijklm")
		print(str.translate(text,table))
if __name__== '__main__':
	rot13("This is a test.")
