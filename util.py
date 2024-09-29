import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import regex

def getIndividualInfo(url=""):
    response = requests.get(url)

    # Parse the page content
    soup = BeautifulSoup(response.content, "html.parser")

    #gets the contact information and basic info from BC prof website 
    sideBars = soup.find("div", class_="sidebar")
    content = regex.sub(r'\n+', '\n', sideBars.text)
    contentList = content.split('\n')
    current_section = None

    individualFaculty = {
        "name": None,
        "contact": {},
        "education": [],
        "courses": []
    }

    for item in contentList:
        item = item.strip()  # Strip any excess whitespace

        if not item:
            continue

        # Check for name and title
        if individualFaculty["name"] is None and "Ph.D." in item:
            individualFaculty["name"] = contentList[contentList.index(item) - 1] + " " + item
            continue

        # Switch sections based on markers
        if item == 'Contact':
            current_section = 'contact'
            continue
        elif item == 'Education':
            current_section = 'education'
            continue
        elif item == 'Courses':
            current_section = 'courses'
            continue
        elif item == 'CV or Resume':
            current_section = None
            continue

        # Populate the dictionary based on the current section
        if current_section == 'contact':
            if 'Telephone' in item:
                individualFaculty['contact']['telephone'] = item.split(': ')[1]
            elif 'Email' in item:
                individualFaculty['contact']['email'] = item.split(': ')[1]
            else:
                individualFaculty['contact']['office'] = item
        elif current_section == 'education':
            individualFaculty['education'].append(item)
        elif current_section == 'courses':
            individualFaculty['courses'].append(item)

    # Output the parsed dictionary
    print(individualFaculty)

    #Introduction paragraph
    intro = soup.find("div", class_ = "bio-container")
    print(intro.text)

    return individualFaculty, intro