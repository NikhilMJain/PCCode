from bs4 import BeautifulSoup
import requests

r = requests.get('http://shityoucanafford.com/wp-json/wp/v2').json()
soup = BeautifulSoup(r, 'html.parser')
#print(soup.prettify)
mydivs = soup.findAll("div", {"class": "rtitle"})

print(mydivs)