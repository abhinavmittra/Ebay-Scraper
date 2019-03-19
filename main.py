import requests
from bs4 import BeautifulSoup
import pandas as pd

result = requests.get("https://www.ebay.com/deals")
ebay_page=result.content
soup=BeautifulSoup(ebay_page,'html.parser')

#Container with all featured items
featured_items_container = soup.find_all('div','ebayui-dne-item-featured-card')

#Collecting each featuired items in the container
items = featured_items_container[0].find_all('div','dne-itemtile dne-itemtile-medium')
#titles = [item.find('h3').get('title') for item in items]
titles=[]
prices = []
for index,item in enumerate(items):
  #print('{}. {}'.format(index+1,item.find('h3').get('title')))
  titles.append(item.find('h3').get('title'))
  #Some items don't have a price so we insert NA instead of their price
  if item.find('div','dne-itemtile-price'):
    prices.append(item.find('div','dne-itemtile-price').text)
  else:
    prices.append('NA')
result_final = pd.DataFrame(
  {
  'Title': titles,
  'Price': prices,
  }
)

result_final.to_csv('ebay_deals.csv')
print("Done")