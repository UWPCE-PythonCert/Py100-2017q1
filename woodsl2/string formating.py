'''String Formatting Lab¶,
Building up strings¶ , For reference:
The official reference docs:
https://docs.python.org/3/library/string.html#string-formatting
And a more human-readable intro:
https://pyformat.info/
And a nice “Cookbook”:
https://mkaz.tech/python-string-format.html
A Couple Exercises¶
Write a format string that will take:
( 2, 123.4567, 10000)
and produce:
'file_002 :   123.46, 1.00e+04'
'''


def formatter(tup):
return ("'the {} numbers are : ").format(len(tup)) + (", ".join(["%d"] * len(tup)) + "'") %tup

print(formatter((1,2,3,4,5)))

"""
sample output

'the 5 numbers are : 1, 2, 3, 4, 5'
"""
