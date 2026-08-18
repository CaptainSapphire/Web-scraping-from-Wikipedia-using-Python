import requests # It is the foundation of web scraping in Python. It allows to send HTTP requests like GET and POST to download web pages quickly and reliably.

import lxml #  A high-performance library for parsing HTML and XML, lxml is extremely fast and ideal for large-scale scraping tasks
import BeautifulSoup # A beginner-friendly HTML parser that creates a parse tree for easy data extraction. It works seamlessly with content fetched using Requests.
import Selenium # Automates a real browser, enabling scraping of dynamic, JavaScript-loaded websites. It is slower than other tools and less suitable for large-scale scraping.
import Scrapy # A full-featured, asynchronous web scraping framework built for speed and scalability. It is ideal for large crawling projects, providing pipelines and advanced data handling capabilities.



## Workflow description
### document load --> parsing --> extraction --> transformation


url = "https://en.wikipedia.org/wiki/Main_Page"
headers = {
    "User-Agent": "Mozilla/5.0"
}
page = requests.get(url, headers=headers) # requests.get(): sends an HTTP GET request to the website.
print(page.status_code) # page.status_code: returns 200 if the page loaded successfully.
print(page.content) # page.content: returns the full HTML of the page.
