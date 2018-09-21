import os
import datetime
import csv
import re
from os import path
from datetime import datetime, timedelta

#file names and paths
filePath0  = os.path.abspath("<YOUR PATH>")#ENTER PATH TO FILE
fileName0 = "<YOUR FILE NAME>" #ENTER NAME OF CSV

#date variables
today = datetime.now()
oldEntryDate = today - timedelta(days=60)

class fileUpdate:
	def __init__(self, filePath, file):
		self.filePath = filePath
		self.file = file

	def main(self):
		try:
			with open(self.filePath + "/" + self.file, 'rb') as csvfile, open(self.filePath + "/" + today.strftime('%Y%m%d') + self.file, 'wb') as out:
				reader = csv.reader(csvfile)
				writer = csv.writer(out, delimiter=',')
				#assigning date to a string variable
				oldDate = oldEntryDate.strftime('%Y%m%d') #date string of yyyymmdd
				r = re.compile("\d{4}\d{2}\d{2}") #regex to identify date patterns of yyyymmdd
				#loop through rows in reader
				for row in reader:
					substrings=filter(r.match, row) #searching for matching patterns in row
					if not substrings:
						writer.writerow(list(row)) #write this first because of 
					for y in substrings:
						if y >= oldDate: #if y is older than 120 days
							writer.writerow(list(row)) #write the rows to the newfile
		except csv.Error as e:
			sys.exit('file %s, line %d: %s' % (self.file, reader.line_num, e))
		os.remove(self.filePath + "/" + self.file) #remove the original file
		os.rename(self.filePath + "/" + today.strftime('%Y%m%d') + self.file, self.filePath + "/" + self.file) #rename the newfile with the original file's name

if __name__ == '__main__':
    class0 = fileUpdate(filePath0, fileName0)
    class0.main()
