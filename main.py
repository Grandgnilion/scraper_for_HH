from bs4 import BeautifulSoup
import requests
import lxml
import json
url = "https://hh.ru"
headers = {"Accept": "*/*","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"}
#req = requests.get(url, headers = headers)
#src  = req.text
#with open("file.html", "w") as file:
#    file.write(src)
#with open("file.html") as file:
    #src = file.read
#user = input("Enter vacancy")
#user1 = f'{url}/search/vacancy/?text={user}'
#req1 = requests.get(user1, headers = headers)
#src = req1.text
#with open("file1.html", "w") as file:
#    file.write(src)
with open("file1.html") as file:
    src1 = file.read()
soup = BeautifulSoup(src1,"lxml")
link = soup.find_all(class_="serp-item__title")
all_vacancy = {}
#for item in link:
#    item_text = item.text
#    item_href = item.get("href")
#    all_vacancy[item_text] = item_href
#with open("all_vacancy.json", "w") as file1:
#    json.dump(all_vacancy, file1, indent=4, ensure_ascii=False)
page = soup.find_all(class_ = "bloko-button")
res2 = []
for item in page:
    res = item.text
    res1 = res.split()
    for i in res1:
        if(i.isdigit()):
            res2.append(int(i))
src2 = res2[-1]
user = 'Программист-стажер'
user1 = f'{url}/search/vacancy/?text={user}'
url1 = []
for item in range(int(src2-1)):
    url1.append(user1 + f'&page={item}')
for item in range(url1):
    req = requests.get(url1[item])
    src = req.text
    print(src)