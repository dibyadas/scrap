import requests
from bs4 import BeautifulSoup as bs
url = "https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno=16MA200"
def fetcher(url):
    r = requests.get(url)
    data  = bs(r.content,'html.parser')
    td = data.findAll("td")
    c= 0
    for i in td:
        if i.get_text() == " SGPA":
            c = td[td.index(i)+1]
    print("Name = ",td[4].text ," SGPA = ",c.text)

for i in range(1,52):
	if i<10:
		fetcher(url+"0"+str(i))
	else:
		fetcher(url+str(i))


# url = 




