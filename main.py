import requests as requests
import bs4
import io

url="https://www.youtube.com/channel/UCa5UDzFzpIjJ1VSxCSlQP_g/videos"
data=requests.get(url)


soup=bs4.BeautifulSoup(data.text,"html.parser")
formatted_text=soup.prettify()
filename="temp.html"
# print(formatted_text)


with io.open(filename, 'a',encoding="utf-8") as the_file:
    the_file.write(formatted_text)



# this is for finding all para in page

for para in soup.findAll('p'):
    print(para.text)

# for link in soup.findAll('a'):
#     link=link.get('href')
#     # if link[0:3]=="/wa":
#     print(link)
