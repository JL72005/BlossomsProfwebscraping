import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import regex
import util


# # URL of the page to scrape (these are done)
response = requests.get('https://www.bc.edu/content/bc-web/academics.html')

soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a', class_='n-btn r-maroon text-center')
#print(links)
schoolLinks = [tag['href'].replace('about', 'department-list') for tag in links]
print(schoolLinks)
url = "https://www.bc.edu/content/bc-web/schools/morrissey/departments/art/people/faculty-directory/asher-anderson.html"

#util.getIndividualInfo(url)
# with open("test.csv", mode="w", newline='', encoding='utf-8') as csv_file:
#     fieldnames = ['sidebarInfo', 'Information']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({
#         'sidebarInfo' : generalData,
#         'Information': regex.sub(r'\n+','\n',intro.text).replace(',', ' ')
#     })

    
# print(f"Data has been successfully written.")
