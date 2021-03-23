from bs4 import BeautifulSoup
import requests
import pandas as pd

# Make HTTP get request
url = "https://en.wikipedia.org/wiki/List_of_NFL_franchise_owners"
page = requests.get(url)

# Parse content
content = BeautifulSoup(page.text, "html.parser")

page_title = content.title.text[:content.title.text.find("-")]
all_tables = content.find_all("table", class_="wikitable sortable")

df = pd.read_html(str(all_tables))

print(df[-1])