import requests
from requests import status_codes
from bs4 import BeautifulSoup

# Make HTTP get request
response = requests.get(
    url="https://en.wikipedia.org/wiki/List_of_professional_sports_team_owners"
)

# Parse content
content = BeautifulSoup(response.text, 'lxml')

# Get list of teams
teams = [team.text for team in content.find_all('dt')]

# Get team owners
owners = [owner.text for owner in content.find_all('a') if owner.text.isalpha()]

#for owner in owners:
for owner in owners:
    print(owner)
