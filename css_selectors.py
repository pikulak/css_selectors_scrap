#!c:/python34/python.exe
import requests
from bs4 import BeautifulSoup as bs4
html_content = requests.get('http://www.w3schools.com/cssref/css_selectors.asp').text
soup = bs4(html_content, 'html5lib')
table = soup.find('table', {'class':'w3-table-all notranslate'})
tbody = table.tbody
rows = tbody.find_all("tr")
f = open('response.txt','w+', encoding='utf8')
for i, rows in enumerate(rows):
    if i == 0:
        continue
    columns = rows.find_all('td')
    selector = columns[0].get_text()
    example = columns[1].get_text()
    example_desc = " ".join(columns[2].get_text().split())
    css = columns[3].get_text().strip()
    prepare = "{};{};{};{}\n".format(
        selector,
        example,
        example_desc,
        css)
    f.write(prepare)
    
    
#f.write(rows.contents)