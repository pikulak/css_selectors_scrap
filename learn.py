#!c:/python34/python.exe
import requests
from bs4 import BeautifulSoup as bs4
ranking = []
data = {
    'user': 'pikulak',
    'password': '8b761bfd779d3a63f7d6cf7c8c3e0a1edd5211fc',
    'sso': '0'}
url = 'https://www.plemiona.pl/index.php?action=login&server_pl108'
session = requests.session()
f = open('response.txt','w+',encoding="utf8")
with session:
    session.post(url, data=data)
for i in range(1,10):
    url = 'https://pl108.plemiona.pl/game.php?&screen=ranking&rank='+str(i*25)

    print(str(i))
    html_content = session.get(url).text
    soup = bs4(html_content, 'html.parser')
    table = soup.find("table",{'id':'player_ranking_table', 'class':'vis'})
    rows = table.find_all('tr')
    for row in rows:
        hrefs = row.find('a')
        try:
            nick = hrefs.get_text().strip()
            if nick != None:
                ranking.append(nick)
        except AttributeError:
            continue
for i, item in enumerate(ranking):
    s = "{}. {}".format(i+1, item)
    f.write(s+"\n")