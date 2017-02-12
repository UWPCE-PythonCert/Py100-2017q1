import csv
with open('test_csv.csv', 'r') as csvFile:
	csvFileReader = csv.reader(csvFile)
	csvList = []
	for row in csvFileReader:
		if len(row) != 0:
			csvList += [row]

csvFile.close()

for item in csvList:
	print(item[0].title() +
		item[1].title() +
		" is a" + item[2] +
		" for" + item[3].title() +
		" in" + item[4].title() +
		".")