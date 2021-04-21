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

df = pd.read_html(str(table))
print(df)
df = pd.DataFrame(df[0])
print(df)


'''
for team in table.find_all('tbody'):
    rows = team.find_all('a')
    for row in rows:
        #print(row.text.strip())
        #nfl_teams = row.get("title")
        print(row.get('title'))
'''

#headers = [h.text for h in table.find_all('th')]
#print(headers)

