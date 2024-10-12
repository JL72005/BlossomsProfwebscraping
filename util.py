import requests
import types
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import regex
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

def getDepartmentFaculty(url=""):
    response = requests.get(url)

    # Parse the page content
    soup = BeautifulSoup(response.content, "html.parser")

    facultyInfo = []

    # Find all elements with the class 'profile-link profile-link-advanced'
    links = soup.find_all('a', href=True)

    for link in links:
        if 'profile' in link['href']:
            print(link['href'])
    
    return [link['href'] for link in links if 'profile' in link['href']]

def getDepartments(url=""):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Target the specific section of the webpage that lists departments
    department_links = soup.find_all('a', class_='button-primary')  # Adjust as per the HTML structure
    # Print the href attribute of each department link
    for link in department_links:
        href = link.get('href')
        if href:
            print(href)
    
    return [link.get('href')+'/people/faculty/' for link in department_links]

# Call the function with the target URL
# getDepartmentFaculty("https://www.bu.edu/afam/people/faculty/")
# getDepartmentFaculty("https://www.bu.edu/mcbb/people/faculty/")
links = getDepartments("https://www.bu.edu/cas/departments/")
with open('buLinks.txt', 'w') as file:
    for link in links:
        facLinks = getDepartmentFaculty(link)
        for fac in facLinks:
            file.write(fac+'\n')
