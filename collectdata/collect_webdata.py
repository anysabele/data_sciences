import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Python'
request = requests.get(url)
extraction = BeautifulSoup(request.text,'html.parser')

#display text
#print(extraction.text.strip())

#filter display by tag

for textline in extraction.find_all('h2'):
    title = textline.text.strip()
    print(f'Title: {title}')

for textline in extraction.find_all('p'):
    p = textline.text.strip()
    print(f'Paragraph: {p}')

#count tags
count_h2 = 0
count_p = 0

for textline in extraction.find_all(['h2', 'p']):
    if textline.name == 'h2':
        count_h2 += 1
    elif textline.name == 'p':
       count_p += 1
print(f'\nTitle: {count_h2}')
print(f'Paragraph: {count_p}')

#display nested tags
for title in extraction.find_all('h2'):
    print(f'\nTitle: {title.text.strip()}')
    for link in title.find_next_siblings(['p', 'ul', 'ol']):
        for a in link.find_all('a', href=True):
          print(f'Text link: {a.text.strip()}, | URL: {a['href']}')