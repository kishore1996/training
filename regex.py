import os
import re

filename = 'kishoreresume.txt'
newfilename = 'result.txt'

os.path.isdir("C:/Users/kishore/Downloads/pdf_convert")
data = open(filename,'r')
a = data.read()

r = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')
results = r.findall(a)
email = ""
for x in results:
	email += str(x)+"\n"

def writefile():
	f = open(newfilename, 'w')
	f.write(email)
	f.close()
	print ("File written.")
writefile();