import re


comments = open("Act6.csv", "r", newline = "\r\n")

regex = re.compile(r'CVE-\d\d\d\d-\d\d\d\d')#Look for CVE number

f=open('cve_sr_title.csv','w')
for line in comments:
    list1= line.strip().split(',')
    sr=list1[0]# return a string
    cve_title = regex.findall(line) # return a list of strings
    for title in cve_title:
         sr_plus_title = sr + title
         print(sr_plus_title,file=f)
