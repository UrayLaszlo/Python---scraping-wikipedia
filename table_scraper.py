import mysql.connector
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Make HTTP get request
url = "https://en.wikipedia.org/wiki/List_of_NFL_franchise_owners"
page = requests.get(url)
#print(page.status_code)

# Parse content
content = BeautifulSoup(page.text, "html.parser")

# Get page title
page_title = content.title.text[:content.title.text.find("-")]
#print(page_title)

# Get data table
table = content.find("table", class_="wikitable sortable")
#print(table.text)
# Save in Pandas dataframe?
#df = pd.read_html(str(table))
#print(df)

for team in table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        nfl_team = row.find('td', class_="reference").text
        print(nfl_team)

#print(table)

#headers = [h.text for h in table.find_all('th')]
#print(headers)

