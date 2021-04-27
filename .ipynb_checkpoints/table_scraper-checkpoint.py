import mysql.connector
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Make HTTP get request
url = "https://en.wikipedia.org/wiki/List_of_NFL_franchise_owners"
page = requests.get(url)

# Parse content
content = BeautifulSoup(page.text, "html.parser")

# Get data table
table = content.find("table", class_="wikitable sortable")
#print(table.text)
# Save in Pandas dataframe?
df = pd.read_html(str(table))
#print(df)
df = pd.DataFrame(df[0])
print(df[['Purchase Price', 'Franchise']]['Franchise'].min(), df[['Purchase Price', 'Franchise']].max())

# Get page title
#page_title = content.title.text[:content.title.text.find("-")]
#print(page_title)

#for team in table.find_all('tbody').children:
#    for row in team:
#        #print(row.text.strip())
#        #nfl_teams = row.get("title")
#        print(row.text)


#headers = [h.text for h in table.find_all('th')]
#print(headers)

