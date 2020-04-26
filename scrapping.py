import requests as requests
import bs4


def goldprice():
    url = "https://finance.yahoo.com/quote/GC=F?p=GC=F"
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    gp = soup.findAll('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return gp

def fbparsePrice():
    url = "https://finance.yahoo.com/quote/FB?p=FB"
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    price = soup.findAll('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price
i=0
while True:
    i+=1
    print(str(i)+" The curr facebook price is : "+str(fbparsePrice())+" The curr gold price is : "+str(goldprice()))

