import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

# # URL of the page to scrape (these are done)
# url = "https://www1.wellesley.edu/psychology/faculty"
# url = "https://www.wellesley.edu/academics/department/computer-science"
# url = "https://www.wellesley.edu/academics/program/data-science" 
# url = "https://www.wellesley.edu/academics/department/sociology"
# https://www.wellesley.edu/academics/department/education

# # Read the list of professors from the text file
# with open("psychologyfaculty.txt", "r") as file1:
#     profslist = file1.readlines()

# # Clean the list by removing whitespace and newline characters
# cleaned = [line.rstrip() for line in profslist]

url = "https://www.wellesley.edu/academics/department/mathematics"

# Send a GET request to the website
response = requests.get(url)

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

# Find all anchor tags with the class 'faculty_related_item_title_link'
faculty_links = []
for a_tag in soup.find_all('a', class_='faculty_related_item_title_link'):
    href = a_tag['href']
    faculty_links.append(href)

# Print the faculty links as a list
# Open a CSV file to store the scraped data
department = "Math_faculty.csv"
with open(f"{department}", mode="w", newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Name', 'Email', 'Information']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Loop through each professor's webpage
    for webpage in faculty_links:
        response = requests.get(webpage)  # Send a GET request to the webpage
        soup = BeautifulSoup(response.content, "html.parser")  # Parse the HTML content of the page

        # Extract the professor's name
        name = soup.find(id="page_title").get_text(strip=True) if soup.find(id="page_title") else "N/A"

        # Extract the professor's email
        email = None
        for a_tag in soup.find_all("a", href=True):
            if "mailto:" in a_tag['href']:
                email = a_tag['href'].replace("mailto:", "")
                break

        # Extract additional information (contained in <p> tags)
        info = soup.find_all("p")
        info_word = ' '.join([item.get_text(strip=True) for item in info])

        # Write the data to the CSV file
        writer.writerow({
            'Name': name,
            'Email': email if email else "N/A",
            'Information': info_word
        })

print(f"Data has been successfully written to {department}.")
