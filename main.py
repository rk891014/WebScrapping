import requests as requests
import bs4
import io

url = "https://finance.yahoo.com/quote/GC=F?p=GC=F"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, "html.parser")

for gold in :
    print(gold)