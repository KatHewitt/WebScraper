import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.homebase.co.uk/search/products?q=concrete&redirectFrom=Any'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'}

page = requests.get(url, headers=headers)

#print(page.status_code) #200 code okay response

src = page.content 
#print(src)

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
#print(links)

#list of names 
names = []
for name in soup.find_all("p",{"class":"product-tile__description__text"}):
    names.append(name.text.strip())
  
#list of prices 
prices = []
for price in soup.find_all("span",{"class":"product-tile__price__item"}):
    prices.append(price.text.strip())


#writes code to dataframe 
df = pd.DataFrame(list(zip(names, prices)),
    columns =['names','prices'])
df

#converts dataframe to excel 
df.to_excel("ScrapedData.xlsx")
