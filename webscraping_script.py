import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

# # URL of the page to scrape (these are done)

url = "https://www.bc.edu/content/bc-web/schools/morrissey/departments/art/people/faculty-directory/asher-anderson.html"

# Send a GET request to the website
response = requests.get(url)

# Parse the page content
#print("Hello World")
soup = BeautifulSoup(response.content, "html.parser")
#gets the contact information and basic info from BC prof website 
sideBars = soup.find_all("div", class_="sidebar")
for sidebar in sideBars:
    print(sidebar.text)
intro = soup.find("div", class_ = "bio-container")
print(intro.text)
