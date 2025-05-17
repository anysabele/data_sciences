import requests
from bs4 import BeautifulSoup
import pandas

print('Requests: ')
response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
print(response.text[:800])

print('BeautifulSoup: ')
soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:1000])

print('Pandas')
url_dados = pandas.read_html('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
print(url_dados[1].head(10))