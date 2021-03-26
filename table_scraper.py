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

d = pd.read_html(str(table))

df = d[0]

print(len(d))
print(df.info())
#print(table.text.strip())
