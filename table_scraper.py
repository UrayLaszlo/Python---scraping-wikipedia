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
table = content.find("table", class_="wikitable sortable")

df = pd.read_html(str(table))

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Lacim_77"
)

print(df)
#print(df.info())
print(table.text)
