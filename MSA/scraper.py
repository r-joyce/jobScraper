#! Python3
# Job/Internship Scraper - MSA
# By: Ryan Joyce

import requests
import bs4

# Get the page
page = requests.get('https://bms.hanford.gov/HRISJP/JobsList.aspx?BU=MSC&PT=E')

# Check the page
try:
    page.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# Save the page
File = open('MSA/html.txt', 'wb')
for chunk in page.iter_content(100000):
	File.write(chunk)
File.close()

# Find what we want from the HTML
File = open('MSA/html.txt')
soup = bs4.BeautifulSoup(File.read(), "html.parser")
elements = soup.select('.TFtable > tr > td')

# Print header
print("*-- MSA --*\n-----------\nhttps://bms.hanford.gov/HRISJP/JobsList.aspx?BU=MSC&PT=E\n")
print("Number of jobs: ", len(elements)/8, "\n")

# Print out all the jobs
for i in range (0,len(elements)):
	if i % 8 == 0:
		print("Category:       ", elements[i].getText())
	elif i % 8 == 1:
		print("Position Title: ", elements[i].getText())
	elif i % 8 == 2:
		print("Posting #:      ", elements[i].getText())
	elif i % 8 == 3:
		print("Openings:       ", elements[i].getText())
	elif i % 8 == 4:
		print("Reg\Temp:       ", elements[i].getText())
	elif i % 8 == 5:
		print("Company:        ", elements[i].getText())
	elif i % 8 == 6:
		print("Posted Date:    ", elements[i].getText())
	else:
		print("Closing Date:   ", elements[i].getText(), "\n")

