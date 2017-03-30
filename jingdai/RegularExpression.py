import re

string='please help me to find numbers like ABC-123-4567#, YBN-345-8970*'

regex=re.compile(r'\w\w\w-\d\d\d-\d\d\d\d\S')

result= regex.search(string)

print(result.group())

# try group the pattern individually

regex=re.compile(r'(\w\w\w)-(\d\d\d)-(\d\d\d\d\S)') # r for raw_string

result= regex.search(string)

print(result.group(3))

print(result.groups()) # return a tuple

# search function only returns first occurrence , how to return all occurrence?

regex=re.compile(r'\w\w\w-\d\d\d-\d\d\d\d\S')
results= regex.findall(string)
print(results)


