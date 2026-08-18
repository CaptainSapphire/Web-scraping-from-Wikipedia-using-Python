import sys
print(sys.executable)

import requests # It is the foundation of web scraping in Python. It allows to send HTTP requests like GET and POST to download web pages quickly and reliably.

import lxml #  for parsing HTML and XML, lxml is extremely fast and ideal for large-scale scraping tasks
from bs4 import BeautifulSoup # HTML parser that creates a parse tree for easy data extraction. It works seamlessly with content fetched using Requests.
from selenium import webdriver # Automates a real browser, enabling scraping of dynamic, JavaScript-loaded websites
import scrapy # A full-featured, asynchronous web scraping framework built for speed and scalability. It is ideal for large crawling projects, providing pipelines and advanced data handling capabilities.

# Note: I had to change the imports a lot because the original site is outdated and I was struggling. 

## Workflow description
### document load --> parsing --> extraction --> transformation


# Get webpages with requests
topic = input("Enter a Wikipedia topic: ") 
url = "https://en.wikipedia.org/wiki/Main_Page"
headers = {
    "User-Agent": "Mozilla/5.0"
}
page = requests.get(url, headers=headers) # requests.get(): sends an HTTP GET request to the website.
print(page.status_code) # page.status_code: returns 200 if the page loaded successfully.
# print(page.content) # page.content: returns the full HTML of the page.
# ^ Useful for the first run, don't need it beyond that.

# parsing html
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

# extra the actual contents
print(soup.find_all('p'))
print("\n\n")
print(soup.find_all('p')[0].get_text())


## Taking the project further
# I want to be able to ask the terminal