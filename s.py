import requests
import sys
from bs4 import BeautifulSoup as bs
url = "https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno=16MA200"
urlx = "https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno="
def fetcher(url):
	r = requests.get(url)
	data  = bs(r.content,'html.parser')
	td = data.findAll("td")
	for i in td:
		if i.get_text() == " SGPA":
			c = td[td.index(i)+1]
	print("Name = ",td[4].text ," SGPA = ",c.text)
def fetch():
	for i in range(1,52):
		if i<10:
			fetcher(url+"0"+str(i))
		else:
			fetcher(url+str(i))
r = sys.argv[1:]



if r:
	try:
		fetcher(urlx+r[0])
	except AttributeError:
		print("Please enter the roll number properly.")
	except KeyboardInterrupt:
		print("\nBye")
else:
	try:
		fetch()
	except KeyboardInterrupt:
		print("\nBye")
