import mysql.connector
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Make HTTP get request
url = "https://en.wikipedia.org/wiki/List_of_NFL_franchise_owners"
page = requests.get(url)

# Parse content
content = BeautifulSoup(page.text, "html.parser")

page_title = content.title.text[:content.title.text.find("-")]
print(page_title)

table = content.find("table", class_="wikitable sortable")
print(table.text)

headers = [h.text for h in table.find_all('th')]
print(headers)

df = pd.read_html(str(table))
print(df)


#rows = table.find_all('tr').text

#print(df.info())
#print(table.text)

