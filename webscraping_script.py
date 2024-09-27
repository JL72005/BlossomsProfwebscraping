import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import regex

# # URL of the page to scrape (these are done)

url = "https://www.bc.edu/content/bc-web/schools/morrissey/departments/art/people/faculty-directory/asher-anderson.html"

# Send a GET request to the website
response = requests.get(url)

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

#gets the contact information and basic info from BC prof website 
sideBars = soup.find("div", class_="sidebar")
print(regex.sub(r'\n','-',sideBars.text))

#Introduction paragraph
intro = soup.find("div", class_ = "bio-container")
print(intro.text)